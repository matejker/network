from network.network import Network
from network.algorithms.exceptions import NotEulerianNetwork
from copy import deepcopy

# A connected graph has an Euler cycle if and only if every vertex has even degree.
# ~ Euler


def hierholzer(network: Network, source=0):
    """Hierholzer's algorithm for finding an Euler cycle

    Args:
        network (Network):
        source=0 (int): node where starts (and ends) the path

    Raises:
        NotEulerianNetwork: if exists at least one node with odd degree

    Returns:
        list of nodes that form a path visiting all edges

    References:
        .. [1] sanjeev2552, heruslu, Code_Mech,
        Geeks For Geeks, A computer science portal for geeks
        https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/

        .. [2] Reinhard Diestel,
        Graph Theory,
        Springer, Volume 173 of Graduate texts in mathematics, ISSN 0072-5285
    """

    path = []
    temp_path = []
    degrees_list = deepcopy(network.degrees_list)
    edges_basket = deepcopy(network.edges_basket)
    if network.n == 0:
        return path

    if network.directed:
        out_degree, in_degree = network.directed_degrees()
        odd_degree_nodes = [{'node': n, 'out_degree': d, 'in_degree': in_degree[n]} for n, d in enumerate(out_degree) if d != in_degree[n]]  # noqa
    else:
        odd_degree_nodes = [{'node': n, 'degree': d} for n, d in enumerate(network.degrees_list) if d % 2 == 1]


    if len(odd_degree_nodes) > 0:
        raise NotEulerianNetwork(f'Network is not Eulerian, not all nodes are even degree: {odd_degree_nodes}')

    temp_path.append(source)
    temp_node = source

    while len(temp_path):
        if degrees_list[temp_node]:
            temp_path.append(temp_node)
            next_node = edges_basket[temp_node][-1]

            degrees_list[temp_node] -= 1
            edges_basket[temp_node].pop()

            if not network.directed:
                degrees_list[next_node] -= 1
                i = edges_basket[next_node].index(temp_node)
                del edges_basket[next_node][i]

            temp_node = next_node
        else:
            path.append(temp_node)
            temp_node = temp_path[-1]
            temp_path.pop()

    # If the network is directed we will revert the path
    if network.directed:
        return path[::-1]

    return path
