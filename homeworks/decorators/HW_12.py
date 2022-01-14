# Task #1
def double_result(func):
    def inner(a, b):
        # return function result multiplied by two
        value = func(a, b)

        return value * 2

    return inner


def add_task_one(a, b):
    return a + b


print(add_task_one(5, 5))


@double_result
def add_task_one(a, b):
    return a + b


print(add_task_one(5, 5))


# Task #2
def only_odd_parameters(func):
    def inner(*args):
        for j in args:
            if j % 2 != 0:
                return func(*args)
            # if args passed to func are not odd - return "Please use only odd numbers!"
            else:
                return "Please use only odd numbers!"

    return inner


@only_odd_parameters
def add_task_two(a, b):
    return a + b


print(add_task_two(5, 5))
print(add_task_two(4, 4))


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


print(multiply(5, 5, 5, 5, 5))
print(multiply(2, 5, 3, 3, 2))


# Task #3
def logged(func):
    def inner(*args):
        result = func(*args)
        return result

    return inner


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


# Task #4
def type_check(correct_type):
    def type_decorator(func):
        def inner(num):
            if type(num) == correct_type:
                return func(num)
            else:
                return f"Wrong Type: {type(num)}"

        return inner

    return type_decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
