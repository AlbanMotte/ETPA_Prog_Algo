import random

notes = [0,1,2,3,4,5,6,7,8,9,10]

for i in range(11):
    notes [i] = random.randint(1,10)
    print(notes [i], end=" ") 
input()