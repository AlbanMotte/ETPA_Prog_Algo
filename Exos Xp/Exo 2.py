nb_Experience_Joueur = int(input("Quelle quantité d'Xp avez-vous ? : "))
niveau_Actuel = 11
niveau_Calcul = int((niveau_Actuel + nb_Experience_Joueur / 100))
print("Vous êtes actuellement niveau", niveau_Calcul, "Bravo !")
input()