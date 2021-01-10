import pytest

from network import Network
from network.algorithms import hopcroft_karp, NetworkIsNotBipartite


def test_hopcroft_karp():
    bipartite_graph = Network(8, [(0, 4), (0, 5), (1, 4), (1, 7), (2, 6), (3, 5), (3, 6)])
    not_bipartite_graph = Network(8, [(0, 4), (0, 5), (1, 4), (1, 7), (2, 6), (3, 5), (3, 6), (7, 6)])
    even_cycle = Network(6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)])

    assert hopcroft_karp(bipartite_graph) == [(0, 4), (1, 7), (2, 6), (3, 5)]
    assert hopcroft_karp(bipartite_graph, False) == ([(0, 4), (1, 7), (2, 6), (3, 5)], [(4, 0), (5, 3), (6, 2), (7, 1)])

    assert hopcroft_karp(even_cycle) == [(0, 1), (2, 3), (4, 5)]
    with pytest.raises(NetworkIsNotBipartite):
        hopcroft_karp(not_bipartite_graph)
