from collections import deque

from network.network import Network
from network.algorithms.bipartite import is_bipartite, get_bipartite_sets
from network.algorithms.exceptions import NetworkIsNotBipartite

__all__ = ["hopcroft_karp"]

INFINITY = float("inf")


def hopcroft_karp(network: Network, one_layer=True):
    """ Hopcroft-Karp - maximum cardinality matching on bipartite network. The algorithm was originally published by
    Hopcroft and Karp in 1973 [1], but in this case we implemented solution from Wikipedia [2].

    References:
        .. [1] John E. Hopcroft and Richard M. Karp. (1973),
        "An n^{5 / 2} Algorithm for Maximum Matchings in Bipartite Graphs",
         SIAM Journal of Computing 2.4, pp. 225--231. <https://doi.org/10.1137/0202019>.
        .. [2] Wikimedia, Hopcroft–Karp algorithm,
        https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm#Pseudocode
        .. [3] Sofiat Olaosebikan (2015),  Python Implementation of HopcroftKarp's Algorithm
        https://github.com/sofiatolaosebikan/hopcroftkarp
    """

    if not is_bipartite(network):
        raise NetworkIsNotBipartite("Network is not bipartite, you can not run Hopcroft-Karp on non bipartite networks")

    # A matching M is maximum iff there is no augmenting path.

    layer_a, layer_b = get_bipartite_sets(network)
    a_matches = {v: None for v in layer_a}
    b_matches = {v: None for v in layer_b}
    dist = {}
    queue = deque()

    def _bfs():
        for v in layer_a:
            if a_matches[v] is None:
                dist[v] = 0
                queue.append(v)
            else:
                dist[v] = INFINITY

        dist[None] = INFINITY

        while queue:
            v = queue.popleft()
            if dist[v] < dist[None]:
                for u in network.edges_basket[v]:
                    if dist[b_matches[u]] is INFINITY:
                        dist[b_matches[u]] = dist[v] + 1
                        queue.append(b_matches[u])
        return dist[None] is not INFINITY

    def _dfs(v):
        if v is not None:
            for u in network.edges_basket[v]:
                if dist[b_matches[u]] == dist[v] + 1:
                    if _dfs(b_matches[u]):
                        b_matches[u] = v
                        a_matches[v] = u
                        return True
            dist[v] = INFINITY
            return False
        return True

    while _bfs():
        for v in layer_a:
            if a_matches[v] is None:
                _dfs(v)

    a_matches = [(k, v) for k, v in a_matches.items() if v is not None]
    b_matches = [(k, v) for k, v in b_matches.items() if v is not None]

    return a_matches if one_layer else (a_matches, b_matches)
