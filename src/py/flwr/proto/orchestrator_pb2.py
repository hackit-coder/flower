# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flwr/proto/orchestrator.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flwr.proto import fab_pb2 as flwr_dot_proto_dot_fab__pb2
from flwr.proto import transport_pb2 as flwr_dot_proto_dot_transport__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x66lwr/proto/orchestrator.proto\x12\nflwr.proto\x1a\x14\x66lwr/proto/fab.proto\x1a\x1a\x66lwr/proto/transport.proto\"\xf8\x01\n\x10\x43reateRunRequest\x12\x0e\n\x06\x66\x61\x62_id\x18\x01 \x01(\t\x12\x13\n\x0b\x66\x61\x62_version\x18\x02 \x01(\t\x12I\n\x0foverride_config\x18\x03 \x03(\x0b\x32\x30.flwr.proto.CreateRunRequest.OverrideConfigEntry\x12\x1c\n\x03\x66\x61\x62\x18\x04 \x01(\x0b\x32\x0f.flwr.proto.Fab\x12\x0b\n\x03ttl\x18\x05 \x01(\x01\x1aI\n\x13OverrideConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.flwr.proto.Scalar:\x02\x38\x01\"4\n\x11\x43reateRunResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0e\n\x06run_id\x18\x02 \x01(\x12\"%\n\x13GetRunStatusRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\x12\"&\n\x14GetRunStatusResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\xab\x01\n\x0cOrchestrator\x12H\n\tCreateRun\x12\x1c.flwr.proto.CreateRunRequest\x1a\x1d.flwr.proto.CreateRunResponse\x12Q\n\x0cGetRunStatus\x12\x1f.flwr.proto.GetRunStatusRequest\x1a .flwr.proto.GetRunStatusResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flwr.proto.orchestrator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CREATERUNREQUEST_OVERRIDECONFIGENTRY']._options = None
  _globals['_CREATERUNREQUEST_OVERRIDECONFIGENTRY']._serialized_options = b'8\001'
  _globals['_CREATERUNREQUEST']._serialized_start=96
  _globals['_CREATERUNREQUEST']._serialized_end=344
  _globals['_CREATERUNREQUEST_OVERRIDECONFIGENTRY']._serialized_start=271
  _globals['_CREATERUNREQUEST_OVERRIDECONFIGENTRY']._serialized_end=344
  _globals['_CREATERUNRESPONSE']._serialized_start=346
  _globals['_CREATERUNRESPONSE']._serialized_end=398
  _globals['_GETRUNSTATUSREQUEST']._serialized_start=400
  _globals['_GETRUNSTATUSREQUEST']._serialized_end=437
  _globals['_GETRUNSTATUSRESPONSE']._serialized_start=439
  _globals['_GETRUNSTATUSRESPONSE']._serialized_end=477
  _globals['_ORCHESTRATOR']._serialized_start=480
  _globals['_ORCHESTRATOR']._serialized_end=651
# @@protoc_insertion_point(module_scope)
