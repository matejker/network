from network.network import Network
from network.algorithms.exceptions import NotEulerianNetwork
from copy import deepcopy

# A connected graph has an Euler cycle if and only if every vertex has even degree.
# ~ Euler


def hierholzer(network: Network, source=0):
    """ TODO:

    Args:
        network (Network):
        source=0 (int): node where starts (and ends) the path

    Raises:
        NotEulerianNetwork: if exists at least one node with odd degree

    Returns:
        list of nodes that form a path visiting all edges
    """

    path = []
    temp_path = []
    degrees_list = deepcopy(network.degrees_list)
    edges_basket = deepcopy(network.edges_basket)

    if network.n == 0:
        return path

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
            degrees_list[next_node] -= 1

            edges_basket[temp_node].pop()
            i = edges_basket[next_node].index(temp_node)
            del edges_basket[next_node][i]

            temp_node = next_node
        else:
            path.append(temp_node)
            temp_node = temp_path[-1]
            temp_path.pop()

    return path
