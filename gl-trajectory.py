import math

def trajectory(theta, d):
    vi = 76
    g = 10

    x = d * math.cos(theta)
    y = d * math.sin(theta)

    determinant = vi**4 - g * (g * x**2 + 2 * vi**2 * (y - 1.66))
    # print(f"Determinant: {determinant:.2f}")
    if determinant <= 0:
        print("Target is out of range.")
        return
    r_high = math.atan((vi**2 + math.sqrt(determinant)) / (g * x))
    r_low = math.atan((vi**2 - math.sqrt(determinant)) / (g * x))
    t_low = (x / (vi * math.cos(r_low)))
    t_high = (x / (vi * math.cos(r_high)))

    def spacer(ang, zero):
        ang = math.degrees(ang)
        space = float((ang - zero))
        if 10 < space < 90:
            return " "
        elif 0 < space < 10:
            return "  "
        elif -10 < space < 0:
            return " "
        elif -90 < space < -10:
            return ""
        else:
            return ""

    print("-" * 55)
    print(f"Low angle: {math.degrees(r_low):.2f} degrees, Time: {t_low:.2f} seconds")
    print("Zeroing distance")
    print("|  100m  |  150m  |  200m  |  250m  |  300m  |  350m  |")
    print(f"|{spacer(r_low, 3.5)}{math.degrees(r_low) - 3.5:.2f}° |{spacer(r_low, 6.5)}{math.degrees(r_low) - 6.5:.2f}° |{spacer(r_low, 9.5)}{math.degrees(r_low) - 9.5:.2f}° |{spacer(r_low, 12.5)}{math.degrees(r_low) - 12.5:.2f}° |{spacer(r_low, 15.5)}{math.degrees(r_low) - 15.5:.2f}° |{spacer(r_low, 18.5)}{math.degrees(r_low) - 18.5:.2f}° |")
    print("-" * 55)
    print(f"High angle: {math.degrees(r_high):.2f} degrees, Time: {t_high:.2f} seconds")
    print("Zeroing distance")
    print("|  100m  |  150m  |  200m  |  250m  |  300m  |  350m  |")
    print(f"| {math.degrees(r_high) - 3.5:.2f}° | {math.degrees(r_high) - 6.5:.2f}° | {math.degrees(r_high) - 9.5:.2f}° | {math.degrees(r_high) - 12.5:.2f}° | {math.degrees(r_high) - 15.5:.2f}° | {math.degrees(r_high) - 18.5:.2f}° |")

stop = False
while not stop:
    print()
    print("-" * 75)
    theta = int(input("Enter the angle of elevation (in degrees): "))
    d = int(input("Enter the distance to the target (in meters): "))
    trajectory(math.radians(theta), d)
