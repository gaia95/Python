# Add a prompt and input for user 

def add(a, b):
    print(f'ADDING: {a} + {b}')
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING: {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING: {a} * {b}")
    return a * b

def divide(a , b):
    print(f"DIVIDING: {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add (30 , 5) # argument för funktionens parametrar
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ:{iq}")

print("\nHere is a puzzle: \n")
# A puzzle form the extra credit, type it anyway 

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

