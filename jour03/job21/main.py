#Créer un générateur de mots en vous appuyant sur les statistiques précédemment
#calculées (longueur des mots, première lettre des mots, enchaînement de lettres).

import random

# longueurs de mots
word_lengths = [3, 4, 5, 6, 7, 8, 9, 10]

# première lettre des mots
first_letters = {'a': 0.2, 'b': 0.1, 'c': 0.15, 'd': 0.05, 'e': 0.25, 'f': 0.1, 'g': 0.05, 'h': 0.1}

# enchaînement de lettres
letter_pairs = {'th': 0.15, 'he': 0.12, 'in': 0.08, 'er': 0.07, 'an': 0.06, 're': 0.05, 'es': 0.04, 'on': 0.04, 'st': 0.03, 'nt': 0.03, 'en': 0.03, 'at': 0.02, 'ed': 0.02, 'nd': 0.02, 'to': 0.02, 'or': 0.02, 'ea': 0.02, 'ti': 0.02, 'ar': 0.02, 'te': 0.02, 'ng': 0.02}

def generate_word():
    # choisir une longueur de mot aléatoire
    length = random.choice(word_lengths)

    # choisir une première lettre en fonction des probabilités
    first_letter = random.choices(list(first_letters.keys()), weights=list(first_letters.values()))[0]

    # créer le mot en itérant jusqu'à la longueur souhaitée
    word = [first_letter]
    for i in range(length - 1):
        # choisir une lettre en fonction des lettres précédentes et des probabilités
        previous_letters = ''.join(word[-2:])
        possible_next_letters = [pair[1] for pair in letter_pairs.items() if pair[0].startswith(previous_letters)]
        if possible_next_letters:
            next_letter = random.choice(possible_next_letters)
        else:
            # s'il n'y a pas de correspondance pour les paires précédentes, choisir une lettre aléatoire
            next_letter = random.choice('abcdefghijklmnopqrstuvwxyz')
        word.append(next_letter)

    # assembler les lettres pour former le mot final
    return ''.join(word)

# exemple d'utilisation
for i in range(10):
    print(generate_word())