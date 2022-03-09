class Chapitre :
    def __init__ (self,gold, hp, text, links) :
        self.__orGagne = gold
        self.__pvPerdus = hp
        self.__texte =  text
        self.__listeLiens = links
    def getTexte (self):
        return self.__texte
    def getPvPerdus (self) :
        return self.__pvPerdus
    def getLoot (self) :
        return self.__orGagne
    def getListeLiens (self) :
        listeLiens = {0 : "Chapitre 0", 1 : "Chapitre 1", 2 : "Chapitre 2", 3 : "Chapitre 3", 4 : "Chapitre 4", 5 : "chapitre 5", 6 : "chapitre 6", 7 : "chapitre 7"}
            for i in range(self.__ListeLiens):
                if(i == self.__ListeLiens):
                    self.__ListeLiens = listeLiens[i]
        return self.__listeLiens



class Personnage :
    def __init__ (self, name, hp, gold) :
        self.__Nom = name
        self.__PV = hp
        self.__Or = gold
    def getNom (self) :
        return self.__Nom
    def getPV (self) :
        return self.__PV
    def getOr (self) :
        return self.__Or
    def perdPV (self, nombrePV) :
        self.__PV = self.__PV - nombrePV
        return self.__PV
    def gainOr (self, nombreOr) :
        self.__Or = self.__Or + nombreOr
        return self.__Or

Dovakhiin = Personnage("Dovahkiin", 100, 0)
chapitre0 = Chapitre(0,0 "Vous vous réveiller dans une charette à destination d'Helgen où vous allez vous faire exécuter pour avoir tenter de traverser la frontière illégalement. Les Impériaux ont capturés des rebelles Sombrages et vous avec. Le bouureau vous appel... Quand soudain, un dragon surgit et commence à ravager la ville ! Ralof, un sombrage et Hadvar un impérial vous demande de les suivre. AVEC QUI DECIDEZ VOUS DE PARTIR ?",0)
chapitre1 = Chapitre()
chapitre2 = Chapitre()

#CHAPITRE 1

