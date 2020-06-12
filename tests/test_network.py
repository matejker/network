import numpy as np
from network import Network


def test_network_class():
    n = 10
    edges = [
        (0, 1), (2, 0), (2, 1), (3, 2), (3, 0), (4, 0), (4, 3), (5, 2),
        (5, 1), (6, 3), (6, 4), (7, 0), (7, 5), (8, 0), (8, 1), (9, 4), (9, 0)
    ]

    test_network = Network(n, edges)

    expected_degrees_list = [7, 4, 4, 4, 4, 3, 2, 2, 2, 2]
    expected_degree_distribution = np.round(np.array([0., 0.4, 0.1, 0.4, 0., 0., 0.1], dtype=np.float64), 1)
    expected_degree_bin_edges = np.array([1, 2, 3, 4, 5, 6, 7])

    expected_edges_basket = [
        [1, 2, 3, 4, 7, 8, 9],
        [0, 2, 5, 8],
        [0, 1, 3, 5],
        [2, 0, 4, 6],
        [0, 3, 6, 9],
        [2, 1, 7],
        [3, 4],
        [0, 5],
        [0, 1],
        [4, 0]
    ]
    expected_mean_degree = 3.4

    test_network.get_degree_distribution()

    assert test_network.degrees_list == expected_degrees_list
    assert (np.round(test_network.degree_distribution, 4) == expected_degree_distribution).all()
    assert (test_network.degree_bin_edges == expected_degree_bin_edges).all()
    assert test_network.edges_basket == expected_edges_basket
    assert test_network.mean_degree == expected_mean_degree
