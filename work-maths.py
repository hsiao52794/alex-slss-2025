# calculate the interior angle of a regular polygon

def angle():
    print("how many sides does the polygon have?")
    sides = int(input("sides: "))
    angle = 180-(360/sides)
    print(f"angle: {angle}")

def area():
    import math
    print("how many sides does the polygon have?")
    sides = int(input("sides: "))
    print("how long is each side?")
    side_length = int(input("side length: "))
    angle = (180-(360/sides))/2
    area = (side_length / 2) * sides * (((side_length / 2) / math.sin((360 / sides) / 2) * math.sin(angle)))
    print(f"area: {area}")

def main():
    area()

if __name__ == "__main__":
    main()
