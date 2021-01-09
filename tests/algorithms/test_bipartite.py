from network import Network
from network.algorithms import is_bipartite, get_bipartite_sets

bipartite_graph = Network(8, [(0, 4), (0, 5), (1, 4), (1, 7), (2, 6), (3, 5), (3, 6)])
not_bipartite_graph = Network(8, [(0, 4), (0, 5), (1, 4), (1, 7), (2, 6), (3, 5), (3, 6), (7, 6)])
even_cycle = Network(6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)])
odd_cycle = Network(5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])


def test_get_bipartite_sets():
    assert get_bipartite_sets(bipartite_graph) == [{0, 1, 2, 3}, {4, 5, 6, 7}]
    assert get_bipartite_sets(not_bipartite_graph) is False
    assert get_bipartite_sets(even_cycle) == [{0, 2, 4}, {1, 3, 5}]
    assert get_bipartite_sets(odd_cycle) is False


def test_is_bipartite():
    assert is_bipartite(bipartite_graph)
    assert is_bipartite(not_bipartite_graph) is False
    assert is_bipartite(even_cycle)
    assert is_bipartite(odd_cycle) is False
