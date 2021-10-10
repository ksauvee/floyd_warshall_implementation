class GraphParser:
    @staticmethod
    def translate_file_to_data(filename):
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
