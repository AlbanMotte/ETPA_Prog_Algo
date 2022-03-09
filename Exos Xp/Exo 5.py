pv_Ennemi = 100
pv_Joueur = 100
attaque_Joueur = int(input("Combien de dégats faites-vous ?"))
resistance_Monstre = (20 * attaque_Joueur / 100) 
pv_Ennemi = (pv_Ennemi - resistance_Monstre)
print("L'ennemi a maintenant", pv_Ennemi, "point de vie ! Encore un effort !")