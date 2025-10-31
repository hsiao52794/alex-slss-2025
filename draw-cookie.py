import turtle
window = turtle.Screen()
window.bgcolor("white")

repeat = int(input("repeat: "))
mike = turtle.Turtle()
mike.shapesize(1/5)
mike.shape("circle")
mike.color("brown")
mike.speed(0)
mike.width(5)

zoom = int(input("zoom(minimum 5): "))
if zoom < 5:
    zoom = 5

def draw_cookie():
    angle = mike.heading()
    mike.setheading(0)
    mike.circle(3*zoom)
    mike.right(-90)
    mike.penup()
    mike.forward(4*zoom)
    mike.right(90)
    for _ in range(4):
        mike.forward(1*zoom)
        mike.pendown()
        mike.stamp()
        mike.right(90)
        mike.penup()
        mike.forward(1*zoom)
    mike.right(90)
    mike.forward(1*zoom)
    mike.pendown()
    mike.stamp()
    mike.penup()
    mike.forward(3*zoom)
    mike.setheading(angle)

draw_cookie()
for counter in range(repeat):
    for _ in range(2):
        for _ in range(counter):
            mike.penup()
            mike.forward(10*zoom)
            mike.pendown()
            draw_cookie()
        mike.right(90)

turtle.exitonclick()
