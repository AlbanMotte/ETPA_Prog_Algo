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

class Chapitre:
    def __init__(self,goldModif,pvModif,txt,links):
        self.__modifGold = goldModif
        self.__modifPV = pvModif
        self.__ListeLiens = links
        self.__text = txt

    def getListeLiens(self):
        listeLiens = {0 : "Chapitre 0", 1 : "chapitre 1", 2 : "chapitre 2", 3 : "chapitre 3", 4 : "chapitre 4", 5 : "chapitre 5", 6 : "chapitre 6", 7 : "chapitre 7"}
        for i in range(self.__ListeLiens):
            if(i == self.__ListeLiens):
                self.__ListeLiens = listeLiens[i]
        return self.__ListeLiens

    def getPvPerdus(self, new):
        if (new > 150) :
            self.__modifPV = 150
        else : 
            self.__modifPV = self.__modifPV + new
        return self.__modifPV

    def GetOrGagne(self, change):
        self.__modifGold = self.__modifGold + change
        return self.__modifGold
    
    def getText(self):
        print(self.__text)

class Personnage:
    def __init__(self,name,gold,pv):
        self.__nom = name
        self.__monnaie = gold
        self.__vie = pv

    def getNom(self):
        return self.__nom
    def getOr(self):
        return self.__monnaie
    def getPv(self):
        return self.__vie
    def perdPv(self, modif):
        if (modif > 150) :
            self.__vie = 150
        else : 
            self.__vie = self.__vie + modif
        return self.__vie 
    def gagneOr(self, modifG):
        if (modifG <= -self.__monnaie) :
            self.__monnaie = 0
        else : 
            self.__monnaie = self.__monnaie + modifG
        return self.__vie 

Georges = Personnage("Balruf Georges", 100, 150)
Chapitre0 = Chapitre(100,0,"Vous arrivez ?? votre guilde pour vous inscire. Apr??s votre inscription vous recevez 100 d'or et on vous fait comprendre que chaque qu??te accomplit sera tax?? par la guilde, vous ??tes actuellement au maximum de votre forme (150 pv). Vous d??cidez finalement de prendre une qu??te." ,0)
Chapitre1 = Chapitre(25,-35,"Vous avez donc prit la qu??te pour chasser des loups. Alors que vous arrivez sur place, vous ??tes attaqu?? par des loups. Vous arrivez ?? les terrasser et d??cidez donc de r??cup??rer la fourrure. Par chance peu apr??s un marchand ambulant se pr??sente ?? vous et vous lui vendez tout.",1)
Chapitre2 = Chapitre(0,+100,"Apr??s cette m??saventure vous d??cidez de continuer dans la grotte. Alors que vous avancez, vous tombez sur une fontaine de f??e. Vous la buvez et vous vous sentez comme neuf.", 2)
Chapitre3 = Chapitre(0, 0, "Vous prenez une direction au hasard et marchez avec quelques provisions. ?? force de marche vous arrivez face ?? un panneau, sur l'une des faces il est ??crit 'Danger de mort' et sur l'autre 'Repaire de bandits'. Quel choix allez-vous faire ? \n1- Prendre le chemin mortel \n2- Prendre le chemin vers le repaire des bandits",3)
Chapitre4 = Chapitre(0, -200, "Alors que vous essayer de remonter cette pente, une pierre se d??robe sous votre main et vous tombez t??te la premi??re sur le sol, votre nuque fait un sacr?? bruit, mais au moins maintenant vous pouvez voir o?? vous vous grattez quand vous avez la main dans le dos",4)
Chapitre5 = Chapitre(0,-200,"Bhouahahaha bonne blague... ... Ha vraiment ? Bon eh bien alors que vous avancez dans le d??sert pour affronter cette salamandre g??ant vous vous rendez commpte qu'un pauvre couteau ne va pas suffire. C'est barbecue pour la salamandre semble-t-il.",5)
Chapitre6 = Chapitre(200,-100,"Alors que vous d??cidez d'aller rejoindre votre qu??te pour combattre de satan??s bandits, vous tombez sur une cal??che accompagn??e de gardes. Vous vous rendez compte que ces personnes et vos bandits s'affrontent, vous plongez pour les aider. Les bandits sont plut??t nombreux, sans cette escorte vous serez tr??s certainement mort... ?? l'int??rieur vous pouvez voir un baron et sa femme apeur??s.",6)

victoire = False
saisie = 0

