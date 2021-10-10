class floyd_warshall_graph:
    def __init__(self, nb_nodes, ):
        if nb_nodes < 0:
            raise ValueError
        self.__nb_nodes = nb_nodes
        self.__adj_matrix = [[0 for _ in range(self.__nb_nodes)] for _ in range(self.__nb_nodes)]

    def get_adj_matrix(self):
        new_adj_matrix = [line.copy() for line in self.__adj_matrix]
        return new_adj_matrix
