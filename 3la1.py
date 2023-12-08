# funktioner
def question(info, text1, text2, text3, correct): # 5 parametrar som är argumentvariablar, ska få argument tilldelade. 
    print(info)
    print("1.", text1)
    print("2.", text2)
    print("3.", text3)
    print("Svara med korrekt siffra: ")

    svar = int(input()) # spelaren svara med med en siffra
    if correct == svar:
        print("Rätt!")
    else: print("Fel!")   

question("När skapades Python?", "1800-talet", "1991", "1929", 2) # Dessa är värden , även argument som sparas i variablarna som deklarerades innan.
