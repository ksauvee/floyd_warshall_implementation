import pytest
from math import inf

from src.graph import Graph


def test_0_edge_graph():
    with pytest.raises(ValueError):
        graph_test = Graph(0, 0, [])
        graph_test.floyd_warshall()


def test_simple_graph():
    graph_test = Graph(2, 1, [[0, 1, 1]])
    dist, prev = graph_test.floyd_warshall()
    assert dist == [[0, 1], [inf, 0]] and prev == [[0, 0], [1, 1]]


def test_much_harder_graph():
    graph_test = Graph(4, 7, [[0, 1, 2], [0, 3, 6], [1, 2, -2], [2, 1, 5], [2, 3, 5], [3, 0, -4], [3, 1, -1]])
    dist, prev = graph_test.floyd_warshall()
    assert dist == [[0, 2, 0, 5], [-1, 0, -2, 3], [1, 3, 0, 5], [-4, -2, -4, 0]] \
           and prev == [[0, 0, 1, 2], [3, 1, 1, 2], [3, 0, 2, 2], [3, 0, 1, 3]]
