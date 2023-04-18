numbers = []
for i in range(5):
    number = int(input("Veuillez saisir un nombre :"))
    numbers.append(number)

# On trie les nombres par ordre croissant
numbers.sort()

# Et on les affiche dans le terminal par ordre croissant
print("Voici les nombres triés par ordre croissant :")
for number in numbers:
    print(number)
