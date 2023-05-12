import re

def count_words():
    # Ouverture du fichier en mode lecture
    with open("data.txt", "r") as fichier:
        # Lecture du contenu du fichier
        content = fichier.read()

    # Utilisation d'une expression régulière pour trouver les mots
    words = re.findall(r'\b\w+\b', content)

    # Comptage du nombre de mots
    number_words = len(words)

    # Affichage du résultat
    print("Nombre de mots :", number_words)


count_words()
