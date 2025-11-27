print("Enter the distance from spot A to the target.")
pos_A = int(input(": "))
print("Enter the distance from spot B to the target.")
pos_B = int(input(": "))

import math

a = pos_A
b = pos_B
c = 11

ang_a = math.acos((b**2 + c**2 - a**2)/(2 * b * c))
ang_a = math.degrees(ang_a)
ang_b = math.acos((a**2 + c**2 - b**2)/(2 * a * c))
ang_b = math.degrees(ang_b)

"""

"""
for ang in [ang_a, ang_b]:
    if ang < 90:
        ang = 180 - ang

    ang = 360 - (ang -25)

if ang_a < 90:
    ang_a = 180 - ang_a

ang_a = 360 - (ang_a - 25)

if ang_b < 90:
    ang_b = 180 - ang_b

ang_b = 360 - (ang_b - 25)

ang = (ang_a + ang_b) / 2

print()
print("Angle from spot A to target:")
print(ang_a)
print("Angle from spot B to target:")
print(ang_b)
print()
print("Final angle to target:")
print(round(ang))
print()
