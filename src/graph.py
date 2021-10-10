class Graph:
    """Graph represents graph used for floyd-warshall algorithm"""
    def __init__(self, nb_nodes, nb_edges, edges):
        # test incoherent values
        if nb_nodes < 0 or nb_edges < 0 or len(edges) != nb_edges:
            raise ValueError
        self.__nb_nodes = nb_nodes
        self.__adj_matrix = [[0 for _ in range(self.__nb_nodes)] for _ in range(self.__nb_nodes)]

    def get_adj_matrix(self):
        new_adj_matrix = [node_neighbors.copy() for node_neighbors in self.__adj_matrix]
        return new_adj_matrix
