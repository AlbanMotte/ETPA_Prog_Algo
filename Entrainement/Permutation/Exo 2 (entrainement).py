tableau = [12,25,36,12,21]
taille = len(tableau)
minimal = tableau[2]
print (minimal)
indice = 0

for i in range(2 , 5):
    if (tableau[i] < minimal) :
        minimal = tableau[i]
        indice = i
print(indice)