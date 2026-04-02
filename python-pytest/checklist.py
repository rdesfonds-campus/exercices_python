# checklist.py

# On commence avec une liste vide pour stocker les tâches
tasks = []

def afficher_menu():
    """Affiche le menu principal."""
    print("=== CHECKLIST ===")
    print("1. Voir les tâches")
    print("2. Ajouter une tâche")
    print("3. Marquer une tâche comme faite")
    print("4. Quitter")

def afficher_taches():
    """Affiche toutes les tâches avec leur numéro."""
    if not tasks:
        print("Aucune tâche pour le moment.")
        return

    print("\nListe des tâches :")
    for index, task in enumerate(tasks):
        # index commence à 0, on ajoute 1 pour afficher à partir de 1
        statut = "✅" if task["done"] else "⬜"
        print(f"{index + 1}. {statut} {task['title']}")

def ajouter_tache():
    """Demande un titre et ajoute une nouvelle tâche non faite."""
    title = input("Titre de la nouvelle tâche : ")
    # On stocke chaque tâche comme un petit dictionnaire
    task = {
        "title": title,
        "done": False,
    }
    tasks.append(task)
    print("Tâche ajoutée !")

def marquer_tache_faite():
    """Demande le numéro de la tâche et la marque comme faite."""
    if not tasks:
        print("Pas de tâches à marquer.")
        return

    afficher_taches()
    choix = input("Numéro de la tâche à marquer comme faite : ")

    # On vérifie que l'utilisateur a bien tapé un nombre
    if not choix.isdigit():
        print("Merci d'entrer un numéro valide.")
        return

    index = int(choix) - 1  # on repasse à un index qui commence à 0

    if index < 0 or index >= len(tasks):
        print("Numéro de tâche invalide.")
        return

    tasks[index]["done"] = True
    print("Tâche marquée comme faite !")

def main():
    """Boucle principale du programme."""
    while True:
        afficher_menu()
        choix = input("Choisis une option (1-4) : ")

        if choix == "1":
            afficher_taches()
        elif choix == "2":
            ajouter_tache()
        elif choix == "3":
            marquer_tache_faite()
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, essaie encore.")

        print()  # ligne vide pour l'esthétique

# Ce bloc permet de lancer main() seulement si on exécute ce fichier
if __name__ == "__main__":
    main()