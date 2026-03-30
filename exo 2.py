import random

# --- DONNEES --- 
choix_possibles = ["pierre", "papier", "ciseaux"]

# --- FONCTION --- 
def determiner_gagnant(joueur, ordinateur):
    if joueur == ordinateur:
        return "Egalité !"
    
    # --- Combinaisons gagnantes ---
    combinaisons_gagnantes = [
        ("pierre", "ciseaux"),
        ("papier", "pierre"),
        ("ciseaux", "papier")
    ]

    if (joueur, ordinateur) in combinaisons_gagnantes:
        return "Tu gagnes !"
    else:
        return "L'ordinateur gagne !"

# --- Scores au début ---
score_joueur = 0
score_ordi = 0

print("=== Pierre - Papier - Ciseaux ===")
print("Tape 'quitter' pour arrêter le jeu.\n")

while True:
    choix_joueur = input("Ton choix (pierre / papier / ciseaux) : ").lower() #//lower passe les caractères majuscules en minuscules

    if choix_joueur == "quitter":
        print(f"\nPartie terminée ! Score final -> Toi : {score_joueur} | Ordi : {score_ordi}")
        break

    # Validation de la saisie
    if choix_joueur not in choix_possibles:
        print("Choix invalide, réessaie.\n")
        continue  # Repart au début de la boucle

    # Choix aléatoire de l'ordinateur
    choix_ordi = random.choice(choix_possibles)

    print(f"Ordinateur choisit : {choix_ordi}")

    # Résultat
    resultat = determiner_gagnant(choix_joueur, choix_ordi)
    print(f"→ {resultat}\n")

    # Mise à jour du score
    if resultat == "Tu gagnes !":
        score_joueur += 1
    elif resultat == "L'ordinateur gagne !":
        score_ordi += 1
