saisie=int(input("Saisir votre nombre d'etoiles entre 1 et 10 : "))
j=0
etape = 0
while j < saisie :
    if(saisie < 11 and saisie > 0 and etape == 0) :
        for i in range(saisie) :
            print("*", end=" ")
        print("")
        etape = 1
        j=j+1
    elif(saisie < 11 and saisie > 0) :
        for l in range(saisie-2) :
            print("*", end=" ");
            for k in range(saisie-2) :
                print(" ", end=" ")
            print("*")
            j=j+1
        etape = 0 
input()