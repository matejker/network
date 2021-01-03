from network.network import Network
from network.algorithms.exceptions import NotNetworkNode

def dfs(network: Network, source: int):
    """ Depth First Search

    Args:
        network (Network): network object
        source(int): node where starts (and ends) the path
    Raises:
        NotNetworkNode: if source is not in the network

    Returns:
        list of nodes that form a sorted spanning tree

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

    def _dfs(_visited, _node):
        _visited.append(_node)

        for neighbour in sorted(network.edges_basket[_node]):
            if neighbour not in _visited:
                _visited = _dfs(_visited, neighbour)

        return _visited

    return _dfs([], source)




