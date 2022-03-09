Pv_Ennemi = 100
Pv_Joueur = 100
Armure_Monstre = 5
attaque_Joueur = int(input("Combien de dégats faites-vous ?"))
resistance_Monstre = (20 * attaque_Joueur / 100) 
pv_Ennemi = (Pv_Ennemi - resistance_Monstre + armure_Monstre)
print("L'Ennemi a encore", Pv_Ennemi, "point de vie ! Revenez avec un plus haut niveau...")
input()