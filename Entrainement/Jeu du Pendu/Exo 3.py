import random
mots = ["minecraft", "skyrim", "halo", ""]
choix = random.choice (mots)
taille_mot = [0]
mot_choisis = " "
lettre_propose = [" "]
taille_mot = (len(choix))
mot_choisis = taille_mot * "*"

print ("Bienvenue dans ce jeu du pendu ! Vous devrez deviner le nom d'un jeux vidéo connu ! C'est partit !")
print (mot_choisis)

lettre = input('Entrez une lettre : ')
if lettre in choix :
    print ("Cette lettre est présente dans le mot !")
if lettre not in choix :
    print("Cette lettre n'est pas dans le mot !")

