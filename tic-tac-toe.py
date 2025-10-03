
print("")
border_y = str("|")
border_x = str("⏤")
a1 = str(".")
a2 = str(".")
a3 = str(".")
b1 = str(".")
b2 = str(".")
b3 = str(".")
c1 = str(".")
c2 = str(".")
c3 = str(".")
repeat = 0

print("Use numder 1 to 9 play")
print("like this: ")

print( "7", border_y, "8", border_y, "9")
print( border_x, border_x, border_x, border_x, border_x)
print( "4", border_y, "5", border_y, "6")
print( border_x, border_x, border_x, border_x, border_x)
print( "1", border_y, "2", border_y, "3")

print("")
start = input('type in "start" to start the game.')

print( a1, border_y, a2, border_y, a3)
print( border_x, border_x, border_x, border_x, border_x)
print( b1, border_y, b2, border_y, b3)
print( border_x, border_x, border_x, border_x, border_x)
print( c1, border_y, c2, border_y, c3)

while start == str("start"):

    O = int(input("O: "))
    if O == 1:
        c1 = str("O")
    if O == 2:
        c2 = str("O")
    if O == 3:
        c3 = str("O")
    if O == 4:
        b1 = str("O")
    if O == 5:
        b2 = str("O")
    if O == 6:
        b3 = str("O")
    if O == 7:
        a1 = str("O")
    if O == 8:
        a2 = str("O")
    if O == 9:
        a3 = str("O")

    print( a1, border_y, a2, border_y, a3)
    print( border_x, border_x, border_x, border_x, border_x)
    print( b1, border_y, b2, border_y, b3)
    print( border_x, border_x, border_x, border_x, border_x)
    print( c1, border_y, c2, border_y, c3)

    """
    a1 a2 a3
    b1 b2 b3
    c1 c2 c3
    a1 b1 c1

    a2 b2 c2
    a3 b3 c3
    a1 b2 c3
    c1 b2 a3
    """

    if a1 and a2 and a3 == str("O") or b1 and b2 and b3 == str("O") or c1 and c2 and c3 == str("O") or a1 and b1 and c1 == str("O"):
        print("Player O has won!!!")
        break
    if a2 and b2 and c2 == str("O") or a3 and b3 and c3 == str("O") or a1 and b2 and c3 == str("O") or c1 and b2 and a3 == str("O"):
        print("Player O has won!!!")
        break

    X = int(input("X: "))
    if X == 1:
        c1 = str("X")
    if X == 2:
        c2 = str("X")
    if X == 3:
        c3 = str("X")
    if X == 4:
        b1 = str("X")
    if X == 5:
        b2 = str("X")
    if X == 6:
        b3 = str("X")
    if X == 7:
        a1 = str("X")
    if X == 8:
        a2 = str("X")
    if X == 9:
        a3 = str("X")

    print( a1, border_y, a2, border_y, a3)
    print( border_x, border_x, border_x, border_x, border_x)
    print( b1, border_y, b2, border_y, b3)
    print( border_x, border_x, border_x, border_x, border_x)
    print( c1, border_y, c2, border_y, c3)

    if a1 and a2 and a3 == str("X") or b1 and b2 and b3 == str("X") or c1 and c2 and c3 == str("X") or a1 and b1 and c1 == str("X"):
        print("Player X has won!!!")
        break
    if a2 and b2 and c2 == str("X") or a3 and b3 and c3 == str("X") or a1 and b2 and c3 == str("X") or c1 and b2 and a3 == str("X"):
        print("Player X has won!!!")
        break
