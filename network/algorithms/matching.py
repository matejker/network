from network.network import Network
from network.algorithms.search import bfs, dfs
from network.algorithms.bipartite import is_bipartite, get_bipartite_sets
from network.algorithms.exceptions import NetworkIsNotBipartite


def hopcroft_karp(network: Network):
    """ Hopcroft-Karp """

    if not is_bipartite(network):
        raise NetworkIsNotBipartite("Network is not bipartite, you can not run Hopcroft-Karp on non bipartite networks")

    layer_a, layer_b = get_bipartite_sets(network)

    # A matching M is maximum iff there is no augmenting path.
