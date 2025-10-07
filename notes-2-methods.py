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

# ask the custom if they want fries
fries_reply = input("Do you want fries?") # "yes!"

if "yes" in fries_reply.lower():
	print("Here are your fries.")
else:
	print("you will no have fries.")
