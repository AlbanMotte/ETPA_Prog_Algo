import random
chiffre = random.randint(1,100)
nb_utilisateur = int(input("Veuillez saisir un nombre :"))
if (nb_utilisateur == chiffre) :
        print ("Bravo nous avons le même nombre !")
        input()
else :
    while nb_utilisateur != chiffre :
        if (nb_utilisateur < chiffre) :
            print("Votre nombre est plus petit")
            input()
            nb_utilisateur = int(input("Veuillez saisir un nombre :"))
        else :
            print("Votre nombre est plus grand")
            input()
            nb_utilisateur = int(input("Veuillez saisir un nombre :"))
input()
