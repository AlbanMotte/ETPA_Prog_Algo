grille =[1,2,3,4,5,6,7,8,9]

symbole_joueur1 = 1
symbole_joueur2 = 2

print(grille[0],"|", grille[1],"|", grille[2])
print("----------")
print(grille[3],"|", grille[4],"|", grille[5])
print("----------")
print(grille[6],"|", grille[7],"|", grille[8])

print("Joueur 1, Quel symbole voulez-vous jouer ?")
choix = input("X ou O ? ")

if choix == "X" :
    symbole_joueur1 = "X"
    symbole_joueur2 = "O"
else :
    symbole_joueur1 = "O"
    symbole_joueur2 = "X"


print ("Joueur 1 =", symbole_joueur1)
print ("Joueur 2 =", symbole_joueur2)

def play(grille):                                                                                                         
    while True:                                                      
        rang = input("entrez le numéro de votre rang: ")                 
        while not rang.isdigit() or int(rang) < 1 or int(rang) > 3:     
                                                                        
            rang = input("Entrez un rang entre 1-3: ")                  
        rang = int(rang)                                                
        col = input("Entrez le numéro de votre colonne: ")               
        while not col.isdigit() or int(col) < 1 or int(col) > 3:       
            col = input("Entrez une colonne entre 1-3: ")                
        col = int(col)                                                   
        if grille[rang-1][col-1] != " ":                                
            print("Choisissez un emplacement vide !")                    
        else:                                                           
            return (rang-1, col-1)  
input()