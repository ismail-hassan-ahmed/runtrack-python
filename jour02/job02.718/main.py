class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = []

    def inventaire(self):
        print(f"Livres en possession de {self.prenom} {self.nom}:")
        for livre in self.collection:
            print(livre.titre)

class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        for livre in auteur.oeuvre:
            if livre.titre == titre:
                self.catalogue[livre] = self.catalogue.get(livre, 0) + quantite
                print(f"{quantite} exemplaires de {livre.titre} ont été ajoutés au catalogue de {self.nom}")
                return
        print(f"Le livre '{titre}' n'existe pas dans l'œuvre de {auteur.nom}")

    def inventaire(self):
        print(f"Catalogue de {self.nom}:")
        for livre, quantite in self.catalogue.items():
            print(f"{livre.titre} ({quantite} exemplaires)")

    def louer(self, client, titre):
        for livre in self.catalogue:
            if livre.titre == titre and self.catalogue[livre] > 0:
                client.collection.append(livre)
                self.catalogue[livre] -= 1
                print(f"{client.prenom} {client.nom} a loué le livre '{livre.titre}'")
                return
        print(f"Le livre '{titre}' n'est pas disponible dans {self.nom}")

    def rendreLivres(self, client):
        for livre in client.collection:
            self.catalogue[livre] = self.catalogue.get(livre, 0) + 1
        client.collection = []
        print(f"{client.prenom} {client.nom} a rendu tous ses livres à {self.nom}")
