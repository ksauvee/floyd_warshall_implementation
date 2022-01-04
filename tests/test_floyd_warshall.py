import pytest
from math import inf

from src.graph import Graph


def test_0_edge_graph():
    with pytest.raises(ValueError):
        graph_test = Graph(0, 0, [])
        graph_test.floyd_warshall()


def test_simple_graph():
    graph_test = Graph(2, 1, [[0, 1, 1]])
    dist, prev, have_negative_cycle, logs = graph_test.floyd_warshall()
    assert dist == [[0, 1], [inf, 0]] \
           and prev == [[0, 0], [1, 1]] \
           and not have_negative_cycle


def test_much_harder_graph():
    graph_test = Graph(4, 7, [[0, 1, 2], [0, 3, 6], [1, 2, -2], [2, 1, 5], [2, 3, 5], [3, 0, -4], [3, 1, -1]])
    dist, prev, have_negative_cycle, logs = graph_test.floyd_warshall()
    assert dist == [[0, 2, 0, 5], [-1, 0, -2, 3], [1, 3, 0, 5], [-4, -2, -4, 0]] \
           and prev == [[0, 0, 1, 2], [3, 1, 1, 2], [3, 0, 2, 2], [3, 0, 1, 3]] \
           and not have_negative_cycle


def test_with_negative_path_graph():
    graph_test = Graph(3, 5, [[0, 1, -2], [0, 2, 1], [1, 1, -1], [1, 0, 1], [2, 1, 2]])
    dist, prev, have_negative_cycle, logs = graph_test.floyd_warshall()
    print(dist)
    assert dist == [[-inf, -inf, -inf], [-inf, -inf, -inf], [-inf, -inf, -inf]] \
           and prev == [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]] \
           and have_negative_cycle


def test_with_small_negative_path_graph():
    graph_test = Graph(3, 3, [[0, 1, -2], [0, 2, 1], [1, 1, -1]])
    dist, prev, have_negative_cycle, logs = graph_test.floyd_warshall()
    print(dist)
    assert dist == [[0, -inf, 1], [inf, -inf, inf], [inf, inf, 0]] \
           and prev == [[0, -1, 0], [1, -1, 1], [2, 2, 2]] \
           and have_negative_cycle


def test_with_negative_path_much_harder_graph():
    graph_test = Graph(4, 7, [[0, 1, 2], [0, 3, 6], [2, 2, -1], [2, 1, 5], [2, 3, 5], [3, 0, -4], [3, 1, -1]])
    dist, prev, have_negative_cycle, logs = graph_test.floyd_warshall()
    print(dist)
    assert dist == [[0, 2, inf, 6], [inf, 0, inf, inf], [-inf, -inf, -inf, -inf], [-4, -2, inf, 0]] \
           and prev == [[0, 0, 0, 0], [1, 1, 1, 1], [-1, -1, -1, -1], [3, 0, 3, 3]] \
           and have_negative_cycle
