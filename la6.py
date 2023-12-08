# ascii table. Stora bokstäver
for x in range(65, 91): # inklusive 65, exclusive 91
    print(chr(x)) # skriver ut allt

# små bokstäver
for x in range(97, 123): 
    print(chr(x))

# skriver ut alla tecken i ascii

for x in range(256): # range börjar på 0 om man bara har ett argument.
    print(chr(x)+ " " + str(x)) 

    