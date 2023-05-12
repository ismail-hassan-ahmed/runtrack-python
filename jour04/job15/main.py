def compare_chaines(chaine1, chaine2):
    if len(chaine1) != len(chaine2) and '*' not in chaine2:
        return 0

    i, j = 0, 0
    while i < len(chaine1) and j < len(chaine2):
        if chaine2[j] == '*':
            j += 1
            while j < len(chaine2) and chaine2[j] == '*':
                j += 1
            if j == len(chaine2):
                return 1
            while i < len(chaine1) and chaine1[i] != chaine2[j]:
                i += 1
            if i == len(chaine1):
                return 0
        elif chaine1[i] == chaine2[j]:
            i += 1
            j += 1
        else:
            return 0
    if i == len(chaine1) and j == len(chaine2):
        return 1
    else:
        return 0

chaine1 = input("Entrez la première chaîne : ")
chaine2 = input("Entrez la deuxième chaîne : ")
resultat = compare_chaines(chaine1, chaine2)
print(resultat)