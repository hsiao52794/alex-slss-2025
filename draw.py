import turtle

print('(Use number 1 to 9 to select options, and press "Enter" to confirm)')
print("(1)circle")
print("(2)circle")
print("(3)spiral")
print("(4)fibonacci")
print("(5)mushroom")
print("(6)city")
select = input(": ")
# just in case the user is stupid
while select != str(1) and select != str(2) and select != str(3) and select != str(4) and select != str(5) and select != str(6):
    print("")
    print("Please choose from the given list")
    print('(Use number 1 to 9 to select the options, and press "Enter" to confirm)')
    select = input(": ")

window = turtle.Screen()
window.bgcolor("white")
speed = 0
import math

if select == str(1):
    size = int(input("size(suggested: 100): "))

    pen1 = turtle.Turtle()
    pen1.color("black")
    pen1.shape("turtle")
    pen1.shapesize(size/50)
    pen1.speed(speed*10)
    #pen1.width(size/10)
    for _ in range(36):
        pen1.right(10)
        pen1.circle(size)
    pen2 = turtle.Turtle()
    pen2.color("black")
    pen2.shape("turtle")
    pen2.shapesize(size/50)
    pen2.speed(speed*10)
    #pen2.width(size/10)
    for _ in range(9):
        pen2.penup()
        pen2.forward(2*size)
        pen2.right(90)
        pen2.pendown()
        pen2.forward(2*size)
        for _ in range(3):
            pen2.right(90)
            pen2.forward(4*size)
        pen2.right(90)
        pen2.forward(2*size)
        # back to center
        pen2.right(90)
        pen2.penup()
        pen2.forward(2*size)
        pen2.pendown()
        pen2.right(-10)

    pen3 = turtle.Turtle()
    pen3.color("black")
    pen3.shape("turtle")
    pen3.shapesize(size/50)
    pen3.speed(speed*10)
    # start
    pen3.penup()
    pen3.right(-45)
    number1 = math.sqrt(2*(size**2))
    pen3.forward(2*number1)
    pen3.left(85)
    # sin 5
    number2 = math.sin(math.radians(5))
    number3 = number2*number1
    pen3.pendown()
    for _ in range(36):
        pen3.left(10)
        pen3.forward(4*number3)
        pen3.circle(4*size)

    pen1.shapesize(0.1)
    pen2.shapesize(0.1)
    pen3.shapesize(0.1)

if select == str(2):
    size = int(input("size(suggested: 50): "))

    pen1 = turtle.Turtle()
    pen1.color("black")
    pen1.shape("turtle")
    pen1.shapesize(size/50)
    pen1.speed(speed*10)
    #pen1.width(size/10)
    for _ in range(36):
        pen1.right(10)
        pen1.circle(size)
    pen3 = turtle.Turtle()
    pen3.color("black")
    pen3.shape("turtle")
    pen3.shapesize(size/50)
    pen3.speed(speed*10)
    # start
    pen3.penup()
    pen3.right(-45)
    pen3.forward(2*size)
    pen3.left(85)
    # sin 5
    pen3.pendown()
    import math
    number4 = size*4*(math.pi)/36
    for _ in range(36):
        pen3.left(10)
        pen3.forward(number4)
        pen3.circle(4*size)

    pen2 = turtle.Turtle()
    pen2.color("black")
    pen2.shape("turtle")
    pen2.shapesize(size/50)
    pen2.speed(speed*10)
    #pen2.width(size/10)
    for _ in range(9):
        pen2.penup()
        pen2.forward(6*size)
        pen2.right(90)
        pen2.pendown()
        pen2.forward(6*size)
        for _ in range(3):
            pen2.right(90)
            pen2.forward(12*size)
        pen2.right(90)
        pen2.forward(6*size)
        # back to center
        pen2.right(90)
        pen2.penup()
        pen2.forward(6*size)
        pen2.pendown()
        pen2.right(-10)

    pen1.shapesize(0.1)
    pen2.shapesize(0.1)
    pen3.shapesize(0.1)

