import pytest
from network import Network
from network.algorithms import hierholzer
from network.algorithms.exceptions import NotEulerianNetwork


def test_hierholzer():
    four_cycle_network = Network(4, [(0, 1), (1, 2), (2, 3), (3, 0)])  # a 4-circle

    assert hierholzer(four_cycle_network) == [0, 1, 2, 3, 0]
    assert hierholzer(four_cycle_network, 2) == [2, 1, 0, 3, 2]

    two_roof_house = Network(6, [(0, 1), (0, 2), (0, 3), (0, 5), (1, 2), (1, 3), (1, 5), (2, 3), (2, 4), (3, 4)])

    assert hierholzer(two_roof_house) == [0, 1, 2, 0, 3, 2, 4, 3, 1, 5, 0]


def test_hierholzer_non_eulerian_network():
    non_eulerian_network = Network(4, [(0, 1), (1, 2), (2, 3)])

    with pytest.raises(NotEulerianNetwork):
        hierholzer(non_eulerian_network)
