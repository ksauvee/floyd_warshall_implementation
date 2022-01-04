from src.graph_selector import GraphSelector
from src.graph_parser import GraphParser

if __name__ == "__main__":
    print("Bienvenue !")

    print("Voulez-vous sauvegarder les traces d'exécution ?\n- 1 : Oui\n- 2 : Non")
    choice = input()

    while not (choice.isnumeric() and 1 <= int(choice) <= 2):
        print("Voulez-vous sauvegarder les traces d'exécution ? (Veuillez entrer 1 ou 2)\n- 1 : Oui\n- 2 : Non")
        choice = input()

    choice = int(choice)
    store_traces = False
    if choice == 1:
        store_traces = True

    isLoopContinuing = 1

    while isLoopContinuing == 1:
        print("\nSelection du graphe...")
        graph_filename_chosen, execution_traces_filepath = GraphSelector.graph_selector(store_traces)
        print("\nCréation du graphe...")
        graph_chosen = GraphParser.graph_file_parser(graph_filename_chosen)

        logs = "Affichage du graphe : \n"
        logs += "\n" + graph_chosen.display_matrix(graph_chosen.get_adj_matrix())
        logs += "\nApplication de l'algorithme Floyd-Warshall...\n"
        try:
            print("Affichage des matrices L et P à chaque itération :")
            dist, prev, have_negative_cycle, floyd_warshall_logs = graph_chosen.floyd_warshall()
            logs += floyd_warshall_logs
        except ValueError:
            print("Erreur : Impossible d'appliquer l'algorithme de Floyd-Warshall sur ce graphe.\n"
                  "Vérifiez que le nombre de liens du graphe est >= 0.")
            continue
        logs += "\nRecherche de circuits absorbants...\n"
        if have_negative_cycle:
            logs += "Il existe des circuits absorbants !\n"
        else:
            logs += "Il n'existe pas de circuits absorbants !\n\n" \
                    + "Affichage des chemins les plus courts entre chaque paire de sommets : \n" \
                    + "Format: sommet_initial->sommet_2->...->sommet_terminal (longueur du chemin)\n\n"

            logs += graph_chosen.get_paths(prev, dist)

        print(logs)
        if store_traces:
            with open(execution_traces_filepath, "w") as traces_file:
                traces_file.write(logs)

        print("\nSouhaitez-vous tester un autre graphe ?\n- 1 : Oui\n- 2 : Non")
        isLoopContinuing = input()

        while not (isLoopContinuing.isnumeric() and 1 <= int(isLoopContinuing) <= 2):
            print("\nSouhaitez-vous tester un autre graphe ? (Veuillez entrer 1 ou 2)\n- 1 : Oui\n- 2 : Non")
            isLoopContinuing = input()

        isLoopContinuing = int(isLoopContinuing)

    print("\nAu revoir !")
