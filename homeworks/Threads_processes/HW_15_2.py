import math
import threading


def calculation(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant > 0:
        value1 = (-b - math.sqrt(discriminant)) / (2 * a)
        value2 = (-b + math.sqrt(discriminant)) / (2 * a)
        print(f" Solution are: {value1} and {value2}")
    elif discriminant == 0:
        value1 = value2 = -b / (2 * a)
        print(f"Solution are one: {value1} or {value2}")
    else:
        print("Not solution!")


t1 = threading.Thread(target=calculation(6, 11, -35))
t2 = threading.Thread(target=calculation(5, - 2, -9))
t1.start()
t2.start()
