# Printing med implementation av funktioner

from logging import Formatter # Importerar existerande funktion vars kod kan användas 

formatter = "{} {} {} {}" # Deklarerar en variabel, hämtar textsträngar

print(formatter.format(1,2,3,4)) # Nya värden som sparas i hinken 
print(formatter.format("one, ", "two, ", "three, ","four")) # ?radera värden i hinken och lägger till nya ?
print(formatter.format(True , False , False , True)) 

# print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(
    "I love ",
    "chocolate ", 
    "and hate insects ",
    "drink your water"
))