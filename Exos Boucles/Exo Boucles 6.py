saisie=int(input("Saisir votre nombre d'etoiles entre 1 et 10 : "))
j=0
damier = 0
etape = 1
e = 0
for e in range(saisie) :
    for d in range(saisie) :
        j=0
        while j < saisie :
            for i in range(int(saisie/2)) : 
                if damier == 0 and etape == 1:
                    for i in range(saisie) :
                        print("*", end=" ")
                    print("", end="")
                    damier = 1
                    etape = 0
                elif damier == 1 and etape == 1 :
                    for i in range(saisie) :
                        print(" ", end=" ")
                    print("", end="")
                    damier = 0
                    etape = 0
                if etape == 0 and damier == 0 :
                    for i in range(saisie) :
                        print("*", end=" ")
                    print("", end="")
                    damier = 1
                    etape = 1
                else :
                    for i in range(saisie) :
                        print(" ", end=" ")
                    print("", end="")
                    damier = 0
                    etape = 1
            j=j+saisie
        print("")
    if etape == 0 :
        etape = 1 
    elif etape == 1 :
        etape = 0
input()