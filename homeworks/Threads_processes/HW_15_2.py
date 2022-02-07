import math
from multiprocessing import Process


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


if __name__ == '__main__':
    t1 = Process(target=calculation(6, 11, -35))
    t2 = Process(target=calculation(5, - 2, -9))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
