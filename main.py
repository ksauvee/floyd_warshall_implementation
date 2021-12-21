from src.graph_selector import GraphSelector
from src.graph_parser import GraphParser

if __name__ == "__main__":
    print("Bienvenue !")

    print("Voulez-vous sauvegarder les traces d'exécution ?\n- 1 : Oui\n- 2 : Non")
    choice = int(input())

    while not 1 <= choice <= 2:
        print("Voulez-vous sauvegarder les traces d'exécution ? (Veuillez entrer 1 ou 2)\n- 1 : Oui\n- 2 : Non")
        choice = int(input())

    store_traces = False
    if choice == 1:
        store_traces = True

    isLoopContinuing = 1

    while isLoopContinuing == 1:
        print("\nSelection du graphe...")
        graph_filename_chosen, execution_traces_filepath = GraphSelector.graph_selector(store_traces)
        print("\nCréation du graphe...")
        graph_chosen = GraphParser.graph_file_parser(graph_filename_chosen)

        print("\nAffichage du graphe : \n")
        graph_chosen.display_matrix(graph_chosen.get_adj_matrix())

        print("\nApplication de l'algorithme Floyd-Warshall...")
        try:
            dist, prev, have_negative_cycle = graph_chosen.floyd_warshall()
        except ValueError:
            print("Erreur : Impossible d'appliquer l'algorithme de Floyd-Warshall sur ce graphe.\n"
                  "Vérifiez que le nombre de liens du graphe est >= 0.")
            continue
        print("\nRecherche de circuits absorbants...")
        if have_negative_cycle:
            print("Il existe des circuits absorbants !")

            if store_traces:
                with open(execution_traces_filepath, "w") as traces_file:
                    traces_file.write("Il existe des circuits absorbants !")
        else:
            print("Il n'existe pas de circuits absorbants !\n")
            print("Affichage des chemins les plus courts entre chaque paire de sommets : ")
            print("Format: sommet_initial->sommet_2->...->sommet_terminal (longueur du chemin)\n")
            paths = graph_chosen.get_paths(prev, dist)
            print(paths)

            if store_traces:
                with open(execution_traces_filepath, "w") as traces_file:
                    traces_file.write("Il n'existe pas de circuits absorbants !\n\n")
                    traces_file.write("Affichage des chemins les plus courts entre chaque paire de sommets : \n")
                    traces_file.write("Format: sommet_initial->sommet_2->...->sommet_terminal (longueur du chemin)\n\n")
                    traces_file.write(paths)

        print("\nSouhaitez-vous tester un autre graphe ?\n- 1 : Oui\n- 2 : Non")
        isLoopContinuing = int(input())

        while not 1 <= isLoopContinuing <= 2:
            print("\nSouhaitez-vous tester un autre graphe ? (Veuillez entrer 1 ou 2)\n- 1 : Oui\n- 2 : Non")
            isLoopContinuing = int(input())

    print("\nAu revoir !")
