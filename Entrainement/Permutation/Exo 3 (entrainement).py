tableau = [12,25,36,10,21]
taille = len(tableau)
minimal = tableau[2]
print (minimal)
indice = 0
print(tableau)

for i in range(2 , 5):
    if (tableau[i] < minimal) :
        minimal = tableau[i]
        indice = i

print(indice)
print("L'indice le plus petit va permutter avec le premier indice : \n")

change = tableau [0]
i = tableau [0]
tableau [0] = change

print(tableau)