"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import flwr.proto.orchestrator_pb2
import grpc

class OrchestratorStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    CreateRun: grpc.UnaryUnaryMultiCallable[
        flwr.proto.orchestrator_pb2.CreateRunRequest,
        flwr.proto.orchestrator_pb2.CreateRunResponse]
    """Request to create a new run"""

    GetRunStatus: grpc.UnaryUnaryMultiCallable[
        flwr.proto.orchestrator_pb2.GetRunStatusRequest,
        flwr.proto.orchestrator_pb2.GetRunStatusResponse]
    """Get the status of a given run"""


class OrchestratorServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def CreateRun(self,
        request: flwr.proto.orchestrator_pb2.CreateRunRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.orchestrator_pb2.CreateRunResponse:
        """Request to create a new run"""
        pass

    @abc.abstractmethod
    def GetRunStatus(self,
        request: flwr.proto.orchestrator_pb2.GetRunStatusRequest,
        context: grpc.ServicerContext,
    ) -> flwr.proto.orchestrator_pb2.GetRunStatusResponse:
        """Get the status of a given run"""
        pass


def add_OrchestratorServicer_to_server(servicer: OrchestratorServicer, server: grpc.Server) -> None: ...
