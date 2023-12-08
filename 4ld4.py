# Modulus, rest division.

def jämnt_tal(tal):
    if tal % 2 == 0: # om talet är jämnt delbart med 2 och har 0 i rest 
        print("Talet var jämnt")
    else:
        print("Talet var udda")

jämnt_tal(12)
jämnt_tal(524)
jämnt_tal(1003)

print("----------------------------")

def delbart_ellerEj(nämnare, täljare):
    if nämnare % täljare == 0: # om talet inte hade rest
        print(f'Talet {nämnare} var jämnt delbart med {täljare}')
    else:
        print(f'Talet {nämnare} var inte jämnt delbart med {täljare}. Resten var {nämnare%täljare}.')

delbart_ellerEj(5, 10) # argument tal 
delbart_ellerEj(22, 11)
delbart_ellerEj(103, 3)

sträng_täljare = input("Skriv en täljare: ")
täljare = int(sträng_täljare)
sträng_nämnare = input("Skriv en nämnare: ")
nämnare = int(sträng_nämnare)

delbart_ellerEj(nämnare, täljare)
