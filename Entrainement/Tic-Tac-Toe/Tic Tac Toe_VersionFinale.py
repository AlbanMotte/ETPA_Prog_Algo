def afficheGrille (tableau):
    for i in range (0,9,3):
        print(tableau[i], tableau[i+1], tableau[i+2])

#Comment créer la grille (prog du haut)

def ajouteSymbole (tableau,numérodetour):
    caseDispo = False
    while (not caseDispo):
        numéroCase = int(input("Choisissez une case (de 0 à 8 ): "))
        if (tableau[numéroCase]!="X" and tableau[numéroCase]!="O"):
            caseDispo= True

    symboleCourant = ""
    if (numérodetour %2==1):
        symboleCourant = "X"
    else:
        symboleCourant = "O"
    tableau[numéroCase] = symboleCourant

def testeVictoireHorizontale(tableau) :
        for i in range (0,9,3):
            if (tableau[i] == tableau[i+1] == tableau[i+2]) :
                if(tableau[i] =="X" or tableau[i] =="O"):
                    return True
        return False

def testeVictoireVerticale(tableau) :
        for i in range (0,3):
            if (tableau[i] == tableau[i+3] == tableau[i+6]) :
                if(tableau[i] =="X" or tableau[i] =="O"):
                    return True
        return False

def testeVictoireDiagonale(tableau) :
        if(tableau[4] =="X" or tableau[4] =="O"):
            if (tableau[0] == tableau[4] == tableau[8]) :
                return True
            elif (tableau[2] == tableau[4] == tableau[6]) :
                return True
        return False

grille = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
victoire = False
tour = 0
while ((not victoire) and tour<9) :
    tour+=1
    afficheGrille(grille)
    ajouteSymbole(grille, tour)
    victoire = testeVictoireHorizontale(grille) or testeVictoireVerticale(grille) or testeVictoireDiagonale(grille)

afficheGrille(grille)

if(victoire) :
    print("Victoire !")
else : print("Oh... C'est Grillé !")