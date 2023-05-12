class Person:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

class Author(Person):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def listerOeuvre(self):
        if len(self.oeuvre) == 0:
            print(f"{self.nom} {self.prenom} hasn't written anything yet.")
        else:
            print(f"{self.nom} {self.prenom} has written :")
            for livre in self.oeuvre:
                print(livre.titre)

    def ecrireUnLivre(self, titre):
        livre = Book(titre, self)
        self.oeuvre.append(livre)

class Book:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

class Customer(Person):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = []

    def inventaire(self):
        if len(self.collection) == 0:
            print(f"{self.nom} {self.prenom} does not own any books.")
        else:
            print(f"{self.nom} {self.prenom} has :")
            for livre in self.collection:
                print(livre.titre)

class Library:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        for livre in auteur.oeuvre:
            if livre.titre == titre:
                if titre in self.catalogue:
                    self.catalogue[titre] += quantite
                else:
                    self.catalogue[titre] = quantite
                print(f"The library has bought {quantite} copy(ies) of the book {titre}.")
                return
        print(f"The book {titre} is not available with the author {auteur.nom} {auteur.prenom}.")

    def inventaire(self):
        if len(self.catalogue) == 0:
            print(f"The library catalog {self.nom} is empty.")
        else:
            print(f"The library {self.nom} has :")
            for livre, quantite in self.catalogue.items():
                print(f"{quantite} exemplaire(s) de {livre}")

    def louer(self, client, titre):
        if titre in self.catalogue and self.catalogue[titre] > 0:
            for livre in client.collection:
                if livre.titre == titre:
                    print(f"{client.nom} {client.prenom} has already praised the book {titre}.")
                    return
            livre = Book(titre, None)
            client.collection.append(livre)
            self.catalogue[titre] -= 1
            print(f"{client.nom} {client.prenom} praised the book {titre}.")
        else:
            print(f"The book {titre} is not available")

    def rendreLivres(self, client):
        for livre in client.collection:
            if livre.titre in self.catalogue:
                self.catalogue[livre.titre] += 1
            else:
                self.catalogue[livre.titre] = 1
        client.collection = []
        print(f"{client.nom} {client.prenom} returned all his books.")

# Créations des auteurs
author1 = Author("Ismail", "Hassan")
author2 = Author("Noura", "Ali")

# Affichage de l'inventaire de la bibliothèque avant l'achat de livre
author1.ecrireUnLivre("My first title")
author1.ecrireUnLivre("My second title")
author2.ecrireUnLivre("My third title")
print("----------------")

#Création de la bibliothèque
library = Library("Zoula Library")
print("----------------")

#Achat de livres par la bibliothèque
library.acheterLivre(author1, "La vie est belle", 5)
library.acheterLivre(author2, "Quoi de beau", 3)
library.acheterLivre(author2, "Programming is amazing", 2)
print("----------------")

customer1 = Customer("Samir", "Warsama")
customer2 = Customer("Bouh", "Boured")
print("----------------")

#Louer des livres par les clients
library.louer(customer1, "Quoi de neuf")
library.louer(customer1, "La vie est belle")
library.louer(customer2, "Je mange du pain")
library.louer(customer2, "Vancances a paris")
print("----------------")

#Affichage des livres en possession des clients
customer1.inventaire()
customer2.inventaire()
print("----------------")

#Affichage de l'inventaire de la bibliothèque après la location de livres
library.inventaire()

print("----------------")
#Retour des livres des clients à la bibliothèque
library.rendreLivres(customer1)
library.rendreLivres(customer2)

print("----------------")
#Affichage de l'inventaire de la bibliothèque 
#après le retour des livres

library.inventaire()
print("----------------")
#Affichage des livres en possession des clients après le retour des livres
customer1.inventaire()
customer2.inventaire()