class Chapitre :
    def __init__(self, gold, hp, txt, links) :
        self.__orGagne = gold
        self.__pvPerdus = hp
        self.__texte = txt
        self.__listeLiens = links
    def getOrGagne(self):
        return self.__orGagne
    def getPvPerdus(self) :
        return self.__pvPerdus
    def getTexte(self) :
        return self.__texte
    def getListeLiens(self) :
        return self.__listeLiens

class Personnage:
    def __init__ (self,name) :
        self.__nom = name
        self.__pv = 100
        self.__or = 0
    def getNom(self) :
        return self.__nom
    def getPv (self) :
        return self.__pv
    def getOr (self) :
        return self.__or
    def perdPv (self,nombre) :
        self.__pv -= nombre
        if (self.__pv <= 0):
            self.__pv = 0
        return self.__pv
    def gagneOr (self,nombre) :
        self.__or +=nombre
        return self.__or
    
#Prog Pincipal

chapitre1 = Chapitre(0,2,"Vous êtes en pleine fôret, près d'une ville...Vous pouvez aller en 2, en 4 ou en 8 !", [2,4,8])
chapitre2 = Chapitre (1,24, "Un gros monstre te défonce mais tu as réussi à lui voler une pièce ! P'tit chanceux ! Tu gagnes 1 Or et perd 24 PV !", [])
chapitre4 = Chapitre (1,3, "Un Voyou te tabasse la tronche mais il fait tomber une pièce pendant le processus ! Quel veinard ! Tu gagnes 1 Or et perd 3 PV !", [])
chapitre8 = Chapitre (38,87, "Vous échappez de justesse aux gardes mais vous êtes bléssé... Quelle chance ! Un cofre rempli d'Or ! Tu gagnes 38 Or et perds 87 PV !", [])

choixNom = input ("Nommez votre Personnage !")
perso = Personnage (choixNom)

livre = {1:chapitre1, 2:chapitre2, 4:chapitre4, 8:chapitre8}
choixJoueur = 1
chapitreCourant = chapitre1
victoire = False
defaite = False
numeroFinal = 8

while (not (victoire or defaite)) :
    print(chapitreCourant.getTexte())
    pvActuels = perso.perdPv(chapitreCourant.getPvPerdus())
    perso.gagneOr(chapitreCourant.getOrGagne())

    if (pvActuels == 0):
        defaite = True
        print("Vous avez perdu !")

    if (choixJoueur == numeroFinal and not defaite):
        print("Vous avez gagné !")
        victoire = True
    else :
        choixValable = False
        while(not choixValable) :
            choixJoueur = int(input("Où souhaitez-vous aller ?"))
            if choixJoueur in chapitreCourant.getListeLiens() :
                choixValable = True
        chapitreCourant = livre[choixJoueur]