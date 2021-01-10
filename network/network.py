import numpy as np

__all__ = ["NetworkException", "Network"]


class NetworkException(Exception):
    pass


class Network:
    """Generic framework for network objects.

    Object attributes:
        n (integer): number of nodes
        edges (list): network edges as a list of tuples
        edges_basket (list): node neighbors as list of lists
        degrees_list (list): degrees of each node
        mean_degree (float): average node degree
        k_min (integer): min degree
        k_max (integer): max degree
        degree_distribution (list): degree distribution (or histogram over node degrees)
        degree_bin_edges (list): histogram bin_edges of the degree_distribution

    To use:
        >>> network = Network(3, [(0, 1), (2, 1)])
        >>> network.edges_basket
        [[1], [0, 2], [1]]
        >>> network.degrees_list
        [1, 2, 1]
        >>> network.k_max
        2
        >>> network.k_min
        1
        >>> network.mean_degree
        1.3333333333333333
        >>> network.n
        3

    References:
        .. [1] Newman, M. E. J. (2010),
        Networks: an introduction,
        Oxford University Press, Oxford; New York

        .. [2] Reinhard Diestel,
        Graph Theory,
        Springer, Volume 173 of Graduate texts in mathematics, ISSN 0072-5285
    """

    @staticmethod
    def get_edge_basket(n, edges, edge_basket=None, directed=False, reverse=False, weighted=False):
        """Converts list of edges (tuples) into list of node's neighbors

        Args:
            n (int): number of nodes
            edges (list): list of edges (tuples)
            edge_basket (list): list of node's neighbors
            directed (boolean): if the network is directed
            reverse (boolean): if True will reverse the edges (e.g. (0, 1) to (1, 0))
            weighted (boolean): if the network is weighted

        Returns:
            edge_basket (list): list of node's neighbors
        """
        edges_basket = edge_basket or [[] for _ in range(n)]

        # Removing weights for weighted network
        edges = [(v, u) for v, u, w in edges] if weighted else edges

        for v, u in edges:
            if reverse and directed:
                v, u = u, v

            edges_basket[v].append(u)
            if not directed:
                edges_basket[u].append(v)

        return edges_basket

    def __init__(self, n, edges, edge_basket=None, directed=False, weighted=False):
        self.n = n
        self.directed = directed
        self.weighted = weighted

        # Sanitise weighted edges with no weights, default weight is 1
        if weighted:
            self.edges = [e for e in edges if len(e) == 3]
            self.edges.extend([(e[0], e[1], 1) for e in edges if len(e) == 2])
        else:
            self.edges = edges

        self.edges_basket = edge_basket or self.get_edge_basket(n, self.edges, directed=directed, weighted=weighted)

        self.degrees_list = [len(_) for _ in self.edges_basket]

        self.mean_degree = np.mean(self.degrees_list)  # TODO: think about powerlaw
        self.k_min = min(self.degrees_list) if n > 0 else 0
        self.k_max = max(self.degrees_list) if n > 0 else 0

    def get_degree_distribution(self, log=False, density=True):  # TODO: think about powerlaw
        """Determines the network's degree distribution on both linear or logarithmic scale

        Args:
            log (boolean): Using the logarithmic scale
            density (boolean): Returning distribution over the cumulative values (histogram)

        Returns:
            degree_distribution (list): degree distribution (or histogram over node degrees)
            degree_bin_edges (list): histogram bin_edges of the degree_distribution

        Usage:
            >>> network = Network(3, [(0, 1), (2, 1)])
            >>> network.get_degree_distribution()
            (array([0.66666667, 0.33333333]), array([1, 2]))
            >>> network.degree_distribution
            array([0.66666667, 0.33333333])

        Warning:
            degree_distribution and degree_bin_edges are not in Network.__init__, they are intentionally determined
            after running Network.get_degree_distribution()!

        """
        m_log = np.round(np.log10(self.k_max), 0)

        bins = np.logspace(np.log10(self.k_min), np.log10(10. ** m_log), m_log * 5.) if log \
            else np.arange(1, self.k_max + 2)

        degree_distribution, bin_edges = np.histogram(self.degrees_list, bins=bins, density=density)

        self.degree_distribution = degree_distribution
        self.degree_bin_edges = bin_edges[:-1]

        return degree_distribution, bin_edges[:-1]

    def directed_degrees(self):
        """However, degrees_list holds info about out-degree values (or both for undirected networks), this function
        return out-degree and in-degree for each node

        Returns:
            (tuple): a tuple of two lists denoting out-degree and in-degree

        Warning:
            in_degrees_list, in_k_min and in_k_max are not in Network.__init__, they are intentionally determined
            after running Network.directed_degrees()!
        """
        out_degree = self.degrees_list
        in_coming_edges_basket = self.get_edge_basket(self.n, self.edges, reverse=True, directed=True)

        in_degree = [len(_) for _ in in_coming_edges_basket]
        self.in_degrees_list = in_degree
        self.in_k_min = min(in_degree) if self.n > 0 else 0
        self.in_k_max = max(in_degree) if self.n > 0 else 0

        return out_degree, in_degree
