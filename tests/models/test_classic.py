from network.models.classic import CompleteNetwork


def test_complete_network():
    test_network = CompleteNetwork(4)
    assert test_network.edges == [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

    test_zero_network = CompleteNetwork(0)
    assert test_zero_network.edges == []


def test_complete_network_directed():
    test_network_directed = CompleteNetwork(3, directed=True)
    assert test_network_directed.edges == [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
