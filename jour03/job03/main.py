import matplotlib.pyplot as plt
import string

def compte_occurrences():
    # Ouverture du fichier en mode lecture
    with open("data.txt", "r") as fichier:
        # Lecture du contenu du fichier
        contenu = fichier.read()

    # Conversion du contenu en lettres majuscules pour un comptage sans distinction
    contenu = contenu.upper()

    # Initialisation du dictionnaire pour stocker les occurrences de chaque lettre
    occurrences = {letter: 0 for letter in string.ascii_uppercase}

    # Comptage des occurrences de chaque lettre
    for char in contenu:
        if char in occurrences:
            occurrences[char] += 1

    # Calcul du total des lettres
    total_lettres = sum(occurrences.values())

    # Calcul du pourcentage d'apparition de chaque lettre
    pourcentages = {letter: (count / total_lettres) * 100 for letter, count in occurrences.items()}

    # Génération de l'histogramme
    lettres = list(pourcentages.keys())
    pourcentages_occurrences = list(pourcentages.values())

    plt.bar(lettres, pourcentages_occurrences)
    plt.xlabel('Lettres')
    plt.ylabel('Pourcentage d\'occurrence')
    plt.title('Occurrences des lettres dans le fichier data.txt')
    plt.show()

# Appel de la fonction
compte_occurrences()
