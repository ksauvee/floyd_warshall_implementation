from math import inf


class Graph:
    """
    Graph represents graph used for floyd-warshall algorithm
    """

    def __init__(self, nb_nodes, nb_edges, edges):
        """
        Generate a graph by initialize nb_nodes, nb_edges and adjacency matrix.

        :param nb_nodes: number of graph nodes.
        :type nb_nodes: int
        :param nb_edges: number of graph edges.
        :type nb_edges: int
        :param edges: graph edges.
        :type edges: list(list(int))
        """
        # test incoherent values
        if nb_nodes < 0 or nb_edges < 0 or len(edges) != nb_edges:
            raise ValueError

        self.__nb_nodes = nb_nodes
        self.__nb_edges = nb_edges
        self.__adj_matrix = [[0 if i == j else inf for i in range(self.__nb_nodes)] for j in range(self.__nb_nodes)]

        # start node and end node in each edge should have node id between 0 and nb_nodes - 1
        for edge in edges:
            if not (0 <= edge[0] <= self.__nb_nodes - 1 and 0 <= edge[1] <= self.__nb_nodes - 1):
                raise ValueError

            start_node = edge[0]
            end_node = edge[1]
            weight_edge = edge[2]
            self.__adj_matrix[start_node][end_node] = weight_edge

    def get_nb_nodes(self):
        """
        Gets number of graph nodes.

        :return: the number of graph nodes.
        """
        return self.__nb_nodes

    def get_nb_edges(self):
        """
        Gets number of graph edges.

        :return: the number of graph edges.
        """
        return self.__nb_edges

    def get_adj_matrix(self):
        """
        Gets graph adjacency matrix.

        :return: the graph adjacency matrix.
        """
        # we use copy method in order to respect encapsulation.
        new_adj_matrix = [node_neighbors.copy() for node_neighbors in self.__adj_matrix]
        return new_adj_matrix

    def floyd_warshall(self):
        """
        Apply floyd-warshall algorithm on graph.

        :return 
            - dist : dist is a matrix n*n where dist[i][j] represents the shortest distance between i and j.
            - prev : prev is a matrix n*n where prev[i][j] represents the predecessor of j in this shortest path.
        """
        if self.__nb_edges <= 0:
            raise ValueError

        # initialization : in this step we set dist and prev by visiting direct paths given by adjacency matrix.
        dist, prev = [[self.__adj_matrix[i][j] for j in range(self.__nb_nodes)] for i in range(self.__nb_nodes)], [
            [i for _ in range(self.__nb_nodes)] for i in range(self.__nb_nodes)]

        floyd_warshall_logs = ""
        floyd_warshall_logs += "Initialisation:\n" + "L :\n"
        floyd_warshall_logs += self.display_matrix(dist)

        floyd_warshall_logs += "\n P :\n"
        floyd_warshall_logs += self.display_matrix(prev)

        floyd_warshall_logs += "\n\n"

        # iterations : in this step we set dist and prev by visiting paths passing through node k.
        for k in range(0, self.__nb_nodes):
            for i in range(0, self.__nb_nodes):
                for j in range(0, self.__nb_nodes):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        # we find a shorter distance between i and j so we actualize it.
                        dist[i][j] = dist[i][k] + dist[k][j]
                        # we also change the predecessor.
                        prev[i][j] = prev[k][j]

            floyd_warshall_logs += "Itération n°{}:".format(k + 1) + "\n" + "L :\n"
            floyd_warshall_logs += self.display_matrix(dist)

            floyd_warshall_logs += "\n P :\n"
            floyd_warshall_logs += self.display_matrix(prev)

            floyd_warshall_logs += "\n\n"

        dist, prev, have_negative_cycle = self.__detect_negative_cycle(dist, prev)
        return dist, prev, have_negative_cycle, floyd_warshall_logs

    def __detect_negative_cycle(self, dist, prev):
        have_negative_cycle = False
        # iteration : in this step we look if the path could be shorter than in the floyd warshall algorithm. We visit
        # every path passing through node k
        for k in range(0, self.__nb_nodes):
            for i in range(0, self.__nb_nodes):
                for j in range(0, self.__nb_nodes):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        # we find a shorter distance between i and j so we actualize it and put -inf to represent a
                        # negative cycle.
                        dist[i][j] = -inf
                        # he got no predecessor indeed he is in a negative cycle.
                        prev[i][j] = -1
                        have_negative_cycle = True

        return dist, prev, have_negative_cycle

    def get_path(self, start_node_id, end_node_id, graph_previous_matrix, graph_dist_matrix):
        """
        Get shortest path between start node and end node.

        :param start_node_id: the identifier of the starting node of the path.
        :type start_node_id: int
        :param end_node_id: the identifier of the end node of the path.
        :type end_node_id: int
        :param graph_previous_matrix: the graph previous matrix returned by floyd-warshall algorithm.
        :type graph_previous_matrix: list(list(int))
        :param graph_dist_matrix: the graph dist matrix returned by floyd-warshall algorithm.
        :type graph_dist_matrix: list(list(int))
        :return: the path between start node and end node.
        """
        if not (0 <= start_node_id <= self.__nb_nodes - 1 and 0 <= end_node_id <= self.__nb_nodes - 1):
            raise ValueError

        # if distance between nodes is infinity (no link between them) => no path
        if graph_dist_matrix[start_node_id][end_node_id] == inf:
            return "Pas de chemin."

        path_dist = graph_dist_matrix[start_node_id][end_node_id]

        path = str(end_node_id)
        while end_node_id != start_node_id:
            end_node_id = graph_previous_matrix[start_node_id][end_node_id]
            path = str(end_node_id) + "->" + path

        return path + " (" + str(path_dist) + ")"

    def get_paths(self, prev, dist):
        """
        Get the shortest path beetween every pair of node
        :return: paths list
        """
        if prev is None or dist is None:
            raise ValueError

        paths = ""
        for i in range(0, self.__nb_nodes):
            for j in range(0, self.__nb_nodes):
                if i != j:
                    paths += "Chemin le plus court entre " + str(i) + " et " + str(j) + " : " + str(
                        self.get_path(i, j, prev, dist)) + "\n"

        return paths

    def display_matrix(self, graph_matrix):
        """
        Display graph matrix either dist, prev or adjacency matrix.
        :param graph_matrix: the matrix to print.
        :type graph_matrix: list(list(int))
        """
        # max_number_length is the length of the largest number (including - for negative numbers in number length)
        max_number_length = max(max(x) for x in
                                [[len(number) for number in list(map(str, row))] for row in graph_matrix])
        max_number_length = max(max_number_length, len(str(self.__nb_nodes)) - 1)

        # first we print the list of nodes
        matrix_representation = "    "
        for node_id in range(self.__nb_nodes):
            # we print " " * (max_number_length - len(str(node_id)))
            # in order to align display according to the largest number
            matrix_representation += " " * (max_number_length - len(str(node_id)))
            matrix_representation += " {}".format(node_id)
        matrix_representation += "\n"

        # then we print the dashes
        matrix_representation += "    "
        for node_id in range(self.__nb_nodes):
            matrix_representation += "-" * (max_number_length + 1)
        matrix_representation += "\n"

        # finally, we print the adj matrix rows
        for starting_node in range(self.__nb_nodes):
            # we print the starting node
            matrix_representation += " {} |".format(starting_node)
            for ending_node in range(self.__nb_nodes):
                # here we print the weighs of the links between the starting node and the ending node
                # we print " " * (max_number_length - len(str(self.__adj_matrix[row][column])))
                # in order to align display according to the largest number
                matrix_representation += " " * (max_number_length - len(str(graph_matrix[starting_node][ending_node])))
                matrix_representation += " {}".format(graph_matrix[starting_node][ending_node])
            matrix_representation += "\n"
        return matrix_representation
