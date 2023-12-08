# ---------- Slicing -----------

lista = [1, 2, 3, 4, 5, 6, 7]

print(lista[4]) # skriver ut värde som har index 4 
print(lista[2:4]) # skriver värde som har index 2 & 4. # Skriver ej ut resten av listan.

tuppel = (0, 1, 2, 3, 4, 5)
print(tuppel[3:6]) # -"- ?

print(lista[::-1]) # returns lista baklänges 
print("------------\n")

sträng = "Hello world!"
print(sträng[6:11]) # skriver ut ordet 'world'
print(sträng[4:]) #börjar på index 6 och tar med resten av strängen
print(sträng[::-2]) # reverse str med 2 hopp

print("------------\n")
# ---------- .format -----------
sträng_måsvingar = "1:a argumentet: {}, 2: argumentet {},  3:dje argumentet: {}."
print(sträng_måsvingar.format("Banan", "Jordgubb", "protein pulver"))

lista = ["vatten", "eld", "jord"]
print(sträng_måsvingar.format(*lista))  # packar upp alla värden i listan 

