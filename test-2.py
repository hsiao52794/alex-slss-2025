repeat = int(input("repeat: "))
auto = int(input("auto(0 or 1): "))

import turtle

window = turtle.Screen()
window.bgcolor("white")

pen1 = turtle.Turtle()
pen1.color("black")
pen1.shape("circle")
pen1.shapesize(0.5)
pen1.speed(20)

import random

def outline():
    pen1.color("black")
    pen1.pu()
    pen1.goto(400, -400)
    pen1.pd()
    pen1.goto(400, 400)
    pen1.goto(-400, 400)
    pen1.goto(-400, -400)
    pen1.goto(400, -400)
    pen1.pu()
    pen1.goto(0, 0)

def draw():
    green = 0
    orange = 0
    red = 0
    for i in range(repeat):
        pen1.pu()
        pen1.goto(random.randint(-400, 400), random.randint(-400, 400))
        pen1.pd()
        colors = ["gray", "green", "orange", "red"]
        weight = [84, 10, 5, 1]
        color = random.choices(colors, weights=weight, k=1)[0]
        if color == "green":
            green += 1
        elif color == "orange":
            orange += 1
        elif color == "red":
            red += 1
        pen1.color(color)
        pen1.stamp()

    print(f"Green: {green}, Orange: {orange}, Red: {red}")

def clean():
    pen1.color("white")
    pen1.pu()
    pen1.goto(500, -500)
    pen1.pd()
    pen1.fillcolor("white")
    pen1.begin_fill()
    pen1.goto(500, 500)
    pen1.goto(-500, 500)
    pen1.goto(-500, -500)
    pen1.goto(500, -500)
    pen1.pu()
    pen1.end_fill()
    pen1.goto(0, 0)

import time

a = 0

if auto == 1:
    outline()
    for i in range(10000):
        print(i+1)
        draw()
        time.sleep(0.5)
    window.exitonclick()

elif auto == 0:
    for i in range(10000):
        print(i+1)
        outline()
        draw()
        time.sleep(0.5)
        stop = str(input(":"))
        if stop == "stop":
            break
        clean()
    window.bye()
