
class Person:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("My name is ", self.nom, self.prenom)

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getPrenom(self):
        return self.prenom

    def setPrenom(self, prenom):
        self.prenom = prenom

# Instances
person1 = Person("Ismail", "Hassan-Ahmed")
person2 = Person('Mounira', 'Aden')


person1.SePresenter() 
person2.SePresenter()  


last_name = person1.getNom()
print(last_name)  


person2.setPrenom("Fathia")
person2.SePresenter()