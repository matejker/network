from heapq import heappop, heapify

from network import Network
from .exceptions import NotNetworkNode, SourceTargetNotConnected
from network.tools import weighted_edges_dict

__all__ = ["dijkstra"]


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
        raise NotNetworkNode(f"Source node {source} is not in the network (N={network.n})")

    if target > network.n:
        raise NotNetworkNode(f"Target node {target} is not in the network (N={network.n})")

    path = []
    if source == target:
        return path

    # Get weighted edges, when network is unweighted then every edge has weight 1, having (v, u, w) format
    weighted_edges = weighted_edges_dict(network)

    dist = {n: float("inf") for n in range(network.n)}
    prev = {n: None for n in range(network.n)}
    queue = set(range(network.n))

    def make_heap(distance, q):
        return [(d, n) for n, d in distance.items() if n in q]

    dist[source] = 0

    heap = make_heap(dist, queue)
    heapify(heap)

    while len(queue) > 0:
        d, v = heappop(heap)
        queue.remove(v)

        for u in network.edges_basket[v]:
            alt = d + weighted_edges[v, u]
            if alt < dist[u]:
                dist[u] = alt
                prev[u] = v
        heap = make_heap(dist, queue)
        heapify(heap)

    last_node = target
    m = len(weighted_edges)

    # Iterate till the source is not in the path or we have visited all edges
    while source not in path and m > 0:
        path.append(last_node)
        last_node = prev[last_node]
        m -= 1

    if m == 0:
        raise SourceTargetNotConnected(f"Source {source} is not connected with {target}")

    return path, dist[target]
