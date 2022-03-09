tableau = [12,5,36,28,30]
taille = len(tableau)
minimal = tableau[0]
print (minimal)

for i in range(taille):
    if (tableau[i] < minimal) :
        minimal = tableau[i]
        indice = i
print(indice)
