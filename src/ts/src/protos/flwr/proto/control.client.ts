// @generated by protobuf-ts 2.9.4
// @generated from protobuf file "flwr/proto/control.proto" (package "flwr.proto", syntax proto3)
// tslint:disable
//
// Copyright 2024 Flower Labs GmbH. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// ==============================================================================
//
import type { RpcTransport } from "@protobuf-ts/runtime-rpc";
import type { ServiceInfo } from "@protobuf-ts/runtime-rpc";
import { Control } from "./control";
import type { UpdateRunStatusResponse } from "./run";
import type { UpdateRunStatusRequest } from "./run";
import type { GetRunStatusResponse } from "./run";
import type { GetRunStatusRequest } from "./run";
import { stackIntercept } from "@protobuf-ts/runtime-rpc";
import type { CreateRunResponse } from "./run";
import type { CreateRunRequest } from "./run";
import type { UnaryCall } from "@protobuf-ts/runtime-rpc";
import type { RpcOptions } from "@protobuf-ts/runtime-rpc";
/**
 * @generated from protobuf service flwr.proto.Control
 */
export interface IControlClient {
    /**
     * Request to create a new run
     *
     * @generated from protobuf rpc: CreateRun(flwr.proto.CreateRunRequest) returns (flwr.proto.CreateRunResponse);
     */
    createRun(input: CreateRunRequest, options?: RpcOptions): UnaryCall<CreateRunRequest, CreateRunResponse>;
    /**
     * Get the status of a given run
     *
     * @generated from protobuf rpc: GetRunStatus(flwr.proto.GetRunStatusRequest) returns (flwr.proto.GetRunStatusResponse);
     */
    getRunStatus(input: GetRunStatusRequest, options?: RpcOptions): UnaryCall<GetRunStatusRequest, GetRunStatusResponse>;
    /**
     * Update the status of a given run
     *
     * @generated from protobuf rpc: UpdateRunStatus(flwr.proto.UpdateRunStatusRequest) returns (flwr.proto.UpdateRunStatusResponse);
     */
    updateRunStatus(input: UpdateRunStatusRequest, options?: RpcOptions): UnaryCall<UpdateRunStatusRequest, UpdateRunStatusResponse>;
}
/**
 * @generated from protobuf service flwr.proto.Control
 */
export class ControlClient implements IControlClient, ServiceInfo {
    typeName = Control.typeName;
    methods = Control.methods;
    options = Control.options;
    constructor(private readonly _transport: RpcTransport) {
    }
    /**
     * Request to create a new run
     *
     * @generated from protobuf rpc: CreateRun(flwr.proto.CreateRunRequest) returns (flwr.proto.CreateRunResponse);
     */
    createRun(input: CreateRunRequest, options?: RpcOptions): UnaryCall<CreateRunRequest, CreateRunResponse> {
        const method = this.methods[0], opt = this._transport.mergeOptions(options);
        return stackIntercept<CreateRunRequest, CreateRunResponse>("unary", this._transport, method, opt, input);
    }
    /**
     * Get the status of a given run
     *
     * @generated from protobuf rpc: GetRunStatus(flwr.proto.GetRunStatusRequest) returns (flwr.proto.GetRunStatusResponse);
     */
    getRunStatus(input: GetRunStatusRequest, options?: RpcOptions): UnaryCall<GetRunStatusRequest, GetRunStatusResponse> {
        const method = this.methods[1], opt = this._transport.mergeOptions(options);
        return stackIntercept<GetRunStatusRequest, GetRunStatusResponse>("unary", this._transport, method, opt, input);
    }
    /**
     * Update the status of a given run
     *
     * @generated from protobuf rpc: UpdateRunStatus(flwr.proto.UpdateRunStatusRequest) returns (flwr.proto.UpdateRunStatusResponse);
     */
    updateRunStatus(input: UpdateRunStatusRequest, options?: RpcOptions): UnaryCall<UpdateRunStatusRequest, UpdateRunStatusResponse> {
        const method = this.methods[2], opt = this._transport.mergeOptions(options);
        return stackIntercept<UpdateRunStatusRequest, UpdateRunStatusResponse>("unary", this._transport, method, opt, input);
    }
}
