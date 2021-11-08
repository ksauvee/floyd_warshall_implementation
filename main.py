from src.graph_selector import GraphSelector
from src.graph_parser import GraphParser

if __name__ == "__main__":
    print("Bienvenue !")

    isLoopContinuing = 1

    while isLoopContinuing == 1:
        print("\nSelection du graphe...")
        graph_filename_chosen = GraphSelector.graph_selector()
        print("\nCréation du graphe...")
        graph_chosen = GraphParser.graph_file_parser(graph_filename_chosen)

        print("\nAffichage du graphe...")
        # Display graph here
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
        else:
            print("Il n'existe pas de circuits absorbants !")
            print("\nAffichage des chemins les plus courts entre chaque paire de sommets...")
            graph_chosen.display_paths()

        print("\nSouhaitez-vous tester un autre Automate ?\n- 1 : Oui\n- 2 : Non")
        isLoopContinuing = int(input())

    print("\nAu revoir !")
