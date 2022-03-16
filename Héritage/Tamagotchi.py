class Animal :
    def __init__ (self, name,specie) :
        self.nom = name
        self.espece = specie

class Chat(Animal) :
    def __init__ (self,name) :
        Animal.__init__(self, name, "Chat")
        self.cri = "Miaule"

class Chien(Animal) :
    def __init__ (self, name) :
        Animal.__init__(self, name, "Chien")
        self.cri = "Aboiemment"

class Alligator(Animal) :
    def __init__ (self, name) :
        Animal.__init__(self, name, "Alligator")
        self.cri = "Râle"

class Péruche(Animal) :
    def __init__ (self, name) :
        Animal.__init__(self, name, "Péruche")
        self.cri = "Chant"

class Lapin(Animal) :
    def __init__ (self, name) :
        Animal.__init__(self, name, "Lapin")
        self.cri = "Clapir"

#Déclaration
monChat = Chat("Odin")
monChien = Chien("Falco")
monAlligator = Alligator("Roger")
maPeruche = Péruche("Azur")
monLapin = Lapin("Civet")
listeAnimal = ["Odin", "Falco", "Roger", "Azur", "Civet"]
choixAnimal = "0"
#Main
print("Bienvenue dans l'animalerie de LaVille !")
while choixAnimal not in listeAnimal :
    choixAnimal = int(input("Choisissez votre animal parmis les suivants (Entrez le nom de l'animal): Odin le Chat | Falco le Chien | Roger l'Alligator | Azur la Péruche ou Civet le Lapin : "))
    if choixAnimal in listeAnimal :
        print("Vous avez choisis", choixAnimal, " ! ")
    else :
        print("Ce choix ne figure pas parmis les animaux proposés ! Recommencez !")

input()