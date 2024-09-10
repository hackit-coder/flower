"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import flwr.proto.driver_pb2
import flwr.proto.fab_pb2
import flwr.proto.orchestrator_pb2
import flwr.proto.run_pb2
import grpc

class DriverStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    CreateRun: grpc.UnaryUnaryMultiCallable[
        flwr.proto.orchestrator_pb2.CreateRunRequest,
        flwr.proto.orchestrator_pb2.CreateRunResponse]
    """Request run_id"""

    GetNodes: grpc.UnaryUnaryMultiCallable[
        flwr.proto.driver_pb2.GetNodesRequest,
        flwr.proto.driver_pb2.GetNodesResponse]
    """Return a set of nodes"""

    PushTaskIns: grpc.UnaryUnaryMultiCallable[
        flwr.proto.driver_pb2.PushTaskInsRequest,
        flwr.proto.driver_pb2.PushTaskInsResponse]
    """Create one or more tasks"""

    PullTaskRes: grpc.UnaryUnaryMultiCallable[
        flwr.proto.driver_pb2.PullTaskResRequest,
        flwr.proto.driver_pb2.PullTaskResResponse]
    """Get task results"""

    GetRun: grpc.UnaryUnaryMultiCallable[
        flwr.proto.run_pb2.GetRunRequest,
        flwr.proto.run_pb2.GetRunResponse]
    """Get run details"""

    GetFab: grpc.UnaryUnaryMultiCallable[
        flwr.proto.fab_pb2.GetFabRequest,
        flwr.proto.fab_pb2.GetFabResponse]
    """Get FAB"""


class DriverServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def CreateRun(self,
        request: flwr.proto.orchestrator_pb2.CreateRunRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.orchestrator_pb2.CreateRunResponse:
        """Request run_id"""
        pass

    @abc.abstractmethod
    def GetNodes(self,
        request: flwr.proto.driver_pb2.GetNodesRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.driver_pb2.GetNodesResponse:
        """Return a set of nodes"""
        pass

    @abc.abstractmethod
    def PushTaskIns(self,
        request: flwr.proto.driver_pb2.PushTaskInsRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.driver_pb2.PushTaskInsResponse:
        """Create one or more tasks"""
        pass

    @abc.abstractmethod
    def PullTaskRes(self,
        request: flwr.proto.driver_pb2.PullTaskResRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.driver_pb2.PullTaskResResponse:
        """Get task results"""
        pass

    @abc.abstractmethod
    def GetRun(self,
        request: flwr.proto.run_pb2.GetRunRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.run_pb2.GetRunResponse:
        """Get run details"""
        pass

    @abc.abstractmethod
    def GetFab(self,
        request: flwr.proto.fab_pb2.GetFabRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.fab_pb2.GetFabResponse:
        """Get FAB"""
        pass


def add_DriverServicer_to_server(servicer: DriverServicer, server: grpc.Server) -> None: ...
