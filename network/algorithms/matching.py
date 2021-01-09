from collections import deque


from network.network import Network
from network.algorithms.bipartite import is_bipartite, get_bipartite_sets
from network.algorithms.exceptions import NetworkIsNotBipartite


def hopcroft_karp(network: Network):
    """ Hopcroft-Karp

    References:
        .. [1] John E. Hopcroft and Richard M. Karp. (1973),
        "An n^{5 / 2} Algorithm for Maximum Matchings in Bipartite Graphs",
         SIAM Journal of Computing 2.4, pp. 225--231. <https://doi.org/10.1137/0202019>.
    """

    if not is_bipartite(network):
        raise NetworkIsNotBipartite("Network is not bipartite, you can not run Hopcroft-Karp on non bipartite networks")

    # A matching M is maximum iff there is no augmenting path.
    # https://stackoverflow.com/questions/4697228/hopcroft-karp-algorithm-in-python

    def _bfs():
        for v in layer_a:
            if a_matches[v] is None:
                distances[v] = 0
                queue.append(v)
            else:
                distances[v] = float("inf")
        distances[None] = float("inf")
        while queue:
            v = queue.popleft()
            if distances[v] < distances[None]:
                for u in network.edges_basket[v]:
                    if distances[b_matches[u]] is float("Inf"):
                        distances[b_matches[u]] = distances[v] + 1
                        queue.append(b_matches[u])
        return distances[None] is not float("inf")

    def _dfs(v):
        if v is not None:
            for u in network.edges_basket[v]:
                if distances[b_matches[u]] == distances[v] + 1:
                    if _dfs(b_matches[u]):
                        b_matches[u] = v
                        a_matches[v] = u
                        return True
            distances[v] = float("inf")
            return False
        return True

    # Initialize the "global" variables that maintain state during the search.
    layer_a, layer_b = get_bipartite_sets(network)
    a_matches = {v: None for v in layer_a}
    b_matches = {v: None for v in layer_b}
    distances = {}
    queue = deque()

    # Implementation note: this counter is incremented as pairs are matched but
    # it is currently not used elsewhere in the computation.
    num_matched_pairs = 0
    while _bfs():
        for v in layer_a:
            if a_matches[v] is None:
                if _dfs(v):
                    num_matched_pairs += 1

    # Strip the entries matched to `None`.
    a_matches = {k: v for k, v in a_matches.items() if v is not None}
    b_matches = {k: v for k, v in b_matches.items() if v is not None}

    # At this point, the left matches and the right matches are inverses of one
    # another. In other words,
    #
    #     leftmatches == {v, k for k, v in rightmatches.items()}
    #
    # Finally, we combine both the left matches and right matches.
    return a_matches.items(), b_matches.items()
