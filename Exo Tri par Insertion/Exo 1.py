tableau = [15,24,37,8,30]
taille = len(tableau)
minimal = tableau[0]
print ("Vous aller voir un tableau, l'indice de son plus petit élément va être renvoyé :", tableau)

for i in range(taille):
    if (tableau[i] < minimal) :
        minimal = tableau[i]
        indice = i
print("L'indice le plus petit est le :", indice)