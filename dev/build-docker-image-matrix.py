"""
Usage: python dev/build-docker-image-matrix.py --flwr-version <flower version e.g. 1.9.0>
"""

import argparse
import json
from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any, Callable, Dict, List, Optional


class DistroName(str, Enum):
    ALPINE = "alpine"
    UBUNTU = "ubuntu"


@dataclass
class Distro:
    name: "DistroName"
    version: str


LATEST_SUPPORTED_PYTHON_VERSION = "3.11"
SUPPORTED_PYTHON_VERSIONS = [
    "3.9",
    "3.10",
    LATEST_SUPPORTED_PYTHON_VERSION,
]

DOCKERFILE_ROOT = "src/docker"

UBUNTU_24_04 = Distro(DistroName.UBUNTU, "24.04")
ALPINE_3_19 = Distro(DistroName.ALPINE, "3.19")


@dataclass
class BaseImage:
    distro: Distro
    python_version: str
    namespace_repository: str
    file_dir: str
    tag: str
    flwr_version: str


def new_base_image(
    flwr_version: str, python_version: str, distro: Distro
) -> Dict[str, Any]:
    return BaseImage(
        distro,
        python_version,
        "flwr/base",
        f"{DOCKERFILE_ROOT}/base/{distro.name.value}",
        f"{flwr_version}-py{python_version}-{distro.name.value}{distro.version}",
        flwr_version,
    )


def generate_base_images(
    flwr_version: str, python_versions: List[str], distros: List[Dict[str, str]]
) -> List[Dict[str, Any]]:
    return [
        new_base_image(flwr_version, python_version, distro)
        for distro in distros
        for python_version in python_versions
    ]


@dataclass
class BinaryImage:
    namespace_repository: str
    file_dir: str
    base_image: str
    tags: List[str]


def new_binary_image(
    name: str,
    base_image: BaseImage,
    tags_fn: Optional[Callable],
) -> Dict[str, Any]:
    tags = []
    if tags_fn is not None:
        tags += tags_fn(base_image) or []

    return BinaryImage(
        f"flwr/{name}",
        f"{DOCKERFILE_ROOT}/{name}",
        base_image.tag,
        "\n".join(tags),
    )


def generate_binary_images(
    name: str,
    base_images: List[BaseImage],
    tags_fn: Optional[Callable] = None,
    filter: Optional[Callable] = None,
) -> List[Dict[str, Any]]:
    filter = filter or (lambda _: True)

    return [
        new_binary_image(name, image, tags_fn) for image in base_images if filter(image)
    ]


def tag_latest_alpine_with_flwr_version(image: BaseImage) -> List[str]:
    if (
        image.distro.name == DistroName.ALPINE
        and image.python_version == LATEST_SUPPORTED_PYTHON_VERSION
    ):
        return [image.tag, image.flwr_version]
    else:
        return [image.tag]


def tag_latest_ubuntu_with_flwr_version(image: BaseImage) -> List[str]:
    if (
        image.distro.name == DistroName.UBUNTU
        and image.python_version == LATEST_SUPPORTED_PYTHON_VERSION
    ):
        return [image.tag, image.flwr_version]
    else:
        return [image.tag]


def generate_complete_matrix(flwr_version: str):
    """Generates a matrix comprising Ubuntu and Alpine images. For Alpine, the matrix
    includes only the latest supported Python version, whereas for Ubuntu, it includes all
    supported Python versions.
    """

    # ubuntu base images for each supported python version
    ubuntu_base_images = generate_base_images(
        flwr_version,
        SUPPORTED_PYTHON_VERSIONS,
        [UBUNTU_24_04],
    )
    # alpine base images for the latest supported python version
    alpine_base_images = generate_base_images(
        flwr_version,
        [LATEST_SUPPORTED_PYTHON_VERSION],
        [ALPINE_3_19],
    )

    base_images = ubuntu_base_images + alpine_base_images

    binary_images = (
        # ubuntu and alpine images for the latest supported python version
        generate_binary_images(
            "superlink",
            base_images,
            tag_latest_alpine_with_flwr_version,
            lambda image: image.python_version == LATEST_SUPPORTED_PYTHON_VERSION,
        )
        # ubuntu images for each supported python version
        # and alpine image for the latest supported python version
        + generate_binary_images(
            "supernode",
            base_images,
            tag_latest_alpine_with_flwr_version,
            lambda image: image.distro.name == DistroName.UBUNTU
            or (
                image.distro.name == DistroName.ALPINE
                and image.python_version == LATEST_SUPPORTED_PYTHON_VERSION
            ),
        )
        # ubuntu images for each supported python version
        + generate_binary_images(
            "serverapp",
            base_images,
            tag_latest_ubuntu_with_flwr_version,
            lambda image: image.distro.name == DistroName.UBUNTU,
        )
        # ubuntu images for each supported python version
        + generate_binary_images(
            "superexec",
            base_images,
            tag_latest_ubuntu_with_flwr_version,
            lambda image: image.distro.name == DistroName.UBUNTU,
        )
        # ubuntu images for each supported python version
        + generate_binary_images(
            "clientapp",
            base_images,
            tag_latest_ubuntu_with_flwr_version,
            lambda image: image.distro.name == DistroName.UBUNTU,
        )
    )

    return base_images, binary_images


def generate_ubuntu_python_latest_matrix(flwr_version: str):
    """Generates a matrix comprising Ubuntu images. It includes only the latest supported Python
    version.
    """

    # ubuntu base image for the latest supported python version
    base_images = generate_base_images(
        flwr_version,
        [LATEST_SUPPORTED_PYTHON_VERSION],
        [UBUNTU_24_04],
    )

    binary_images = (
        # ubuntu and alpine images for the latest supported python version
        generate_binary_images("superlink", base_images)
        # ubuntu images for the latest supported python version
        + generate_binary_images("supernode", base_images)
        # ubuntu images for the latest supported python version
        + generate_binary_images("serverapp", base_images)
        # ubuntu images for the latest supported python version
        + generate_binary_images("superexec", base_images)
        # ubuntu images for the latest supported python version
        + generate_binary_images("clientapp", base_images)
    )

    return base_images, binary_images


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        description="Generate Github Docker workflow matrix"
    )
    arg_parser.add_argument("--flwr-version", type=str, required=True)
    arg_parser.add_argument("--simple", action="store_true")
    args = arg_parser.parse_args()

    flwr_version = args.flwr_version
    simple = args.simple

    if simple:
        base_images, binary_images = generate_ubuntu_python_latest_matrix(flwr_version)
    else:
        base_images, binary_images = generate_complete_matrix(flwr_version)

    print(
        json.dumps(
            {
                "base": {"images": list(map(lambda image: asdict(image), base_images))},
                "binary": {
                    "images": list(map(lambda image: asdict(image), binary_images))
                },
            }
        )
    )