while(victoire == False):
    print("Vous ??tes Balruf Georges, vous venez d'atteindre vos 21 ans quand vous d??cidez de devenir aventurier. L'inscription n'a rien de bien compliqu?? et vous avez soif d'aventure bien que vous n'ayez rien pour combattre hormis un petit couteau.")
    Chapitre0.getText()
    Georges.gagneOr(100)
    print("Plusieurs choix s'offrent ?? vous, vous pouvez : \n1- Aller vous inscrire dans la guilde des aventuriers \n 2- Partir ?? l'aventure de vous-m??me \n 3- Vous recouchez et abandonnez ce r??ve stupide")
    while(saisie > 3 or saisie == 0):   
        saisie = int(input("Veuillez saisir votre choix : 1, 2 ou 3 : "))
    if(saisie == 1) :
        saisie = 0
        Chapitre0.getText()
        Georges.gagneOr(100)
        print("Petit rappel sur votre ??tat : " , Georges.getPv() , " Pv et " , Georges.getOr() , " d'or")
        print("Vous voil?? donc inscrit et devant le tableau des qu??tes. Il y a de nombreuses qu??tes, pr??f??rez-vous prendre un qu??te : \n1- De bas niveau \n2- De niveau moyen \n3- De haut niveau ?")
        while(saisie > 3 or saisie == 0):   
            saisie = int(input("Veuillez saisir votre choix : 1, 2 ou 3 : "))

    if(saisie == 1) :
            saisie = 0
            Chapitre1.getText()
            Georges.gagneOr(25)
            Georges.perdPv(-35)
            print("Petit rappel sur votre ??tat : " , Georges.getPv() , " Pv et " , Georges.getOr() , " d'or")
            print("Apr??s votre combat contre les loups vous vous semblez affaiblit, une montagne vient vous barrez la route. Vous en faites le tour jusqu'?? tomber dans un trou, vous d??valez la pente vous blessant d'avantage. ?? la fin de tout ceci, vous vous retrouvez face ?? une crevasse")
            Georges.perdPv(-10)
            print("Vous pouvez soit : \n1- Continuer dans la grotte \n2- Remonter")
            while(saisie > 2 or saisie == 0):   
                saisie = int(input("Veuillez saisir votre choix : 1 ou 2 : "))
            if(saisie == 1):
                saisie = 0
                Chapitre2.getText()
                Georges.perdPv(+100)
                print("Petit rappel sur votre ??tat : " , Georges.getPv() , " Pv et " , Georges.getOr() , " d'or")
                print("Merci d'avoir jou?? ?? cette d??mo.")
                victoire = True
            if(saisie == 2): 
                saisie = 0
                Chapitre4.getText()
                Georges.perdPv(-200)
                print("Merci d'avoir jou?? ?? cette d??mo.")
                victoire = True
            if(saisie == 2):
                saisie = 0
                Chapitre6.getText()
                Georges.perdPv(-100)
                Georges.gagneOr(250)
                print("??a c'??tait du combat ??pique. Votre vaillance vous a valu d'??tre bien vu du noble, il vous r??compense gr??cement et vous invite ?? rejoindre son escorte jusqu'?? la prochaine ville.")
                print("Merci d'avoir jou?? ?? cette d??mo.")
                victoire = True
            if(saisie == 3):
                saisie = 0
                Chapitre5.getText()
                Georges.perdPv(-200)
                print("Merci d'avoir jou?? ?? cette d??mo.")
                victoire = True
            if(saisie == 2) :
                saisie = 0
                Chapitre3.getText()
                print("Petit rappel sur votre ??tat : " , Georges.getPv() , " Pv et " , Georges.getOr() , " d'or")
                while(saisie > 2 or saisie == 0):   
                    saisie = int(input("Veuillez saisir votre choix : 1 ou 2 : "))
                if(saisie == 1) :
                    saisie = 0
                    print("Il est vrai qu'au moyen-??ge le taux de personnes illettr??es ??tait haut, mais je vous ai pr??venu... Vous avancez, encore et encore, une brume vient doucement vous entourez. Puis vous disparaissez ?? jamais de ce monde sans que personne ne comprenne d'o??")
                    victoire = True
                if(saisie == 2) :
                    saisie = 0
                    print("Vous avancez jusqu'au repaire. L??-bas vous faites la recontre de plusieurs de ces sc??l??rats. Le chef vient se pr??senter ?? vous avec un grand marteau, visiblement ils sont tr??s nombreux. Il vous pose alors une question 'Que viens-tu faire par ici ?' Bonne question ??a, que venez-vous faire ? \n1- Les affronter \n2- Les rejoindre")
                    while(saisie > 2 or saisie == 0):   
                        saisie = int(input("Veuillez saisir votre choix : 1 ou 2 : "))
                    if(saisie == 1) :
                        saisie = 0
                        print("Vous lui sortez votre plus grande punchline avant de vous faire tabassez par le groupe.")
                        Georges.gagneOr(-250)
                        Georges.perdPv(-149)
                        print("Apr??s vous avoir d??pouill??, le chef des bandits vous fait prisonnier et se sert de vous comme otage.")
                        print("Petit rappel sur votre ??tat : " , Georges.getPv() , " Pv et " , Georges.getOr() , " d'or")
                        print("Merci d'avoir jou?? ?? cette d??mo.")
                        victoire = True