
def puissance(x,n):
    if n == 1: # si on atteint 1 on s'arrete car y'aura rien de plus a calculer
        return x
    x = x * puissance(x,n -1) # on décrémente les puissance pour finir les nombre des possibles a calculer 
            # en dehors de 1 , 0 et nombres negatifs
    return x # on retourne une succession de calcul fait récurivement et a la fin on a le calcul de notre puissance     

print(puissance(5,5)) 