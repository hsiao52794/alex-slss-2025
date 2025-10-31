import turtle

print('(Use number 1 to 9 to select options, and press "Enter" to confirm)')
print("(1)circle")
print("(2)circle")
print("(3)spiral")
print("(4)fibonacci")
print("(5)square")
select = input(": ")
# just in case the user is stupid
while select != str(1) and select != str(2) and select != str(3) and select != str(4) and select != str(5):
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
    import math
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
    size = int(input("size(suggested: 10): "))
    repeat = int(input("repeat: "))
    pen1 = turtle.Turtle()
    pen1.color("black")
    pen1.shape("arrow")
    pen1.shapesize(1)
    pen1.speed(20)

    ang1 = 0

    pen1.pu()
    L = size
    for counter in range(repeat):
        ang2 = 180-(90+ang1)
        L1 = math.sin(math.radians(ang2))*(L/math.sin(math.radians(90)))
        L2 = math.sin(math.radians(ang1))*(L/math.sin(math.radians(90)))
        pen1.forward(L/2)
        pen1.right(-90)
        pen1.forward(L/2)
        pen1.right(180)
        pen1.pd()
        for color in ["red", "orange", "green", "blue"]:
            pen1.color(color)
            pen1.forward(L)
            pen1.right(90)
        pen1.pu()
        pen1.forward(L/2)
        pen1.right(90)
        pen1.forward(L/2)
        pen1.right(180)
        pen1.right(ang1)
        L = L1 + L2
        ang1 = ang1 + 1
    pen1.shapesize(0.01)

turtle.exitonclick()
turtle.done
