import pytest
from math import inf

from src.graph import Graph


def test_negative_number_of_nodes():
    with pytest.raises(ValueError):
        Graph(-3, 2, [[0, 0, 0], [0, 9, 0]])


def test_negative_number_of_edges():
    with pytest.raises(ValueError):
        Graph(2, -4, [[]])


def test_edges_list_length_should_equals_nb_edges():
    with pytest.raises(ValueError):
        Graph(2, 2, [[0, 0, 0]])


def test_graph_without_node():
    graph_test = Graph(0, 0, [])
    assert graph_test.get_nb_nodes() == 0
    assert graph_test.get_nb_edges() == 0
    assert len(graph_test.get_adj_matrix()) == 0

    for node_neighbors in graph_test.get_adj_matrix():
        assert len(node_neighbors) == 0


def test_graph_with_one_node():
    graph_test = Graph(1, 0, [])
    assert graph_test.get_nb_nodes() == 1
    assert graph_test.get_nb_edges() == 0
    assert len(graph_test.get_adj_matrix()) == 1

    for node_neighbors in graph_test.get_adj_matrix():
        assert len(node_neighbors) == 1


def test_graph_with_54_nodes():
    graph_test = Graph(54, 0, [])
    assert graph_test.get_nb_nodes() == 54
    assert graph_test.get_nb_edges() == 0
    assert len(graph_test.get_adj_matrix()) == 54

    for node_neighbors in graph_test.get_adj_matrix():
        assert len(node_neighbors) == 54


def test_edge_with_invalid_values():
    with pytest.raises(ValueError):
        Graph(2, 1, [[0, 3, 3]])


def test_adj_matrix_correctly_filled():
    graph_test = Graph(3, 2, [[0, 2, 3], [0, 1, 1]])
    assert graph_test.get_nb_nodes() == 3
    assert graph_test.get_nb_edges() == 2
    graph_test_adj_matrix = graph_test.get_adj_matrix()

    for i in range(3):
        for j in range(3):
            if i == 0 and j == 1:
                assert graph_test_adj_matrix[i][j] == 1
            elif i == 0 and j == 2:
                assert graph_test_adj_matrix[i][j] == 3
            elif i == j:
                assert graph_test_adj_matrix[i][j] == 0
            else:
                assert graph_test_adj_matrix[i][j] == inf


def test_get_path_incorrect_start_id():
    graph_test = Graph(2, 1, [[0, 1, 1]])
    dist, prev, have_negative_cycle, logs = graph_test.floyd_warshall()

    with pytest.raises(ValueError):
        graph_test.get_path(-2, 1, prev, dist)


def test_get_path_incorrect_end_id():
    graph_test = Graph(2, 1, [[0, 1, 1]])
    dist, prev, have_negative_cycle, logs = graph_test.floyd_warshall()

    with pytest.raises(ValueError):
        graph_test.get_path(0, 8, prev, dist)


def test_get_path_when_no_path():
    graph_test = Graph(3, 1, [[0, 1, 1]])
    dist, prev, have_negative_cycle, logs = graph_test.floyd_warshall()
    assert graph_test.get_path(0, 2, prev, dist) == "Pas de chemin."


def test_get_path_direct_path():
    graph_test = Graph(2, 1, [[0, 1, -4]])
    dist, prev, have_negative_cycle, logs = graph_test.floyd_warshall()
    assert graph_test.get_path(0, 1, prev, dist) == "0->1 (-4)"


def test_get_path_more_complex():
    graph_test = Graph(4, 7, [[0, 1, 2], [0, 3, 6], [1, 2, -2], [2, 3, 5], [2, 1, 5], [3, 0, -4], [3, 1, -1]])
    dist, prev, have_negative_cycle, logs = graph_test.floyd_warshall()
    assert graph_test.get_path(3, 1, prev, dist) == "3->0->1 (-2)"


def test_get_paths_should_throw_error_when_prev_is_null():
    graph_test = Graph(2, 1, [[0, 1, 1]])
    dist, prev, have_negative_cycle, logs = graph_test.floyd_warshall()
    with pytest.raises(ValueError):
        graph_test.get_paths(None, dist)


def test_get_paths_should_throw_error_when_dist_is_null():
    graph_test = Graph(2, 1, [[0, 1, 1]])
    dist, prev, have_negative_cycle, logs = graph_test.floyd_warshall()
    with pytest.raises(ValueError):
        graph_test.get_paths(prev, None)


def test_get_paths_graph():
    graph_test = Graph(3, 2, [[0, 1, 1], [1, 2, 3]])
    dist, prev, have_negative_cycle, logs = graph_test.floyd_warshall()
    paths = graph_test.get_paths(prev, dist)
    assert paths == "Chemin le plus court entre 0 et 1 : 0->1 (1)\n" \
                    "Chemin le plus court entre 0 et 2 : 0->1->2 (4)\n" \
                    "Chemin le plus court entre 1 et 0 : Pas de chemin.\n" \
                    "Chemin le plus court entre 1 et 2 : 1->2 (3)\n" \
                    "Chemin le plus court entre 2 et 0 : Pas de chemin.\n" \
                    "Chemin le plus court entre 2 et 1 : Pas de chemin.\n"
