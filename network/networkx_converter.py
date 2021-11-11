import networkx as nx

from .network import Network

__all__ = ["network2networkx", "networkx2network"]


def network2networkx(network):
    """Converts Network into networkx.Graph()

    Args:
       network (Network): a Network object

    Returns:
        A NetworkX Graph object.

    """
    edges = network.edges

    graph = nx.DiGraph() if network.directed else nx.Graph()
    graph.add_nodes_from(list(range(network.n)))

    if network.weighted:
        # edges are in format (v, u, w)
        graph.add_weighted_edges_from(edges)
    else:
        graph.add_edges_from(edges)

    return graph


def networkx2network(graph, weight_key='weight'):
    """Converts networkx.Graph() into Network

    Args:
       graph (Graph): a Network object
       weight_key (string): weight key in the graph (usually weight, length)

    Returns:
        A Network object.

    """
    nodes = list(graph.nodes())
    nodes.sort()
    n = len(nodes)

    directed = graph.is_directed()
    weighted_edges = [
        (nodes.index(v), nodes.index(u), d[weight_key]) for (v, u, d) in graph.edges(data=True) if weight_key in d
    ]
    weighted = len(weighted_edges) > 0

    if weighted:
        unweighted_edges = [
            (nodes.index(v), nodes.index(u), 1) for (v, u, d) in graph.edges(data=True) if weight_key not in d
        ]
        edges = weighted_edges + unweighted_edges
    else:
        edges = [(nodes.index(v), nodes.index(u)) for v, u in graph.edges()]

    return Network(n, edges, directed=directed, weighted=weighted)
