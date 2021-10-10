import pytest

from src.floyd_warshall_graph import floyd_warshall_graph


def test_negative_nodes():
    with pytest.raises(ValueError):
        floyd_warshall_graph(-3)


def test_graph_with_one_node():
    graph = floyd_warshall_graph(1)
    assert len(graph.get_adj_matrix()) == 1
