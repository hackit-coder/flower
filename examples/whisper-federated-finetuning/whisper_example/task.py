"""whisper_example: A Flower / PyTorch app with OpenAi's Whisper."""

import random

from flwr_datasets import FederatedDataset
from flwr_datasets.partitioner import NaturalIdPartitioner
from transformers import WhisperProcessor

from datasets import Dataset, concatenate_datasets

fds = None  # Cache FederatedDataset
processor = WhisperProcessor.from_pretrained("openai/whisper-tiny")
REMOVE_COLS = ["file", "audio", "label", "is_unknown", "speaker_id", "utterance_id"]


def load_data(
    partition_id: int,
    save_partition_to_disk: bool,
    partitions_save_path: str,
):
    # Only initialize `FederatedDataset` once
    global fds
    if fds is None:
        partitioner = NaturalIdPartitioner(partition_by="speaker_id")
        fds = FederatedDataset(
            dataset="speech_commands",
            subset="v0.02",
            partitioners={"train": partitioner},
        )

    partition = fds.load_partition(partition_id)

    encoding_fn = get_encoding_fn(processor)

    partition = partition.map(encoding_fn, num_proc=4, remove_columns=REMOVE_COLS)

    # now let's add some _silence_ training examples (add 10% of total examples in this client's data)
    partitioner = fds.partitioners["train"]
    ratio_silences_for_client = 0.1 * (len(partition) / len(partitioner.dataset))
    silence_dataset = prepare_silences_dataset(
        partitioner.dataset, ratio_silences_for_client
    )
    if len(silence_dataset) > 0:
        print(
            f"Adding {len(silence_dataset)} to client data ({len(partition)}) -- partition: {partition_id}"
        )
        silence_enc = silence_dataset.map(encoding_fn)

        partition = concatenate_datasets([partition, silence_enc])
    else:
        print(
            f"Partition is small ({len(partition)}), skipping adding noise. -- partition: {partition_id}"
        )
    if save_partition_to_disk:
        # save dataset. It will be loaded next time this client is spawned
        partition.save_to_disk(f"{partitions_save_path}/client{partition_id}.hf")
    return partition


def get_encoding_fn(processor):
    """Return a function to use to pre-process/encode the SpeechCommands dataset.

    We are working with the 12classes version of this dataset, therefore we need to do
    some reassignment of labels.
    """

    def prepare_dataset(batch):
        audio = batch["audio"]
        data = {}
        data["data"] = processor(
            audio["array"], sampling_rate=audio["sampling_rate"], return_tensors="pt"
        ).input_features

        # All unknown keywords are assigned label 11. The silence clips get assigned label 10
        # In this way we have 12 classes with labels 0-11
        data["targets"] = (
            11
            if batch["is_unknown"]
            else (10 if batch["label"] == 35 else batch["label"])
        )
        return data

    return prepare_dataset


def prepare_silences_dataset(train_dataset, ratio_silence: float = 0.1) -> Dataset:
    """Generate silences for the train set.

    One of the classes in the SpeechCommands datatset is `silence`. However, the dataset
    does not include clips of silence. It does however include 5 long files with
    different background sounds. The taks of this function is to extract several
    (defined by `ratio_silence`) one-second long clips from those background audio
    files. Later, those audio clips will be included into the training set.
    """
    # retrieve original silence audio clips
    silences = train_dataset.filter(lambda x: x["label"] == 35)
    # figure out how many to add
    num_silence_total = int(len(train_dataset) * ratio_silence)
    # num new entries per background noise clip
    num_silence_per_bkg = num_silence_total // len(silences)

    silence_to_add = []
    for sil in silences:
        sil_array = sil["audio"]["array"]
        sr = sil["audio"]["sampling_rate"]
        # print(f"Extracting audio from: {sil['file']} ...")
        for _ in range(num_silence_per_bkg):
            random_offset = random.randint(0, len(sil_array) - sr - 1)
            sil_array_crop = sil_array[random_offset : random_offset + sr]

            entry = sil
            silence_to_add.append(entry)
            silence_to_add[-1]["audio"]["array"] = sil_array_crop

    return Dataset.from_list(silence_to_add)