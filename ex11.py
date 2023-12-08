
print("What's your name?", end=' ')
name = input() # saves user name
print("How old are you?", end=' ') # writes out as a question to user, quotation to make space 
age = input() 
print("How tall are you?", end=' ')
height = input()  
print("How much do you weigh?", end=' ') # end makes space at the end
weight = input() 

# Curly braces are used with f-strings.

print(f"So your name is {name}, you're {age} years old, {height} tall and weigh {weight}.") 
y_n = input("Did i get anything wrong? ")

if (y_n != "yes"):
    print("Sorry, restart and try again.")
 