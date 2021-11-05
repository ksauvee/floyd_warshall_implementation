import pytest

from src.graph_parser import GraphParser


def test_translate_file_to_data_0_node():
    graph_test_nb_nodes, graph_test_nb_edges, graph_test_edges = \
        GraphParser.translate_file_to_data("resources/test_graphs/G?-1.txt")
    assert graph_test_nb_nodes == 0
    assert graph_test_nb_edges == 0
    assert len(graph_test_edges) == 0


def test_translate_file_to_data_1_node():
    graph_test_nb_nodes, graph_test_nb_edges, graph_test_edges = \
        GraphParser.translate_file_to_data("resources/test_graphs/G?-2.txt")
    assert graph_test_nb_nodes == 1
    assert graph_test_nb_edges == 0
    assert len(graph_test_edges) == 0


def test_translate_file_to_data_2_nodes():
    graph_test_nb_nodes, graph_test_nb_edges, graph_test_edges = \
        GraphParser.translate_file_to_data("resources/test_graphs/G?-3.txt")
    assert graph_test_nb_nodes == 2
    assert graph_test_nb_edges == 1
    assert len(graph_test_edges) == 1
    assert graph_test_edges == [[0, 1, 1]]


def test_translate_file_to_data_some_graph():
    graph_test_nb_nodes, graph_test_nb_edges, graph_test_edges = \
        GraphParser.translate_file_to_data("resources/test_graphs/G?-4.txt")
    assert graph_test_nb_nodes == 4
    assert graph_test_nb_edges == 5
    assert len(graph_test_edges) == 5
    assert graph_test_edges == [[3, 1, 25], [1, 0, 12], [2, 0, -5], [0, 1, 0], [2, 1, 7]]
