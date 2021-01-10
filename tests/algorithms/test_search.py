from network import Network
from network.algorithms import bfs, dfs

star_graph = Network(6, [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)])
regular_graph = Network(6, [(0, 1), (0, 3), (2, 5), (3, 4), (4, 1), (5, 1), (4, 5)])
binary_tree = Network(7, [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)])


def test_bfs():
    assert bfs(star_graph, source=0) == list(range(star_graph.n))
    assert bfs(star_graph, source=1) == [1, 0, 2, 3, 4, 5]

    assert bfs(regular_graph, source=0) == [0, 1, 3, 4, 5, 2]
    assert bfs(regular_graph, source=1) == [1, 0, 4, 5, 3, 2]
    assert bfs(regular_graph, source=2) == [2, 5, 1, 4, 0, 3]

    assert bfs(binary_tree, source=0) == list(range(binary_tree.n))


def test_dfs():
    assert dfs(star_graph, source=0) == list(range(star_graph.n))

    assert dfs(regular_graph, source=0) == [0, 1, 4, 3, 5, 2]
    assert dfs(regular_graph, source=1) == [1, 0, 3, 4, 5, 2]
    assert dfs(regular_graph, source=5) == [5, 1, 0, 3, 4, 2]

    assert dfs(binary_tree, source=0) == [0, 1, 3, 4, 2, 5, 6]
