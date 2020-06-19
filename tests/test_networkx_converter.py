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


def test_networkx2network_weighted():
    edges = [(1, 0, 2), (3, 0, 5), (2, 1, 2)]
    weighted_graph = nx.Graph()
    weighted_graph.add_weighted_edges_from(edges)

    test_network = networkx2network(weighted_graph)

    assert test_network.edges == [(1, 0, 2), (1, 2, 2), (0, 3, 5)]


def test_networkx2network_directed():
    edges = [(0, 1), (1, 0), (1, 2)]
    di_graph = nx.DiGraph()
    di_graph.add_edges_from(edges)

    test_network = networkx2network(di_graph)

    assert test_network.edges == edges


def test_networkx2network_weighted_directed():
    edges = [(1, 0, 2), (0, 3, 1), (3, 0, 5), (2, 1, 2)]
    weighted_di_graph = nx.DiGraph()
    weighted_di_graph.add_weighted_edges_from(edges)

    test_network = networkx2network(weighted_di_graph)

    assert test_network.edges == [(1, 0, 2), (0, 3, 1), (3, 0, 5), (2, 1, 2)]


def test_network2networkx():
    edges = [(0, 4), (0, 2), (1, 2), (2, 3)]
    network = Network(5, edges)

    test_graph = network2networkx(network)

    assert len(test_graph.nodes) == 5
    assert list(test_graph.edges) == edges


def test_network2networkx_directed():
    edges = [(0, 1), (1, 0), (1, 2)]
    network = Network(5, edges, directed=True)

    test_graph = network2networkx(network)

    assert len(test_graph.nodes) == 5
    assert list(test_graph.edges) == edges


def test_network2networkx_weighted():
    edges = [(1, 0, 2), (3, 0, 5), (2, 1, 2)]
    network = Network(5, edges, weighted=True)

    test_graph = network2networkx(network)

    assert len(test_graph.nodes) == 5
    assert list(test_graph.edges(data=True)) == [(0, 1, {'weight': 2}), (0, 3, {'weight': 5}), (1, 2, {'weight': 2})]


def test_network2networkx_weighted_directed():
    edges = [(1, 0, 2), (0, 3, 1), (3, 0, 5), (2, 1, 2)]
    network = Network(5, edges, directed=True, weighted=True)

    test_graph = network2networkx(network)

    assert len(test_graph.nodes) == 5
    assert list(test_graph.edges(data=True)) == [(0, 3, {'weight': 1}), (1, 0, {'weight': 2}),
                                                 (2, 1, {'weight': 2}), (3, 0, {'weight': 5})]
