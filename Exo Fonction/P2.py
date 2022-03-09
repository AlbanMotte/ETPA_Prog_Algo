Tableau = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def afficheGrille(Tableau):
    return Tableau

def ajouteSymbole(Tableau) :
    print(Tableau)

print("Le joueur qui choisit X commence !")
Symbole = input("Quel symbole choisissez-vous ? ")
case = int(input("Joueur X, rentrer le numéro de la case où vous voulez jouer : "))


if Tableau[case] != Symbole :
    Tableau[case] = Symbole
    afficheGrille
else : print("Vous ne pouvez pas jouer sur cette case !")

for i in range (3) :
        print ("|".join(Tableau[(i*3):(i*3+3)]))

input()