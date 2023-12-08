# Klasser , Fordon
# Self representerar ett objekt i en klass.

class fordon:
    def __init__(self, märke, hastighet, färg, modell, sittplatser, hjul):
        self.märke = märke
        self.hastighet = hastighet
        self.färg = färg
        self.modell = modell
        self.sittplatser = sittplatser
        self.hjul = hjul

# När ett objekt skapats och fått argument kommer de retuneras i denna sträng;
    def __str__(self):
        return f"{self.märke}{self.hastighet}{self.färg}{self.modell}{self.sittplatser}{self.hjul}"
         


class bil(fordon): # ärver metoder från klass fordon 
    def __init__(self, märke, hastighet, färg, modell, sittplatser, bagage):
        super().__init__(märke, hastighet, färg, modell, sittplatser, 4) #anropar super klass. 4 = default värde för hjul
        self.sidoSpeglar = 2
        self.bagage = bagage
    
    def __str__(self):
        ss = super().__str__()
        return f"{ss}{self.bagage}"

class motorcykel(fordon):
    def __init__(self, märke, hastighet, färg, modell):
        super().__init__(märke, hastighet, färg, modell, 1, 2) # 1 = sittplats 2 = hjul
        self.sidoSpeglar = 2

class volvo(bil):
    def __init__(self, färg):
        super().__init__("Volvo, ", f',{180}, ', färg, ", V60, ", 5, 400)

m1 = motorcykel("Honda, ", f'speed:{300} ', f"Färg: Blå, ", "Modell: Shadow") # motorcykel objekt
b1 = bil("Volvo, ", 250, ", Svart, ", "2010, ", 5, 300) # bil objekt
m1.hjul = 3 # nytt värde, ändrar antal hjul för motorcykeln (default 2 hjul)
vol60 = volvo ("Gul")

print(m1,"\n",b1,"\n",vol60)
