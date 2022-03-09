from colorama import init, Fore, Style, Back
from colorama.initialise import reset_all
init()

print (Fore.BLACK, Back.YELLOW + "Bienvenue sur ce jeu de MOTUS ! Vous avez 8 tentatives pour trouver le mot mystère ! Bonne chance !", Style.RESET_ALL)
print("Instructions : Si la lettre est" , Fore.RED + "ROUGE", Style.RESET_ALL,", elle est à la bonne place. Si la lettre est", Fore.YELLOW + "JAUNE", Style.RESET_ALL,", elle est présente mais pas à la bonne place. Si la lettre est", Fore.BLUE + "BLEUE", Style.RESET_ALL, ", cette lettre n'est pas présente dans le mot.")
import random

mots = ["Aboyez", "Castor", "Cheval", "Balcon", "Girafe", "Calins", "Defait", "Otarie", "Renard", "Oursin"]
choix = random.choice (mots)
taille_mot = [0]
mot_choisis = " "
taille_mot = (len(choix))
tentatives = 8
mot_choisis = taille_mot * "_"
print(mot_choisis)
mot_joueur = [" "]

while tentatives != 0 :

    lettre_1 = input("Choisissez une première lettre : ")
    lettre_2 = input("Choisissez une deuxième : ")
    lettre_3 = input("Choisissez une troisième : ")
    lettre_4 = input("Choisissez une quatrième : ")
    lettre_5 = input("Choisissez une cinquième : ")
    lettre_6 = input("Choisissez une dernière : ")
    mot_joueur = [lettre_1, lettre_2, lettre_3, lettre_4, lettre_5, lettre_6]

    if mot_joueur == mot_choisis :
        print(Fore.RED + mot_joueur)
        print("Vous avez Gagné !!")

    if lettre_1 == choix [1] :
            print(Fore.RED + lettre_1)
            print(Style.RESET_ALL + "Cette lettre est à la bonne place !")
            print(mot_choisis)
            tentatives = tentatives - 1
            print("Il vous reste ", tentatives, "tentatives !")
        
    if lettre_1 != choix [1] :
            print(Fore.BLUE + lettre_1)
            print (Style.RESET_ALL + "Cette lettre n'est pas dans le mot !")
            tentatives = tentatives - 1
            print("Il vous reste ", tentatives, "tentatives !")

    if lettre_2 == choix [2] :
            print(Fore.RED + lettre_1)
            print(Style.RESET_ALL + "Cette lettre est à la bonne place !")
            print(mot_choisis)
            tentatives = tentatives - 1
            print("Il vous reste ", tentatives, "tentatives !")
        
    if lettre_2 != choix [2] :
            print(Fore.BLUE + lettre_1)
            print (Style.RESET_ALL + "Cette lettre n'est pas dans le mot !")
            tentatives = tentatives - 1
            print("Il vous reste ", tentatives, "tentatives !")

    if lettre_3 == choix [3] :
            print(Fore.RED + lettre_1)
            print(Style.RESET_ALL + "Cette lettre est à la bonne place !")
            print(mot_choisis)
            tentatives = tentatives - 1
            print("Il vous reste ", tentatives, "tentatives !")
        
    if lettre_3 != choix [3] :
            print(Fore.BLUE + lettre_1)
            print (Style.RESET_ALL + "Cette lettre n'est pas dans le mot !")
            tentatives = tentatives - 1
            print("Il vous reste ", tentatives, "tentatives !")

    if lettre_4 == choix [4] :
            print(Fore.RED + lettre_1)
            print(Style.RESET_ALL + "Cette lettre est à la bonne place !")
            print(mot_choisis)
            tentatives = tentatives - 1
            print("Il vous reste ", tentatives, "tentatives !")
        
    if lettre_4 != choix [4] :
            print(Fore.BLUE + lettre_1)
            print (Style.RESET_ALL + "Cette lettre n'est pas dans le mot !")
            tentatives = tentatives - 1
            print("Il vous reste ", tentatives, "tentatives !")

    if lettre_5 == choix [5] :
            print(Fore.RED + lettre_1)
            print(Style.RESET_ALL + "Cette lettre est à la bonne place !")
            print(mot_choisis)
            tentatives = tentatives - 1
            print("Il vous reste ", tentatives, "tentatives !")
        
    if lettre_5 != choix [5] :
            print(Fore.BLUE + lettre_1)
            print (Style.RESET_ALL + "Cette lettre n'est pas dans le mot !")
            tentatives = tentatives - 1
            print("Il vous reste ", tentatives, "tentatives !")

    if lettre_6 == choix [6] :
            print(Fore.RED + lettre_1)
            print(Style.RESET_ALL + "Cette lettre est à la bonne place !")
            print(mot_choisis)
            tentatives = tentatives - 1
            print("Il vous reste ", tentatives, "tentatives !")
        
    if lettre_6 != choix [6] :
            print(Fore.BLUE + lettre_1)
            print (Style.RESET_ALL + "Cette lettre n'est pas dans le mot !")
            tentatives = tentatives - 1
            print("Il vous reste ", tentatives, "tentatives !")

if  tentatives == 0 :
    print("Vous avez Perdu !!")
