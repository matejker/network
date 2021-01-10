from network.network import Network

__all__ = ["get_bipartite_sets", "is_bipartite"]


# A bipartite graph is 2-colorable graph.
# A (simple) graph is bipartite if and only if it contains no odd cycles.

def get_bipartite_sets(network: Network):
    """ Finds (possible) edge sets of a bipartite graph

    Args:
        network (Network): network object

    Returns:
         edge sets, otherwise False

    None:
        If graph is not connected the sets are ambiguous.
    """
    def opposite_color(color: int):
        return 1 - color

    color_sets = [set(), set()]
    colors = [-1] * network.n

    for node in range(network.n):
        if colors[node] != -1 or len(network.edges_basket[node]) == 0:
            continue
        color_sets[0].add(node)
        colors[node] = 0
        queue = [node]
        while queue:
            n = queue.pop()
            neighbour_color = opposite_color(colors[n])
            for neighbour in network.edges_basket[n]:
                if colors[neighbour] == -1:
                    colors[neighbour] = neighbour_color
                    color_sets[neighbour_color].add(neighbour)
                    queue.append(neighbour)
                if colors[neighbour] == colors[n]:
                    return False
    return color_sets


def is_bipartite(network: Network):
    """ Checks if network is bipartite

    Args:
        network (Network): network object

    Returns:
        True if bipartite, otherwise False
    """
    return get_bipartite_sets(network) != False  # noqa
