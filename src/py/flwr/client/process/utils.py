# Copyright 2024 Flower Labs GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Flower ClientApp loading utils."""

from logging import DEBUG, WARN
from pathlib import Path
from typing import Callable, Optional

from flwr.client.client_app import ClientApp, LoadClientAppError
from flwr.common.config import get_flwr_dir, get_project_config, get_project_dir
from flwr.common.logger import log
from flwr.common.object_ref import load_app, validate


def _get_load_client_app_fn(
    default_app_ref: str,
    project_dir: str,
    multi_app: bool,
    flwr_dir: Optional[str] = None,
) -> Callable[[str, str], ClientApp]:
    """Get the load_client_app_fn function.

    If `multi_app` is True, this function loads the specified ClientApp
    based on `fab_id` and `fab_version`. If `fab_id` is empty, a default
    ClientApp will be loaded.

    If `multi_app` is False, it ignores `fab_id` and `fab_version` and
    loads a default ClientApp.
    """
    if not multi_app:
        log(
            DEBUG,
            "Flower SuperNode will load and validate ClientApp `%s`",
            default_app_ref,
        )

        valid, error_msg = validate(default_app_ref, project_dir=project_dir)
        if not valid and error_msg:
            raise LoadClientAppError(error_msg) from None

    def _load(fab_id: str, fab_version: str) -> ClientApp:
        runtime_project_dir = Path(project_dir).absolute()
        # If multi-app feature is disabled
        if not multi_app:
            # Set app reference
            client_app_ref = default_app_ref
        # If multi-app feature is enabled but the fab id is not specified
        elif fab_id == "":
            if default_app_ref == "":
                raise LoadClientAppError(
                    "Invalid FAB ID: The FAB ID is empty.",
                ) from None

            log(WARN, "FAB ID is not provided; the default ClientApp will be loaded.")

            # Set app reference
            client_app_ref = default_app_ref
        # If multi-app feature is enabled
        else:
            try:
                runtime_project_dir = get_project_dir(
                    fab_id, fab_version, get_flwr_dir(flwr_dir)
                )
                config = get_project_config(runtime_project_dir)
            except Exception as e:
                raise LoadClientAppError("Failed to load ClientApp") from e

            # Set app reference
            client_app_ref = config["tool"]["flwr"]["app"]["components"]["clientapp"]

        # Load ClientApp
        log(
            DEBUG,
            "Loading ClientApp `%s`",
            client_app_ref,
        )
        client_app = load_app(client_app_ref, LoadClientAppError, runtime_project_dir)

        if not isinstance(client_app, ClientApp):
            raise LoadClientAppError(
                f"Attribute {client_app_ref} is not of type {ClientApp}",
            ) from None

        return client_app

    return _load