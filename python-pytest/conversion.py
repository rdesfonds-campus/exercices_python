# conversion.py
from roman import to_roman  # même dossier, on importe directement

def main() -> None:
    nombre = 26120
    resultat = to_roman(nombre)
    print(nombre, "en chiffres romains =", resultat)

if __name__ == "__main__":
    main()