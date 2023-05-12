import string

# initialisation d'un dictionnaire pour stocker les fréquences
freq_dict = {}
for letter in string.ascii_lowercase:
    freq_dict[letter] = {}
freq_dict[' '] = {} # Initialisation de la clé ' '

# ouverture du fichier en mode lecture
with open("data.txt", "r") as f:
    data = f.read().lower() # lecture et mise en minuscule des données
    total_chars = len(data)
    
    # parcours du fichier et mise à jour des fréquences
    for i in range(total_chars-1):
        current_char = data[i]
        next_char = data[i+1]
        
        if next_char in freq_dict[current_char]:
            freq_dict[current_char][next_char] += 1
        else:
            freq_dict[current_char][next_char] = 1

# affichage des résultats sous forme de graphique
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))
for letter in string.ascii_lowercase:
    freq_list = sorted(freq_dict[letter].items(), key=lambda x: x[0])
    total_occurrences = sum([x[1] for x in freq_list])
    freq_pct = [(x[1]/total_occurrences)*100 for x in freq_list]
    
    plt.plot([x[0] for x in freq_list], freq_pct, label=letter)
    
plt.xlabel("Lettres suivantes")
plt.ylabel("Pourcentage d'apparition")
plt.legend()
plt.show()