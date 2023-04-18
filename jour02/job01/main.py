class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def listerOeuvre(self):
        print(f"{self.prenom} {self.nom} a écrit :")
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

# Création d'un auteur et de ses livres
auteur1 = Auteur("Ismail", "Hassan")
auteur1.ecrireUnLivre("Mangez tous ce qui vous mange pas")
auteur1.ecrireUnLivre("")
auteur1.ecrireUnLivre("Les Contemplations")

# Affichage de la liste des livres de l'auteur
auteur1.listerOeuvre()

# Création d'un autre auteur et d'un livre
auteur2 = Auteur("Zola", "Emile")
livre1 = Livre("Germinal", auteur2)

# Affichage du titre d'un livre
livre1.print()