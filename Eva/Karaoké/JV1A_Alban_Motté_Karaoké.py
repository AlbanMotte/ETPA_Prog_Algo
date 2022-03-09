class Player :
    def __init__ (self, name, score) :
        self.__nom = name
        self.__score = score
    def getScoreJoueur(self) :
        return self.__score
    def getNomJoueur(self) :
        return self.__nom

class Karaoke :
    def __init__(self, name, score, nombre) :
        self.__nomChanson = name
        self.__scoreChanson = score
    def getScoreChanson(self) :
        return self.__scoreChanson
    def getNomChanson(self) :
        return self.__nomChanson

print("Bienvenue aux résultats des scores de Karaoké")
nomJoueur = input ("Quel est votre pseudo ? ")
scoreMinimal = 50
scoreMaximal = 100
scoreChanson1 = 0
scoreChanson2 = 0
scoreChanson3 = 0
scoreChanson4 = 0
scoreChanson5 = 0

#Prog général

choixChanson = input("Choisissez le numéro de la chanson (1 à 5) dont vous voulez entrer un score : ")

while (scoreChanson1 and scoreChanson2 and scoreChanson3 and scoreChanson4 and scoreChanson5 != 0) :
    choixChanson = input("Choisissez le numéro de la chanson (1 à 5) dont vous voulez entrer un score : ")

    if (choixChanson == 1) :
        print("Vous avez choisis Feeling Good !")
        scoreChanson1 = input ("Quel est votre score sur cette chanson ? ")
        if (scoreChanson1 > scoreMinimal):
                score = scoreChanson1
        while (scoreChanson1 < scoreMinimal) :
                print(nomJoueur, ", votre score n'est pas valable, veuillez entrer un autre score !")
        if (scoreChanson1 >= scoreMaximal) :
                score = scoreChanson1
        print(nomJoueur, ", votre score est de ", scoreChanson1, "/100 ! sur Feeling Good")
    if (choixChanson == 2) :
        print("Vous avez choisis Relight my Fire !")
        scoreChanson2 = input ("Quel est votre score sur cette chanson ? ")
        if (scoreChanson2 > scoreMinimal):
            score = scoreChanson2
        while (scoreChanson2 < scoreMinimal) :
            print(nomJoueur, ", votre score n'est pas valable, veuillez entrer un autre score !")
        if (scoreChanson2 >= scoreMaximal) :
            score = scoreChanson2
        print(nomJoueur, ", votre score est de ", scoreChanson2, "/100 ! sur Relight my Fire")
    if (choixChanson == 3) :
        print("Vous avez choisis September !")
        scoreChanson3 = input ("Quel est votre score sur cette chanson ? ")
        if (scoreChanson3 > scoreMinimal):
            score = scoreChanson3
        while (scoreChanson3 < scoreMinimal) :
            print(nomJoueur, ", votre score n'est pas valable, veuillez entrer un autre score !")
        if (scoreChanson3 >= scoreMaximal) :
            score = scoreChanson3
        print(nomJoueur, ", votre score est de ", scoreChanson3, "/100 ! sur September")
    if (choixChanson == 4) :
        print("Vous avez choisis Don't wanna fall in love !")
        scoreChanson4 = input ("Quel est votre score sur cette chanson ? ")
        if (scoreChanson4 > scoreMinimal):
            score = scoreChanson4
        while (scoreChanson4 < scoreMinimal) :
            print(nomJoueur, ", votre score n'est pas valable, veuillez entrer un autre score !")
        if (scoreChanson4 >= scoreMaximal) :
            score = scoreChanson4
        print(nomJoueur, ", votre score est de ", scoreChanson4, "/100 ! sur Don't wanna fall in love")
    if (choixChanson == 5) :
        print("Vous avez choisis Easy Lover !")
        scoreChanson5 = input ("Quel est votre score sur cette chanson ? ")
        if ( scoreChanson5 > scoreMinimal):
            score =  scoreChanson5
        while ( scoreChanson5 < scoreMinimal) :
            print(nomJoueur, ", votre score n'est pas valable, veuillez entrer un autre score !")
        if ( scoreChanson5 >= scoreMaximal) :
            score =  scoreChanson5
        print(nomJoueur, ", votre score est de ",  scoreChanson5, "/100 ! sur Easy Lover")

scoreDonne = int(input("Quel est votre score ? (Minimum 50 et Maximum 100) "))



joueur1 = Player (nomJoueur, scoreDonne)
joueur2 = Player (nomJoueur, scoreDonne)
joueur3 = Player (nomJoueur, scoreDonne)
joueur4 = Player (nomJoueur, scoreDonne)
nombreJoueur = {1:joueur1, 2:joueur2, 3:joueur3, 4:joueur4}

print("Voici les scores sur les musiques :")
print(scoreChanson1, "/100 sur Feeling Good !")
print(scoreChanson2, "/100 sur Relight my Fire !")
print(scoreChanson3, "/100 sur September !")
print(scoreChanson4, "/100 sur Don't wanna fall in love !")
print(scoreChanson5, "/100 sur Easy Lover !")

print("Merci et à bientôt !!")