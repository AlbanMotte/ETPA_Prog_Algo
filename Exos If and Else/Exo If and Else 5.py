import random
chiffre = random.randint(1,100)
nb_utilisateur = int(input("Choisissez un nombre :"))
if nb_utilisateur < chiffre : print("Votre nombre est plus petit")
elif nb_utilisateur > chiffre : print("Votre nombre est plus grand")
else : print("Vous avez le même nombre !")
input()