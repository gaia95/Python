# Try / Except
print("Skriv din ålder: ")
inmat = input()
try:
    ålder = int(inmat)
    print("Din ålder är: ", ålder)
except ValueError as err:
    print(err) # om något annat än en int skrivs in
print("Tack för ditt svar!")
print("-------------------------------------")
# -------------------------------------

success = False

while not success:
    print("Vad är din ålder?: ") # försöker på nytt tills användare skriver in heltal
    x = input()

    try: 
        age = int(x) # users input
        print("Din ålder är: ", age) 
        success = True

    except ValueError as err:
        print("Du angav inte ett heltal!")


    
