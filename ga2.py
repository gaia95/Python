def answer_check(players_answer, right_answer):
    if players_answer == right_answer:
        print("\nWOW, du har RÄTT!")
    else:
        print("\nBU, du har FEL!")

print("************************MITT LILLA FRÅGESPEL ******************************\n")
print("""Vad finns det för olika typer av loopar?
1. for och while
2. floor och well
3. four och with\n""")

answer_check(input("Svar: "), "1")

print("""\nHur skriver man en funktion?
1. deph = {'funktionnamn'}
2. däf innit('funktionnamn'):
3. def 'funktionnamn'():""")

answer_check(input("Svar: "), "3") 