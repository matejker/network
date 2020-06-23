import pytest
from network.models.barabasi_albert import BarabasiAlbert
from network.models.exceptions import BarabasiAlbertModelIncorrectInput


def test_barabasi_albert():
    edges_basket = [
        [1, 2, 3, 4, 6],
        [0, 2, 3, 4, 5, 8, 9],
        [0, 1, 3, 4, 7],
        [0, 1, 2, 4, 9],
        [0, 1, 2, 3, 5, 6],
        [1, 4, 7],
        [0, 4, 8],
        [2, 5],
        [1, 6],
        [1, 3]
    ]

    test_ba = BarabasiAlbert(10, 2, m0=5, seed=42)

    assert test_ba.edges_basket == edges_basket


def test_barabasi_albert_exceptions():
    # m0 < m
    with pytest.raises(BarabasiAlbertModelIncorrectInput):
        BarabasiAlbert(10, 6, 5)

    # n < m0
    with pytest.raises(BarabasiAlbertModelIncorrectInput):
        BarabasiAlbert(1, 6, 5)
