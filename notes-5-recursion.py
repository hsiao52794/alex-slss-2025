import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.left(90)
t.penup()
t.goto(0, -400)
t.color("brown")
t.width(5)
t.shape("arrow")
t.speed(0)

br_n = int(input("repeat: "))
t.pendown()
t.forward(300)
t.penup()
def draw_tree(level: int, branch_length: float):
    # draw a tree recursively at a given level
    # level - the levels of branches
    # branch_length - the length of branch in pixels
    t.pendown()
    if level> 0:
        a = 90
        t.forward(branch_length)
        t.left(a*(br_n-1)/2)
        for _ in range(br_n-1):
            draw_tree(level - 1, branch_length * 0.8)
            t.right(a)
        draw_tree(level - 1, branch_length * 0.8)
        t.left(a*(br_n-1)/2)
        t.backward(branch_length)
    else:
        t.color("green")
        t.stamp()
        t.color("brown")

# only leftside
"""
def draw_tree(level: int, branch_length: float):
    # draw a tree recursively at a given level
    # level - the levels of branches
    # branch_length - the length of branch in pixels
    t.pendown()
    if level> 0:
        a = 20
        t.forward(branch_length)
        t.left((br_n-1)*a)
        for _ in range(br_n):
            draw_tree(level - 1, branch_length * 0.8)
            t.right(a)
        t.left(a)
        t.backward(branch_length)
    else:
        t.color("green")

        t.stamp()
        t.color("brown")
"""

level = int(input("level: "))

#draw_tree(level, 200)

wn.exitonclick()

def factorial(num: int) -> int:
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1

def fibonacci(num: int) -> int:
    if num > 2:
        return fibonacci(num - 1) + fibonacci(num - 2)
    else:
        return 1

a = int(input(": "))
for i in range(a):
    print("------------------")
    print(fibonacci(i+1))
    print()
    print(fibonacci(i+1)/fibonacci(i))
    print()

print(factorial(1))
print(factorial(5))
print(factorial(100))
