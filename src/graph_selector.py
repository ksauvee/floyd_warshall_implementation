class GraphSelector:
    """
    GraphSelector manages the selection among graphs.
    """
    @staticmethod
    def graph_selector():
        """
        Handles the choice of the graph test by the user.
        :return: the path to the text file of the graph chosen by the user.
        """
        test_graph_filename_prefix = "resources/test_graphs/G-"
        graph_number_chosen = "-1"

        while not graph_number_chosen.isnumeric():
            print("Entrez le numéro du graphe que vous souhaitez tester : ", end="")
            graph_number_chosen = input()

        test_graph_file_chosen = test_graph_filename_prefix + graph_number_chosen + ".txt"

        return test_graph_file_chosen
