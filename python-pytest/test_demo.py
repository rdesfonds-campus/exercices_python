# Test découverte pytest

def addition(a: int, b: int) -> int:
    # Cette fonction prend deux nombres entiers et retourne leur somme
    return a + b


def test_addition():
    # GIVEN : on prépare les données d'entrée
    a = 2
    b = 3

    # WHEN : on appelle la fonction que l'on veut tester
    resultat = addition(a, b)

    # THEN : on vérifie que le résultat est celui attendu
    # Si cette condition est fausse, pytest dira que le test a échoué
    assert resultat == 5