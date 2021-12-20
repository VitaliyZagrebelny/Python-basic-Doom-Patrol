print("Calculator!")

while True:

    i = input("Знак (+,-,*,/): ")
    if i in ('+', '-', '*', '/'):
        x = (float(input("x= ")))
        y = (float(input("y= ")))
        if i == '+':
            c = x + y
            print (str(c))
            with open("result.txt", "w") as file:
                file.write(c)
        elif i == '-':
            c1 = x - y
            print(str(c1))
            with open("result.txt", "w") as file:
                file.write(c1)
        elif i == '*':
            c2 = x * y
            print(str(c2))
            with open("result.txt", "w") as file:
                file.write(c2)
        elif i == '/':
            if y != 0:
                c3 = x / y
                print(str(c3))
                with open("result.txt", "w") as file:
                    file.write(c3)
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")
