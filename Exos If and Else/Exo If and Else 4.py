Pv_Ennemi = 100
Armure_Monstre = 5
Attaque_Joueur = int(input("Combien de dégats faites-vous ? : "))
if (Attaque_Joueur <= 5) :
    Attaque_Joueur = 0
    print ("L'armure du Monstre absorbe les dégats !")
if (Attaque_Joueur == 100) :
    print ("Félicitations ! Vous avez tué le Monstre !")
else : 
    Pv_Ennemi = (Pv_Ennemi - Attaque_Joueur + Armure_Monstre)
    print("L'Ennemi a maintenant", Pv_Ennemi, "point de vie ! Encore un effort !")
input()