blanc = 0

nombre = int(input("Un damier de combien de côté ? : "))
taille = int(input("Les cases de combien de côté ? : "))

for i in range (0,nombre):#le damier fait x case de haut (nombre de ligne)
    if blanc == 0: #le damier commence par une case noir
        for i in range (0,taille): #la case fait y de haut
            blanc1 = 0 #la ligne commence par la case noir
            for i in range (0,nombre): #le damier fait x case de long (nombre de colonne)
                if blanc1 == 0:
                    for i in range (0,taille):#la case noir fait y de long
                        print('* ',end='')
                    blanc1 =1 #la case noir est finie d'être afficher, la prochaine case sera blanche
                else:
                    for i in range (0,taille):#la case blanche fait y de long
                        print('  ',end='')
                    blanc1 = 0#la case blanche est finie d'être afficher, la prochaine case sera noir
            print()#la ligne est finie
        blanc = 1
    else:
        for i in range (0,taille):
            blanc1 = 0
            for i in range (0,nombre):
                if blanc1 == 0:
                    for i in range (0,taille):
                        print('  ',end='')
                    blanc1 =1
                else:
                    for i in range (0,taille):
                        print('* ',end='')
                    blanc1 = 0
            print()
        blanc = 0
input()