class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def listerOeuvre(self):
        print(f"{self.prenom} {self.nom} has written :")
        for livre in self.oeuvre:
            print(livre.titre)

    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)


class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def print(self):
        print(self.titre)

author1 = Auteur("Ismail", "Hassan")
author1.ecrireUnLivre("Mangez tous ce qui vous mange pas")
author1.ecrireUnLivre("La vie est belle")


author1.listerOeuvre()


author2 = Auteur("Noura", "Ali")
book1 = Livre("Yahou", author2)


book1.print()