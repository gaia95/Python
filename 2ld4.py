# Listor, loopar, random funktion 

import random
import random as rm # assigning a variable for function random, makes code more compact
from random import choice 

lista_heltal = [0,1,2,3,4,5,7]

for heltal in lista_heltal: # går igenom alla "objekt" i listan och skriver sedan ut
    print(heltal)
print("------")

lista_strängar = ["Tjaba", "Tjena", "Hallå"]


for sträng in lista_strängar: 
    print(sträng)
print("------")

from random import choice 
lista = ["Vi", "Säger", "Så"]
print (choice(lista)) # väljer ett random värde och skriver ut värden slumpmässigt.

print("------")

lista_blandad = ["Först", 5, True, 2.5, "Sist"]
for item in lista_blandad:
    print(f"Item var av typ: {type(item)} med värdet: {item}")

lista3 = ["1", "5", "7"]

print("------")

print(random.choice(lista3)) # skriver ut slumpmässigt element från lista
print(rm)

