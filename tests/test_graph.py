import pytest

from src.graph import Graph


def test_negative_number_of_nodes():
    with pytest.raises(ValueError):
        Graph(-3)


def test_graph_without_node():
    graph_test = Graph(0)
    assert len(graph_test.get_adj_matrix()) == 0

    for node_neighbors in graph_test.get_adj_matrix():
        assert len(node_neighbors) == 0


def test_graph_with_one_node():
    graph_test = Graph(1)
    assert len(graph_test.get_adj_matrix()) == 1

    for node_neighbors in graph_test.get_adj_matrix():
        assert len(node_neighbors) == 1


def test_graph_with_54_nodes():
    graph_test = Graph(54)
    assert len(graph_test.get_adj_matrix()) == 54

    for node_neighbors in graph_test.get_adj_matrix():
        assert len(node_neighbors) == 54
