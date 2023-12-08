# Slica strängat 

print("Längd på sträng:", len("Hello world!")) # Skriver ut antalet tecken/bokstäver i strängen

sträng = "Goddag!"
print(sträng[2]) # skriver ut bokstav som har index 2
print(sträng[5])
print(sträng[6])

print(sträng[0:5]) # slicear ut "Godda" från "Goddag!" (index: 0,1,2,3,4,5,6)
print(sträng[2:6]) #slicear ut bokstäverna "ddag" från "Goddag!" (index: 2,3,4,5,6)

# ---------------------------------

print("Märiem".isalpha()) # if string has alphabethic letters -> ger värde true
print("Meriem".isalpha())
print("Meriem Mohammed".isalpha()) # if not -> ger värde false (mellanslag räknas som not)

# ---------------------------------
print("--------------------------------")

print(" ".isspace()) # kollar efter mellanslag -> värde True
print("\t".isspace()) # tabbar räknas som space
print("\n".isspace()) # newline är räknas också som space

sträng = "Meriem\n\t Mohammed"
print(sträng)
print("Meriem\n\tMohammed".isspace()) 

print(sträng.find("oham")) # returnerar start index

print(sträng[::-1]) # skriver allt baklänges med ett hopp
print(sträng[::-2]) # baklänges med 2 hopp

palindrom = "Vargrav"
print(palindrom[::-1])
