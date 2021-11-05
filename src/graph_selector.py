class GraphSelector:
    """
    GraphSelector manages the selection among graphs.
    """
    @staticmethod
    def graph_selector():
        test_graph_filename_prefix = "resources/test_graphs/G?-"

        print("Entrez le numéro du graphe que vous souhaitez tester : ")
        graph_number_chosen = input()
        test_graph_file_chosen = test_graph_filename_prefix + graph_number_chosen + ".txt"

        return test_graph_file_chosen
