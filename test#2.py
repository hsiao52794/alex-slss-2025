size = int(input("size: "))
repeat = int(input("repeat: "))
sides = int(input("sides(sides>=3): "))

def all_data():
    print(f"ang1: {ang1}")
    print(f"ang2: {ang2}")
    print(f"ang3: {ang3}")
    print(f"L: {L}")
    print(f"L1: {L1}")
    print(f"L2: {L2}")
    print(f"r: {r}")
    print(f"counter: {counter}")

import turtle

window = turtle.Screen()
window.bgcolor("white")

pen1 = turtle.Turtle()
pen1.color("black")
pen1.shape("arrow")
pen1.shapesize(1)
pen1.speed(20)

ang1 = 1

repeat = int((repeat*(360/sides)-1))
pen1.pu()
L = size
for counter in range(repeat):
    ang2 = 180-(360/sides)
    ang3 = 180-(ang2+ang1)
    import math
    L1 = math.sin(math.radians(ang3))*(L/math.sin(math.radians(ang2)))
    L2 = math.sin(math.radians(ang1))*(L/math.sin(math.radians(ang2)))
    r = (L/2)/math.cos(math.radians(ang2/2))
    if (L1 + L2) < L:
        all_data()
        continue
    pen1.forward(r)
    pen1.right(180-(ang2/2))
    pen1.pd()
    for counter in range(sides):
        pen1.forward(L)
        pen1.right(180-ang2)
    pen1.pu()
    pen1.right(ang2/2)
    pen1.forward(r)
    pen1.right(180)
    pen1.right(ang1)
    L = L1 + L2
    ang1 = ang1 + 1
pen1.shapesize(0.01)
turtle.exitonclick()
