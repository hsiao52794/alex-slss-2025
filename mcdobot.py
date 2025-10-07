# (String) methods
# Author: Alex
# Oct 6 2025

print("Hi")
print("What would you like for today?")
meal = str(input(": "))

a = 1
while meal.lower().strip(".") != ("no"):
    print(f"OK, a {meal}")
    if a > 0:
        print("would you like to add a fries?")
        fries = input(": ")
        a = a-1
    print("Anything else?")
    meal = input(": " )
