tableau = [45, 23, 34, 13, 19]
taille = len(tableau)
minimal = tableau[0]
print ("Vous aller voir un tableau, le tableau suivant sera rangé dans l'ordre croissant :", tableau)

for i in range(taille):
    if (tableau[i] < minimal) :
        minimal = tableau[i]
        indice = i



print("Voici le tableau rangé dans l'ordre croissant :", indice)