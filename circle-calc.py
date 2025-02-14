import math

def circle_calc(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    diameter = 2 * radius
    return area, circumference, diameter

if __name__ == "__main__":
    r = float(input("Enter the radius of circle: "))
    area, c, d = circle_calc(r)
    print(f"area is {area}, circumference is {c}, diameter is {d}")