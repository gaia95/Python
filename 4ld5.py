siffror = [1, 5, 4, -1, 5, 2, 10] # lista med int värden

for x in siffror:
    if(x == -1): # om x är -1
        break # avbryter vi loopen och allt efter skrivs ej ut
    print(x)

print("------------------------------")

# ----------------------------------

siff = 0 # startvärde 
while(siff < 16): # så läng värdet är mindre än 16

    if siff == 5: # om siffra är 5
        while(True):
            break # avsluta loop
    else:
        print(siff) # annars fortsätt print 
    siff += 1 # och skriv nästa siffra