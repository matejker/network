from collections import deque

from network.network import Network
from network.algorithms.exceptions import NotNetworkNode

__all__ = ["dfs", "bfs"]

# Basic idea: https://xkcd.com/2407


def dfs(network: Network, source: int):
    """ Depth First Search

    Args:
        network (Network): network object
        source(int): node where starts (and ends) the path
    Raises:
        NotNetworkNode: if source is not in the network

    Returns:
        list of nodes that form a sorted (Depth First Search) spanning tree

    References:
        .. [1] Geeks For Geeks, A computer science portal for geeks,
        Depth First Search or DFS for a Graph
        https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

        .. [2] Reinhard Diestel,
        Graph Theory,
        Springer, Volume 173 of Graduate texts in mathematics, ISSN 0072-5285
    """

    if source > network.n:
        raise NotNetworkNode(f"Source node {source} is not in the network (N={network.n})")

    def _dfs(visited, node):
        visited.append(node)

        for neighbour in sorted(network.edges_basket[node]):
            if neighbour not in visited:
                visited = _dfs(visited, neighbour)

        return visited

    return _dfs([], source)


def bfs(network: Network, source: int):
    """ Breadth First Search

    Args:
        network (Network): network object
        source(int): node where starts (and ends) the path
    Raises:
        NotNetworkNode: if source is not in the network

    Returns:
        list of nodes that form a sorted (Breadth First Search) spanning tree

    References:
        .. [1] Geeks For Geeks, A computer science portal for geeks,
        Breadth First Search or BFS for a Graph
        https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

        .. [2] Reinhard Diestel,
        Graph Theory,
        Springer, Volume 173 of Graduate texts in mathematics, ISSN 0072-5285
    """
    if source > network.n:
        raise NotNetworkNode(f"Source node {source} is not in the network (N={network.n})")

    visited = []
    queue = deque([source])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)

        for neighbour in sorted(network.edges_basket[node]):
            if neighbour not in visited:
                queue.append(neighbour)

    return visited
