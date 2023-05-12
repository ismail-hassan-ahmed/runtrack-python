import re

def count_words_length(length):
    # Ouverture du fichier en mode lecture
    with open("data.txt", "r") as fichier:
        # Lecture du contenu du fichier
        content = fichier.read()

    # Utilisation d'une expression régulière pour trouver les mots de la taille renseignée
    words = re.findall(r'\b\w{%d}\b' % length, content)

    # Comptage du nombre de mots
    number_words = len(words)

    # Affichage du résultat
    print("Nombre de mots de taille %d dans le fichier data.txt : %d" % (length, number_words))

# Demande à l'utilisateur de saisir un nombre entier
length = int(input("Veuillez saisir un nombre entier pour la taille des mots : "))

# Appel de la fonction
count_words_length(length)
