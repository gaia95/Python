from time import sleep

text = "Hejhej jag vill hem."

def wrt(): # wait and return 
    sleep(5) # väntar i 5 sec innan den return nästa mening
    return "Jag vill också hem."

print(text, "Nu kör vi!\n")
print("..\n", wrt())
print("Hemmåt!")