class GraphSelector:
    """
    GraphSelector manages the selection among graphs.
    """
    @staticmethod
    def graph_selector(store_traces):
        """
        Handles the choice of the graph test by the user.
        :return: the path to the text file of the graph chosen by the user.
        """
        test_graph_filename_prefix = "resources/test_graphs/"
        print("Entrez le numéro du graphe que vous souhaitez tester : ", end="")
        graph_number_chosen = input()

        while not (graph_number_chosen.isnumeric() and 1 <= int(graph_number_chosen) <= 13):
            print("Entrez le numéro du graphe que vous souhaitez tester (Veuillez entrer un nombre entre 1 et 13 "
                  "inclus) : ", end="")
            graph_number_chosen = input()

        test_graph_file_chosen = test_graph_filename_prefix + graph_number_chosen + ".txt"
        execution_traces_filepath = ""
        if store_traces:
            execution_traces_filepath = "resources/execution_traces/trace_" + graph_number_chosen + ".txt"

        return test_graph_file_chosen, execution_traces_filepath
