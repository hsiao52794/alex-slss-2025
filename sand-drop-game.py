"""
print("@, @, @, @, @")
print("@, ., ., ., @")
print("@, ., ., ., @")
print("@, ., ., ., @")
print("@, @, @, @, @")

m = int(input("use w, a, s, d to control:"))

if m == 1:
    print("@, @, @, @, @")
    print("., ., ., @, @")
    print("., ., ., @, @")
    print("., ., ., @, @")
    print("@, @, @, @, @")
"""
#a1a2a3a4a5
#b1b2b3b4b5
#c1c2c3c4c5
#d1d2d3d4d5
#e1e2e3e4e5
n = str(".")
o = str("@")
#1st layer
a1 = n
a2 = n
a3 = n
a4 = n
a5 = n
#2nd layer
b1 = n
b2 = n
b3 = n
b4 = n
b5 = n
#3rd layer
c1 = n
c2 = n
c3 = n
c4 = n
c5 = n
#4th layer
d1 = n
d2 = n
d3 = n
d4 = n
d5 = n
#5th layer
e1 = n
e2 = n
e3 = n
e4 = n
e5 = n

print(e1, e2, e3, e4, e5)
print(d1, d2, d3, d4, d5)
print(c1, c2, c3, c4, c5)
print(b1, b2, b3, b4, b5)
print(a1, a2, a3, a4, a5)

m = int(input("press 1, 2, 3, 4 and 5 to drop sand. "))
# 1
"""
while m > 0:
    if m == 1:
        if a1 == n:
            a1 = o
        elif a1 == o:
            b1 = o
        elif b1 == o:
            c1 = o
        elif c1 == o:
            d1 = o
        elif d1 == o:
            e1 = o

    # 2

    # 3

    # 4

    # 5
    print(a1, a2, a3, a4, a5)
    print(b1, b2, b3, b4, b5)
    print(c1, c2, c3, c4, c5)
    print(d1, d2, d3, d4, d5)
    print(e1, e2, e3, e4, e5)
    m = int(input())
"""
while m > 0:
  if m == 1:
    if e1 == n:
      if d1 == n:
        if c1 == n:
          if b1 == n:
            if a1 == n:
              a1 = o
            elif a1 == o:
              b1 = o
          elif b1 == o:
            c1 = o
        elif c1 == o:
          d1 = o
      elif d1 == o:
        e1 = o
  if m == 2:
    if e2 == n:
      if d2 == n:
        if c2 == n:
          if b2 == n:
            if a2 == n:
              a2 = o
            elif a2 == o:
              b2 = o
          elif b2 == o:
            c2 = o
        elif c2 == o:
          d2 = o
      elif d2 == o:
        e2 = o
  if m == 3:
    if e3 == n:
      if d3 == n:
        if c3 == n:
          if b3 == n:
            if a3 == n:
              a3 = o
            elif a3 == o:
              b3 = o
          elif b3 == o:
            c3 = o
        elif c3 == o:
          d3 = o
      elif d3 == o:
        e3 = o
  if m == 4:
    if e4 == n:
      if d4 == n:
        if c4 == n:
          if b4 == n:
            if a4 == n:
              a4 = o
            elif a4 == o:
              b4 = o
          elif b4 == o:
            c4 = o
        elif c4 == o:
          d4 = o
      elif d4 == o:
        e4 = o
  if m == 5:
    if e5 == n:
      if d5 == n:
        if c5 == n:
          if b5 == n:
            if a5 == n:
              a5 = o
            elif a5 == o:
              b5 = o
          elif b5 == o:
            c5 = o
        elif c5 == o:
          d5 = o
      elif d5 == o:
        e5 = o

  print(e1, e2, e3, e4, e5)
  print(d1, d2, d3, d4, d5)
  print(c1, c2, c3, c4, c5)
  print(b1, b2, b3, b4, b5)
  print(a1, a2, a3, a4, a5)

  m = int(input())

'''
  if e1 == n:
    if d1 == n:
      if c1 == n:
        if b1 == n:
          if a1 == n:
            a1 = o
          elif a1 == o:
            b1 = o
        elif b1 == o:
          c1 = o
      elif c1 == o:
        d1 == o
    elif d1 == o:
      e1 = o
'''
"""
print(e1, e2, e3, e4, e5)
print(d1, d2, d3, d4, d5)
print(c1, c2, c3, c4, c5)
print(b1, b2, b3, b4, b5)
print(a1, a2, a3, a4, a5)

m = int(input())
"""
# python3 sand-drop-game.py
