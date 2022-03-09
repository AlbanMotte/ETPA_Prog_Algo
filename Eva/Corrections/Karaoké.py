class Joueur :
    def __init__(self, name) :
        self.__pseudo = name
        self.__score = [0,0,0,0,0]

    def getMoyenne(self):
        somme = 0
        nombreChanson = 0
        for i in range(len(self.__score)):
            if (self.__score[i]<50) :
                nombreChanson += 1
                somme = somme + self.__score[i]
            if (nombreChanson == 0) : 
                nombreChanson = 1
        return somme/nombreChanson
    
    def getScoreTotal(self):
        somme = 0
        for i in range (len(self.__score)):
            if (self.__score[i]>= 50):
                somme = somme + self.__score[i]
        return somme

    def afficherMeilleureChanson(self) :
        meilleureChanson = 0
        meilleureChansonScore = 0
        for i in range (len(self.__score)):
            if (self.__score[i]>meilleureChanson):
                meilleureChansonScore = self.__score[i]
                meilleureChanson = i
        print ("La meilleure chanson est la chanson ", meilleureChanson ,"avec un score de ", meilleureChansonScore)

    def afficherPireChanson(self) :
        meilleureChanson = 100
        meilleureChansonScore = 0
        for i in range (len(self.__score)):
            if (self.__score[i]<meilleureChanson):
                meilleureChansonScore = self.__score[i]
                meilleureChanson = i
        print ("La meilleure chanson est la chanson ", meilleureChanson ,"avec un score de ", meilleureChansonScore)

    def afficherScore (self) :
        for i in range (len(self.__score)):
            if (self.__score[i]<50):
                print("La chanson ", i, "n'a pas été jouée !")
            else:
                print("Chanson ", i , "avec un score de ", self.__score)

    def ajouteScore(self, numero, nombre):
        if (not(nombre<50 or nombre<self.__score[numero])) :
            self.__score[numero] = nombre

class Karaoke :
        def __init__(self) :
            self.__listeJoueurs = {}
            self.__listeChansons = ["Relight my Fire", "Don't wanna fall in Love", "Danger Zone", "September", "Easy Lover"]

        def ajouterJoueur (self, pseudo):
            nouveau = Joueur(pseudo)
            self.__listeJoueurs[pseudo] = nouveau

        def supprimeJoueur (self, pseudo):
            self.__listeJoueurs.pop(pseudo)

        def meilleurScoreChanson(self, numeroChanson):
            