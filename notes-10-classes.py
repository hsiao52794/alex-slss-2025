# Author: Alex
# 11 December

import random

class Pokemon:
    def __init__(self):
        """Constructor"""
        self.name = ""
        self.type = "normal"
        self.level = 1
        self.age = 0
        self.species = ""
        # 1 in 4096
        if random.randint(0, 4096):
            self.is_shiny = False
        else:
            self.is_shiny = False
            print("this pokemon is shiny")
        print("A pokemon is born!!")

    def talk(self):
        """Hear what the pokemon has to say
        The pokemon says its species name"""
        print(f"{self.name} says, \"{self.species}\".")

    def stats(self):
        """Display the stats of the pokemon"""
        space = "-" * (22 - len(self.species))
        print(f"----({self.species}){space}")
        print(f"    Name:  {self.name}")
        print(f"    Type:  {self.type}")
        print(f"    Age:   {self.age}")
        print(f"    Level: {self.level}")
        print("----------------------------")

    def dance(self):
        print(f"{self.name} is dancing...")
        print("✨")

class Mew(Pokemon):
    def __init__(self):
        # call the constructor of the parent class
        super().__init__()
        self.name = "Mew"
        self.type = "Psychic"
        self.species = "Mew"
        self.level = 1
        self.age = 0


if __name__ == "__main__":
    # create a pokemon obj
    pokemon_one = Pokemon()
    # access pokemon properties
    print("Pokemon name: ", pokemon_one.name)
    # change pokemon properties
    pokemon_one.name = "Gary"
    pokemon_one.species = "Pikachu"
    print("Pokemon name: ", pokemon_one.name)
    # create another pokemon
    pokemon_two = Pokemon()
    pokemon_two.name = "Pikachu"
    pokemon_two.species = "Pikachu"
    # check to see if a value is a pokemon
    if pokemon_one == pokemon_two:
        print("They are the same.")
    else:
        print("They're individual pokemon.")

    if type(pokemon_one) is Pokemon:
        print(f"{pokemon_one.name} is a Pokemon.")

    # Tell our pokemon to talk
    pokemon_one.talk()
    pokemon_two.talk()
    # Display stats of pokemon_one
    pokemon_one.stats()
    pokemon_two.stats()
    # Create a Mew object
    pokemon_three = Mew()
    pokemon_three.stats()
