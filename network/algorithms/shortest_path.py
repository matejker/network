from network import Network
from .exceptions import NotNetworkNode


def dijkstra(network: Network, source: int, target: int):
    """Dijkstra's algorithm for finding the shortest path in the network

    Args:
        network (Network): Network object, both wighted and unweighted
        source (int): source node where the path starts
        target (int): target node where the path ends

    Raises:
        NotNetworkNode: if source is not in the network
        NotNetworkNode: if target is not in the network

    Returns:
        shortest path in the network, starting in source and ending in target
    """
    if source > network.n:
        raise NotNetworkNode(f'Source node {source} is not in the network (N={network.n})')

    if target > network.n:
        raise NotNetworkNode(f'Target node {target} is not in the network (N={network.n})')

    path = []
    if source == target:
        return path
