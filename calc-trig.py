import math

def normalize_angle(angle: float) -> float:
    if angle < 90:
        angle = 180 - angle

    return 360 - (angle - 25)

print("Enter the distance from spot A to the target.")
pos_A = int(input(": "))
print("Enter the distance from spot B to the target.")
pos_B = int(input(": "))

c = 11

ang_a = math.acos((pos_B**2 + c**2 - pos_A**2)/(2 * pos_B * c))
ang_a = math.degrees(ang_a)
ang_b = math.acos((pos_A**2 + c**2 - pos_B**2)/(2 * pos_A * c))
ang_b = math.degrees(ang_b)

ang_a = normalize_angle(ang_a)
ang_b = normalize_angle(ang_b)

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
