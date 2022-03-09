Tableau = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def afficheGrille(Tableau):
    return Tableau

for i in range (3) :
        print ("|".join(Tableau[(i*3):(i*3+3)]))

input()