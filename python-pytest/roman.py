def to_roman(nombre: int) -> str:
    # Liste des "briques" triées de la plus grande à la plus petite
    # Chaque élément est un couple (valeur_arabe, symbole_romain)
    valeurs_romaines = [
        (1000, "M"),
        (500, "D"),
        (100, "C"),
        (50, "L"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    resultat = ""  # On commence avec une chaîne vide

    # On parcourt chaque "brique" de la liste
    for valeur, symbole in valeurs_romaines:
        # Tant que la valeur rentre dans le nombre,
        # on ajoute le symbole et on soustrait la valeur
        while nombre >= valeur:
            resultat = resultat + symbole
            nombre = nombre - valeur

    return resultat

