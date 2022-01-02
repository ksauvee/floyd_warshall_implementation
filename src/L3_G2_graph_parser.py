from src.L3_G2_graph import Graph


class GraphParser:
    """
    GraphParser manages different ways to initialize a graph
    """
    @staticmethod
    def translate_file_to_data(filename):
        """
        Translate graph characteristics stored in text file into data usable by Graph constructor.

        :param filename: the path to the test file.
        :type filename: str
        :return: number of graph nodes, number of graph edges, graph edges.
        """
        with open(filename, "r") as reader:
            nb_nodes = int(reader.readline())
            nb_edges = int(reader.readline())

            edges = list(list())
            for _ in range(nb_edges):
                edge_representation = reader.readline()
                # edge is represented by "node1 node2 weight" so we split the string by space
                edge = [int(value) for value in edge_representation.split()]
                edges.append(edge)

            return nb_nodes, nb_edges, edges

    @staticmethod
    def graph_file_parser(filename):
        """
        Generate graph by using data created by method translate_file_to_data.

        :param filename: the path to the test file.
        :type filename: str
        :return: a graph with the same characteristics as the text file.
        """
        nb_nodes, nb_edges, edges = GraphParser.translate_file_to_data(filename)
        return Graph(nb_nodes, nb_edges, edges)
