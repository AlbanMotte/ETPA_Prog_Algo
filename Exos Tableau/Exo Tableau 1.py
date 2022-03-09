notes = [0,1,2,3]
première_note = int(input("Quelle est votre première note ? \n"))
notes [0] = première_note

deuxième_note = int(input("Quelle est votre deuxième note ? \n"))
notes [1] = deuxième_note

troisième_note = int(input("Quelle est votre troisième note ? \n"))
notes [2] = troisième_note

dernière_note = int(input("Quelle est votre dernière note ? \n"))
notes [3] = dernière_note

print(notes)

moyenne = (notes[0]+notes[1]+notes[2]+notes[3])/4
print("Votre moyenne est de", moyenne, "!")

input()