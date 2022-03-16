class Animal :
    def __init__ (self, name,specie) :
        self.nom = name
        self.espece = specie

class Chat(Animal) :
    def __init__ (self,name) :
        Animal.__init__(self, name, "Chat")
        self.cri = "Miaule"

#Main
monChat = Chat("Odin")

input()