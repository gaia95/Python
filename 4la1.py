# If och Else satser

age = int(input("How old are you? ")) # Gör om input till integer

if age > 90:
    print("You are too old to party, granny.")
elif age < 0:
    print("You are yet to be born????")
elif age >= 18:
    print("Welcome to the party!")
else: 
    print("You're too young to party.")