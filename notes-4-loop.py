# loop
# Author: Alex
# Oct 6 2025

import turtle

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("white")

# TMNT - turtles
# creat a turtle called mike

def make_cookies(x: int, y: int):
    mike = turtle.Turtle()
    mike.shapesize(1/5)
    mike.shape("circle")
    mike.color("brown")
    mike.speed(0)

    mike.setheading(0)
    mike.penup()
    mike.goto(0 + x, -30 + y)
    mike.pendown()
    mike.circle(30)
    mike.penup()
    mike.goto(10 + x, 10 + y)
    mike.stamp()
    mike.goto(-10 + x, 10 + y)
    mike.stamp()
    mike.goto(10 + x, -10 + y)
    mike.stamp()
    mike.goto(-10 + x, -10 + y)
    mike.stamp()
    mike.goto(0 + x, 0 + y)
    mike.stamp()

import random
for _ in range(500):
    x = random.randrange(-500, 500)
    y = random.randrange(-500, 500)
    make_cookies(x, y)
"""
for counter in range(50):
    counter = counter * 50
    make_cookies(-counter, -counter)
    make_cookies(counter, -counter)
    make_cookies(counter, counter)
    make_cookies(-counter, counter)
"""

window.exitonclick()
