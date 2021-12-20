print("Calculator!")

while True:
    i = input("Знак (+,-,*,/): ")
    if i in ('+', '-', '*', '/'):
        x = float(input("x= "))
        y = float(input("y= "))
        if i == '+':
            c = x + y
            print(str(c))
        elif i == '-':
            c1 = x - y
            print(str(c1))
        elif i == '*':
            c2 = x * y
            print(str(c2))
        elif i == '/':
            if y != 0:
                c3 = x / y
                print(str(c3))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")

with open("result.txt", "w") as file:
    file.write(f'{c},{c1},{c2},{c3}')
