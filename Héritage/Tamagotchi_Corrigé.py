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
    def __init__ (self, name, food):
        Animal.__init__ (self, name, "Chien")
        self.cri = "aboie"
        self.nourriture = food
        
class Peruche(Animal):
    def __init__ (self, name, food):
        Animal.__init__ (self, name, "Péruche")
        self.cri = "siffle"
        self.nourriture = food

class Alligator(Animal):
    def __init__ (self, name, food):
        Animal.__init__ (self, name, "Alligator")
        self.cri = "vagi"
        self.nourriture = food

class Chat(Animal):
    def __init__ (self, name, food):
        Animal.__init__ (self, name, "Chat")
        self.cri = "miaule"
        self.nourriture = food


#Main
choixAnimal = input("Choisissez votre animal de compagnie parmis les suivants : un Chien, un Chat, une Péruche et un Alligator : ")
if (choixAnimal == "Chat") :
    choixNom = input("Choisissez un nom pour votre chat : ")
    monAnimal = Chat(choixNom, "Poisson")
    print(choixNom + " est un " + choixAnimal)
    print(monAnimal.crie() + ", cela signifie qu'il/elle a faim !")
    choixNourriture = input("Choisissez la nourriture adaptée parmis les suivantes : Croquettes, Poisson, Graines, Viande : ")
    if (choixNourriture == monAnimal.nourriture):
        print(choixNom + "est rasasié !")
    else :
        print(choixNom + " n'aime pas cette nourriture !")

if (choixAnimal == "Chien") :
    choixNom = input("Choisissez un nom pour votre chien : ")
    monAnimal = Chien(choixNom, "Croquette")
    print(choixNom + " est un " + choixAnimal)
    print(monAnimal.crie() + ", cela signifie qu'il/elle a faim !")
    choixNourriture = input("Choisissez la nourriture adaptée parmis les suivantes : Croquettes, Poisson, Graines, Viande : ")
    if (choixNourriture == monAnimal.nourriture):
        print(choixNom + "est rasasié !")
    else :
        print(choixNom + " n'aime pas cette nourriture !")

if (choixAnimal == "Péruche") :
    choixNom = input("Choisissez un nom pour votre péruche : ")
    monAnimal = Peruche(choixNom, "Graine")
    print(choixNom + " est une " + choixAnimal)
    print(monAnimal.crie() + ", cela signifie qu'il/elle a faim !")
    choixNourriture = input("Choisissez la nourriture adaptée parmis les suivantes : Croquettes, Poisson, Graines, Viande : ")
    if (choixNourriture == monAnimal.nourriture):
        print(choixNom + "est rasasié !")
    else :
        print(choixNom + " n'aime pas cette nourriture !")

if (choixAnimal == "Alligator") :
    choixNom = input("Choisissez un nom pour votre alligator : ")
    monAnimal = Alligator(choixNom, "Viande")
    print(choixNom + " est un " + choixAnimal)
    print(monAnimal.crie() + ", cela signifie qu'il/elle a faim ! ")
    choixNourriture = input("Choisissez la nourriture adaptée parmis les suivantes : Croquettes, Poisson, Graines, Viande : ")
    if (choixNourriture == monAnimal.nourriture):
        print(choixNom + "est rasasié !")
    else :
        print(choixNom + " n'aime pas cette nourriture !")
    
input()