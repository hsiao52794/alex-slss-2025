# (String) methods
# Author: Alex
# Oct 6 2025

"""
Write a McDonald's bot that asks if you want fries with your meal.
Call it work-mcdobot.py .
It should accept Yes/yes or No/no as inputs, and reply
appropriately depending on the answer.
If the user inputs anything else, it should repeat back their answer
and say that it does not understand.
"""

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
