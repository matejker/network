import networkx as nx
from network import Network, networkx2network, network2networkx


def test_networkx2network():
    edges = [(0, 4), (0, 2), (2, 1), (2, 3)]
    graph = nx.Graph()
    graph.add_edges_from(edges)

    test_network = networkx2network(graph)

    assert test_network.edges == edges
    assert test_network.n == 5
    assert test_network.edges_basket == [[4, 2], [2], [0, 1, 3], [2], [0]]


def test_network2networkx():
    edges = [(0, 4), (0, 2), (2, 1), (2, 3)]
    network = Network(5, edges)

    test_graph = network2networkx(network)

    assert len(test_graph.nodes) == 5
    assert list(test_graph.edges) == edges
