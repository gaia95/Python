# KLASSER 

class Person:
    def __init__(self, fn, en, pnr):
        self.förnamn = fn # namnet efter self är variabel namn som tilldelas värde 
        self.efternamn = en 
        self.personnummer = pnr

    def __str__(self):
        return f"{self.förnamn}{self.efternamn}{self.personnummer}"

class Lärare(Person): 
    def __init__(self, förnamn, efternamn, personnummer, lön):
        super().__init__(förnamn, efternamn,personnummer)
        self.lön = lön 

    def __str__(self):
        return f'{super().__str__()} {self.lön}'

class Student(Person):
    
    def __init__(self, förnamn, efternamn, personnummer, betyg): # self är ett objekt, fn = förnamn, en = efternamn 
        super().__init__(förnamn, efternamn, personnummer)
        self.betyg = betyg
      
    def __str__(self):
        return f'{super().__str__()} {self.betyg}'

elev1 = Student("Meriem, ", "Mohammed, ", 891243-5647, ", MVG")
elev2 = Student("Mimmi, ", "Tesfa, ", 903783-4939, ", VG")
lärare = Lärare("Maria, ", "Gunnarson, ", 503783-4939, ", 35000")

print(elev1)
print(elev2)
print(lärare)

       