if select == str(3):
    size = int(input("size(suggested: 50): "))
    repeat = int(input("repeat(suggested: >20): "))
    size = size/2

    pen1 = turtle.Turtle()
    pen2 = turtle.Turtle()
    pen3 = turtle.Turtle()
    pen4 = turtle.Turtle()
    pen5 = turtle.Turtle()
    pen6 = turtle.Turtle()
    pen7 = turtle.Turtle()
    pen8 = turtle.Turtle()
    for arms in [pen1, pen2, pen3, pen4, pen5, pen6, pen7, pen8]:
        arms.shape("turtle")
        arms.shapesize(size/50)
        arms.speed(speed*10)

    ang = 0
    for arms in [pen1, pen2, pen3, pen4, pen5, pen6, pen7, pen8]:
        arms.right(45*ang)
        for counter in range(repeat):
            for color in ["red", "orange", "green", "blue"]:
                arms.color(color)
                arms.forward((size*counter*2)/10)
                arms.right(90)
            arms.right(10-(counter*0.2))
            arms.penup()
            arms.forward((size*counter)/10)
            arms.pendown()
        ang = ang + 1
        arms.shapesize(0.01)

if select == str(4):
    size = int(input("size(suggested: 20): "))
    repeat = int(input("repeat: "))

    pen1 = turtle.Turtle()
    pen1.color("black")
    pen1.shape("arrow")
    pen1.shapesize(1)
    pen1.speed(20)

    def fibonacci(num1: int) -> int:
        if num1 > 2:
            return fibonacci(num1 - 1) + fibonacci(num1 - 2)
        else:
            return 1

    def draw_fibonacci():
        num2 = 0
        for _ in range(repeat):
            num2 = num2 + 1
            r = size * fibonacci(num2)
            diag_l = math.sqrt(2*r**2)
            pen1.circle(r, 90)
            for _ in range(2):
                pen1.color("lightblue")
                pen1.right(-90)
                pen1.forward(r)
                pen1.color("black")
            pen1.right(-135)
            pen1.pu()
            pen1.forward(diag_l/2)
            pen1.color("blue")
            pen1.pd()
            pen1.write(fibonacci(num2))
            pen1.pu()
            pen1.color("black")
            pen1.forward(diag_l/2)
            pen1.pd()
            pen1.right(-45)

    draw_fibonacci()

if select == str(5):
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

    pen1 = turtle.Turtle()
    pen1.color("black")
    pen1.shape("arrow")
    pen1.shapesize(1)
    pen1.speed(20)

    repeat = int((repeat*(360/sides)-1))
    ang1 = 1

    pen1.pu()
    L = size
    n = 1
    for counter in range(repeat):
        if ang1 >= 360/sides:
            ang1 = 1
            n = n + 1
        ang2 = 180-(360/sides)
        ang3 = 180-(ang2+ang1)
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

if select == str(6):
    repeat = int(input("building: "))

    window.bgcolor("black")

    pen1 = turtle.Turtle()
    pen1.color("black")
    pen1.shape("arrow")
    pen1.shapesize(1)
    pen1.speed(0)

    pen1.pu()
    pen1.goto(0, -400)
    pen1.pd()
    pen1.color("white")
    pen1.width(5)
    pen1.forward(-600)
    pen1.forward(1200)
    pen1.forward(-600)
    pen1.color("black")
    pen1.width(3)

    import random

    def make_window():
        pen1.pu()
        pen1.forward(10)
        pen1.pd()
        color = ['yellow', 'black', 'white', 'lightblue']
        pen1.color(random.choice(color))
        pen1.shapesize(0.5)
        pen1.shape("square")
        pen1.stamp()
        pen1.pu()
        pen1.color("black")
        pen1.shape("arrow")
        pen1.shapesize(1)
        pen1.forward(10)

    #building
    for counter in range(repeat):
        width = random.randint(5, 10)
        length = random.randint(21, 50)
        location = random.randint(-700, 700)
        if repeat-counter <= repeat/2:
            length = random.randint(11, 20)
            location = random.randint(-1000, 1000)

        pen1.pu()
        pen1.goto(location, -400)
        pen1.pd()
        pen1.fillcolor("gray")
        pen1.begin_fill()
        for counter in range(2):
            pen1.forward(20*width)
            pen1.right(-90)
            pen1.forward(20*length)
            pen1.right(-90)
        pen1.end_fill()

        for counter in range(length):
            pen1.right(-90)
            pen1.forward(10)
            pen1.right(90)
            for counter in range(width):
                make_window()
            pen1.forward(-20*width)
            pen1.right(-90)
            pen1.forward(10)
            pen1.right(90)

    pen1.shapesize(0.01)

turtle.exitonclick()
turtle.done
