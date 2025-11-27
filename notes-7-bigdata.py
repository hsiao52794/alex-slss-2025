# Boilerplate
#

def main():
    path = "data/sfu_best_cmpt120.csv"
    file = open(path)

    line = file.readline()

    # Process the header line
    uncle_fatihs = 0
    pizza_hut = 0
    club_ilia = 0
    for line in file:
        info = line.split(",")
        fave_pizza = info[4]
        if fave_pizza == "Uncle Fatih's":
            uncle_fatihs += 1
        if fave_pizza == "Pizza Hut":
            pizza_hut += 1
        if fave_pizza == "Club Ilia":
            club_ilia += 1

    print(f"Uncle Fatih's: {uncle_fatihs}")
    print(f"Pizza Hut: {pizza_hut}")
    print(f"Club Ilia: {club_ilia}")

    file.close()

if __name__ == "__main__":
    main()
