class Pokemon:
    def __init__(self, name, hp, power, resistance, type) :
        self.__nom = name
        self.__pv = hp
        self.__force = power
        self.__resistance = resistance
        self.__type = type
    def getName (self):
        return self.__nom
    def getHP (self) :
        return self.__pv
    def setHP(self,val):
        self.__pv = val
    def getDegats (self):
        return self.__force
    def getResistance (self):
        return self.__resistance
    def getType (self) :
        return self.__type

class Attaques :
    def __init__ (self, name, type, description, power) :
        self.__nom = name
        self.__type = type
        self.__texte = description
        self.__puissance = power
    def getNameAttaque(self) :
        return self.__nom
    def getType (self) :
        return self.__type
    def getTexte (self) :
        return self.__texte
    def getPuissance (self) :
        return self.__puissance
        
#Pokemon
pKmn1 = Pokemon("Alliagtueur", 100, 20, 10, "Eau")
pKmn2 = Pokemon("Typhlosion", 10, 20, 10, "Feu")

#Attaques
attaque1PKMN1 = Attaques ("Surpuissance", "Combat", "Une attaque puissante de type Combat", 30)
attaque2PKMN1 = Attaques ("Hydrocanon", "Eau", "Un puissant jet d'eau dirigé sur l'ennemi", 30)
attaque3PKMN1 = Attaques ("Crocs Givres", "Glace", "Le lanceur utilise une morsure glaciale", 25)
attaque4PKMN1 = Attaques ("Tranche", "Normal", "Un coup de griffe tranche l'ennemi", 25)

attaque1PKMN2 = Attaques ("")
attaque2PKMN2 = Attaques
attaque3PKMN2 = Attaques
attaque4PKMN2 = Attaques

print("Bienvenue dans ce duel de Pokemon qui oppose Kaiminus à Héricendre !",end=" ")
print("Que le combat commence !!!")
print("Kaiminus a ", pKmn1.getHP()," PV et Héricencdre a ", pKmn2.getHP()," PV")

while (pKmn1.getHP() > 0) and (pKmn2.getHP() > 0) :
    print("Héricendre attaque !")
    pKmn1.setHP(pKmn1.getHP() - pKmn2.getDegats() + pKmn1.getResistance())
    print("Kaiminus a ", pKmn1.getHP(), " PV ! ")
    print("Au tour de Kaiminus !")
    pKmn2.setHP(pKmn2.getHP() - pKmn1.getDegats() + pKmn2.getResistance())
    print("Héricendre a ", pKmn2.getHP(), " PV !")

if (pKmn1.getHP() <= 0) :
    print("Héricendre est le vainqueur !!")
elif (pKmn2.getHP() <= 0):
    print("Kaiminus est le vainqueur !!")

