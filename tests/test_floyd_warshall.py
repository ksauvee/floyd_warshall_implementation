import pytest
from math import inf

from src.graph import Graph

def test_0_edge_graph():
    with pytest.raises(ValueError):
        graph_test = Graph(0, 0, [])
        graph_test.floyd_warshall()


def test_simple_graph():
    graph_test = Graph(2, 1, [[0,1,1]])
    dist, pred = graph_test.floyd_warshall()
    assert dist == [[inf, 1],[inf, inf]] and pred == [[0,0],[1,1]]

def test_very_HARD_graph():
    graph_test = Graph(2, 1, [[0,1,1]])
    dist, pred = graph_test.floyd_warshall()
    assert dist == [[inf, 1],[inf, inf]] and pred == [[0,0],[1,1]]
