from network.models.exceptions import BarabasiAlbertModelIncorrectInput
from network.network import Network
from network.tools import random_choice
from itertools import combinations
import numpy as np


class BarabasiAlbert(Network):
    """Preferential attachment Barabasi-Albert model

    To use:
        >>> ba_model = BarabasiAlbert(5, 2)
        >>> ba_model.edges
        [(0, 1), (2, 1), (2, 0), (3, 2), (3, 0), (4, 3), (4, 2)]
        >>> ba_model.edges_basket
        [[1, 2, 3], [0, 2], [1, 0, 3, 4], [2, 0, 4], [3, 2]]

    Object attributes:
        See Network object
    """

    @classmethod
    def model(cls, n, m, m0=None, seed=None):
        """Barabasi-Albert model [2]

        Args:
            n (integer): number of network nodes
            m (integer): number of new edges from newly added node
            m0=None (integer): size of initial connected network
            seed=None (integer): numpy.random.seed (integer between 0 and 2**32 - 1 inclusive) [1]

        Returns:
            A Network object.

        Raises:
            BarabasiAlbertModelIncorrectInput: If inserted m <= m0
            BarabasiAlbertModelIncorrectInput: If inserted n => m0

        References:
            .. [1] The SciPy community,
            Numpy.random.seed,
            https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.seed.html

            .. [2] Newman, M. E. J. (2010),
            Networks: an introduction,
            Oxford University Press, Oxford; New York
        """
        if seed:
            np.random.seed(seed)

        m0 = m0 or m

        if m0 < m:
            raise BarabasiAlbertModelIncorrectInput(f'Inserted values are not correct, m <= m0, m={m} and 0={m0}')

        if n < m0:
            raise BarabasiAlbertModelIncorrectInput(f'Inserted values are not correct, n => m0, m0={m0} and n={n}')

        # Initial complete graph
        edges = list(combinations(list(range(m0)), 2))
        nodes_basket = list(range(m0)) * (m0 - 1)

        r = m0
        while r < n:
            connections = random_choice(nodes_basket, m)
            rm = [r] * m

            new_edges = list(zip(rm, connections))

            edges.extend(new_edges)
            nodes_basket.extend(rm + connections)

            r += 1

        return edges

    def __init__(self, n, m, m0=None, seed=None, **kwargs):
        edges = self.model(n, m, m0, seed)
        super().__init__(n, edges, **kwargs)
