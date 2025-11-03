print("input three number")
num_one = float(input("1: "))
num_two = float(input("2: "))
num_three = float(input("3: "))
average = float(num_one + num_two + num_three)/3
print(average)

name = input("name: ")
mood = input("mood: ")
if mood.lower().strip("!").strip(".") == "happy":
    print(f"Hey {name}, great to see you smiling!")
elif mood.lower().strip("!").strip(".") == "sad":
    print(f"I hope your day gets better, {name}.")
elif mood.lower().strip("!").strip(".") == "neutral":
    print(f"Sometimes you have average days, {name}.")
else:
    print(f"Hi {name}, hope you're having a good day.")
