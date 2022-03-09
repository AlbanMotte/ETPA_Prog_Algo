Pv_Ennemi = 100
Pv_Joueur = 100
Armure_Monstre = 5
Attaque_Joueur = int(input("Combien de dégats faites-vous ? "))
Pv_Ennemi = (Pv_Ennemi - Attaque_Joueur + Armure_Monstre)
print("L'ennemi a maintenant: ", Pv_Ennemi, "point de vie ! Saletée d'armure !")

