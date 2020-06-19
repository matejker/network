from network.models.exceptions import *
from network.network import Network
from network.models.tools import random_choice
from itertools import combinations, permutations
import numpy as np


class CompleteNetwork(Network):
    def __init__(self, n, directed=False, **kwargs):
        """Compleate graph, denoted as K_n, where every node is connected to every node

        Args:
            n (int): number of nodes
            directed (boolean): if it is a directed or undirected network
            **kwargs (dict): kwargs
        """
        if directed:
            edges = permutations(list(range(n)), 2)
        else:
            edges = combinations(list(range(n)), 2)

        super().__init__(n, list(edges), directed=directed, **kwargs)
