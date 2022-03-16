class Animal:
    def __init__ (self, name, specie):
        self.nom = name
        self.espece = specie
        self.faim = 0
        self.cri = "n'a pas de cri"
    def mange(self, quantity):
        self.fam = self.faim - quantity
    def crie(self):
        print(self.nom + " " + self.cri)

class Chien(Animal):
    def __init__ (self, name):
        Animal.__int__ (self, name, "Chien")
        self.cri = "Aboie"
        print(self.nom + " " + self.cri + "n'aboie pas car il est bien dressé.")

class Chat(Animal):
    def __init__ (self, name):
        Animal.__int__ (self, name, "Chat")
        self.cri = "Miaule"
        print(self.nom + " " + self.cri + "et ronronne.")

#Main
choix = input()
if (choix == 1) :
    monAnimal = Chat("Odin")
else :
    monAnimal = Chien("Falco")

monAnimal.crie()

input()