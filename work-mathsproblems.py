def age():
    age = int(input("how old are you?: "))
    age += 24
    print(f"you will be {age} years old in 2049")

def avg():
    avg = 0
    for num in ["1", "2", "3", "4", "5"]:
        score = int(input(f"judge {num}: "))
        avg += score
    avg /= 5
    print(f"your olympis score is {avg}")

def mc():
    burger = 0
    fries = 0
    total = 0
    print("would you like a burger for $5? (yes/no)")
    burger = input(" ").lower().strip(",.?! ")
    print("would you like fries for $3? (yes/no)")
    fries = input(" ").lower().strip(",.?! ")
    if burger == ("yes"):
        total += 5
    if fries == ("yes"):
        total += 3
    total *= 1.14
    print(f"your total is {total}")

def main():
    pass

if __name__ == "__main__":
    main()
