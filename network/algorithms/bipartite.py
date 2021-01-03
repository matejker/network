from network.network import Network

# A bipartite graph is 2-colorable graph.
# A (simple) graph is bipartite if and only if it contains no odd cycles.


def get_bipartite_sets(network: Network):
    """ Finds (possible) edge sets of a bipartite graph

    Args:
        network (Network): network object

    Returns:
         edge sets, otherwise False
    """
    def opposite_color(color: int):
        return (color + 1) % 2

    color_sets = [set(), set()]
    colors = [-1] * network.n

    for n in range(network.n):
        # Not yet colored
        if colors[n] == -1:
            colors[n] = 1 if set(network.edges_basket[n]) & color_sets[1] else 0
            color_sets[0].add(n)

        neighbour_color = opposite_color(colors[n])

        for neighbour in network.edges_basket[n]:
            colors[neighbour] = neighbour_color
            color_sets[neighbour_color].add(neighbour)

        if color_sets[0] & color_sets[1]:
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
