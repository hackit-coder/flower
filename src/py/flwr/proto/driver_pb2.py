# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flwr/proto/driver.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flwr.proto import node_pb2 as flwr_dot_proto_dot_node__pb2
from flwr.proto import task_pb2 as flwr_dot_proto_dot_task__pb2
from flwr.proto import run_pb2 as flwr_dot_proto_dot_run__pb2
from flwr.proto import common_pb2 as flwr_dot_proto_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x66lwr/proto/driver.proto\x12\nflwr.proto\x1a\x15\x66lwr/proto/node.proto\x1a\x15\x66lwr/proto/task.proto\x1a\x14\x66lwr/proto/run.proto\x1a\x17\x66lwr/proto/common.proto\"\xd9\x01\n\x10\x43reateRunRequest\x12\x0e\n\x06\x66\x61\x62_id\x18\x01 \x01(\t\x12\x13\n\x0b\x66\x61\x62_version\x18\x02 \x01(\t\x12I\n\x0foverride_config\x18\x03 \x03(\x0b\x32\x30.flwr.proto.CreateRunRequest.OverrideConfigEntry\x1aU\n\x13OverrideConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.flwr.proto.ConfigsRecordValue:\x02\x38\x01\"#\n\x11\x43reateRunResponse\x12\x0e\n\x06run_id\x18\x01 \x01(\x12\"!\n\x0fGetNodesRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\x12\"3\n\x10GetNodesResponse\x12\x1f\n\x05nodes\x18\x01 \x03(\x0b\x32\x10.flwr.proto.Node\"@\n\x12PushTaskInsRequest\x12*\n\rtask_ins_list\x18\x01 \x03(\x0b\x32\x13.flwr.proto.TaskIns\"\'\n\x13PushTaskInsResponse\x12\x10\n\x08task_ids\x18\x02 \x03(\t\"F\n\x12PullTaskResRequest\x12\x1e\n\x04node\x18\x01 \x01(\x0b\x32\x10.flwr.proto.Node\x12\x10\n\x08task_ids\x18\x02 \x03(\t\"A\n\x13PullTaskResResponse\x12*\n\rtask_res_list\x18\x01 \x03(\x0b\x32\x13.flwr.proto.TaskRes2\x84\x03\n\x06\x44river\x12J\n\tCreateRun\x12\x1c.flwr.proto.CreateRunRequest\x1a\x1d.flwr.proto.CreateRunResponse\"\x00\x12G\n\x08GetNodes\x12\x1b.flwr.proto.GetNodesRequest\x1a\x1c.flwr.proto.GetNodesResponse\"\x00\x12P\n\x0bPushTaskIns\x12\x1e.flwr.proto.PushTaskInsRequest\x1a\x1f.flwr.proto.PushTaskInsResponse\"\x00\x12P\n\x0bPullTaskRes\x12\x1e.flwr.proto.PullTaskResRequest\x1a\x1f.flwr.proto.PullTaskResResponse\"\x00\x12\x41\n\x06GetRun\x12\x19.flwr.proto.GetRunRequest\x1a\x1a.flwr.proto.GetRunResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flwr.proto.driver_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CREATERUNREQUEST_OVERRIDECONFIGENTRY']._options = None
  _globals['_CREATERUNREQUEST_OVERRIDECONFIGENTRY']._serialized_options = b'8\001'
  _globals['_CREATERUNREQUEST']._serialized_start=133
  _globals['_CREATERUNREQUEST']._serialized_end=350
  _globals['_CREATERUNREQUEST_OVERRIDECONFIGENTRY']._serialized_start=265
  _globals['_CREATERUNREQUEST_OVERRIDECONFIGENTRY']._serialized_end=350
  _globals['_CREATERUNRESPONSE']._serialized_start=352
  _globals['_CREATERUNRESPONSE']._serialized_end=387
  _globals['_GETNODESREQUEST']._serialized_start=389
  _globals['_GETNODESREQUEST']._serialized_end=422
  _globals['_GETNODESRESPONSE']._serialized_start=424
  _globals['_GETNODESRESPONSE']._serialized_end=475
  _globals['_PUSHTASKINSREQUEST']._serialized_start=477
  _globals['_PUSHTASKINSREQUEST']._serialized_end=541
  _globals['_PUSHTASKINSRESPONSE']._serialized_start=543
  _globals['_PUSHTASKINSRESPONSE']._serialized_end=582
  _globals['_PULLTASKRESREQUEST']._serialized_start=584
  _globals['_PULLTASKRESREQUEST']._serialized_end=654
  _globals['_PULLTASKRESRESPONSE']._serialized_start=656
  _globals['_PULLTASKRESRESPONSE']._serialized_end=721
  _globals['_DRIVER']._serialized_start=724
  _globals['_DRIVER']._serialized_end=1112
# @@protoc_insertion_point(module_scope)
