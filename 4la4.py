# Klasser och Subklasser
#----------- Rektangel & Kvadrat ------------------------ #

class rektangel:

    def __init__(self, bredd_parameter, höjd_parameter): # Self är viktig parameter. Används för att kunna access variabler som tillhör en klass.

        self.bredd = bredd_parameter
        self.höjd = höjd_parameter

    def area(self):
        return  self.bredd * self.höjd

    def omkrets(self):
        return self.bredd * 2 + self.höjd * 2

# ----------- Kvadrat ------------------------ #

class kvadrat(rektangel): # Ärver metoder från föräldrar klass, gör kod mer kompakt och slipper upprepningar
    
    def __init__(self, sida): # 1 inparameter, förväntar sig ett argument senare
        super().__init__(sida, sida)
       

r1 = rektangel(10, 25) # Argumenten är sido bredd och höjd
k = kvadrat(5)

print("Rektagel:")
print(f"Area: {r1.area()}") # area 250
print(f"Omkrets: {r1.omkrets()} ") # omkr 70

print("Kvadrat:")
print(f"Area: {k.area()}")
print(f"Omkrets: {k.omkrets()}")

