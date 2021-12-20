print("Calculator!")

while True:

    i = input("Знак (+,-,*,/): ")
    if i in ('+', '-', '*', '/'):
        x = float(input("x= "))
        y = float(input("y= "))
        if i == '+':
            c = x + y
            print(c)
            with open("result.txt", "w") as file:
                file.write(str(c))
        elif i == '-':
            c1 = x - y
            print(c1)
            with open("result.txt", "w") as file:
                file.write(str(c1))
        elif i == '*':
            c2 = x * y
            print(c2)
            with open("result.txt", "w") as file:
                file.write(str(c2))
        elif i == '/':
            if y != 0:
                c3 = x / y
                print(c3)
                with open("result.txt", "w") as file:
                    file.write(str(c3))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")
