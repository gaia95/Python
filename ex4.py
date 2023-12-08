# Variabler och namn 
# Cars är ett namn på en variabel, här sparas data. 

cars = 100 
space_in_a_car = 4.0
drivers = 30
passengers = 90 
cars_not_driven = cars - drivers # subtraherar värdet i "cars" med värdet i "drivers" -> får bilar som ej körs
cars_driven = drivers # Variabel sparar en annan variabel som innehåller information 

carpool_capacity = cars_driven * space_in_a_car # Antal platser 
average_passenger_per_car = passengers / cars_driven # Hur många som får plats i respektive bil 

print("There are only", cars, "cars available")
print("There are only", drivers, "drivers available.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")