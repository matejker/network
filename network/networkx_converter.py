import networkx as nx
from network import Network


def network2networkx(network):
    """Converts Network into networkx.Graph()

    Args:
       network (Network): a Network object

    Returns:
        A NetworkX Graph object.

    """
    edges = network.edges

    g = nx.Graph()
    g.add_edges_from(edges)

    return g


def networkx2network(graph):
    """Converts networkx.Graph() into Network

    Args:
       graph (Graph): a Network object

    Returns:
        A Network object.

    """
    n = len(graph.nodes())
    edges = list(graph.edges())

    # TODO: in Graph nodes do not have be integers mapping from 0 to n
    # TODO: add mapping for edges and nodes to 0 - n

    return Network(n, edges)
