
def triDeMot():
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    result = input('Ecrivez une suite de lettres: ')
    new = ""
    
    for letter in result:
        if letter not in alphabet:
            print("Le mot doit contenir seulement des lettres de l'alphabet sans accent ni majuscule.")
            return

    for letter in result:
        i = alphabet.index(letter)
        if i == 25:
            new += letter
        else:
            new += alphabet[i+1]
            
    print("Le nouveau mot est :", new)

triDeMot()