import random

notes = [0,1,2,3,4,5,6,7,8,9,10]

for i in range(11):
    notes [i] = random.randint(1,10)
    print(notes [i], end=" ")
    
print("\n")

changement1 = int(input("Quel nombre voulez-vous permutter ? \n"))
changement2 = int(input("Quel est le nombre qui va permutter ? \n"))

change = notes [changement1]
notes [changement1] = notes [changement2]
notes [changement2] = change

print(notes)
input()