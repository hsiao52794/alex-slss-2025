# (String) methods
# Author: Alex
# Oct 6 2025

# ask for weather

weather = input("what's the weather like today")

if weather.lower().strip("!").strip(".") == "rainy":
    # rainy, RAINY, RAiny
    # Rainy!
    print("You should bring an unbrella")
else:
    print("I see")
