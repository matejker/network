from network.network import NetworkException


class NotEulerianNetwork(NetworkException):
    pass


class NotNetworkNode(NetworkException):
    pass


class SourceTargetNotConnected(NetworkException):
    pass


class NetworkIsNotBipartite(NetworkException):
    pass
