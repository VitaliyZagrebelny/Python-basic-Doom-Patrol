import dataclasses
from collections import namedtuple


# 1TASK

class Laptop:
    def __init__(self, ):
        element = Battery("The laptop needs a strong battery")
        self.element = element


class Battery:
    def __init__(self, power):
        self.power = power


# 2TASK
class Guitar:
    def __init__(self, types_guitars):
        self.types_guitar = types_guitars


class GuitarString:
    def __init__(self):
        pass


types_guitars = GuitarString
guitar = Guitar(types_guitars)


# 3TASK
class Calc:
    @staticmethod
    def add_nums(x, y, z):
        return (x + y + z)


calculator = Calc()
print(calculator.add_nums(20, 30, 40))


# 4 TASK

class Pasta:
    def __init__(self, element):
        self.element = element

    def __str__(self):
        return f"Pasta ({self.element})"

    @classmethod
    def carbonara(cls):
        return (["tomato", "cucumber"])

    @classmethod
    def bolognaise(cls):
        return (['bacon', 'parmesan', 'eggs'])


carbonara_Past = Pasta.carbonara()
bolognaise_Past = Pasta.bolognaise()
print(carbonara_Past)
print(bolognaise_Past)


# 5TASK
class Concert:
    max_visitors_num = 0

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, meaning):
        if meaning < self.max_visitors_num:
            self._visitors_count = meaning
        else:
            self._visitors_count = self.max_visitors_num


Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)


# 6TASK

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


my_biography = AddressBookDataClass(key=1111,
                                    name="Vitaliy",
                                    phone_number="222-44-55",
                                    address="Kyiv",
                                    email="zfdhhfhh@gmail.com", birthday="today",
                                    age=20)
print(my_biography)
print(my_biography.name)
print(my_biography.email)

# 7 TASK
AddressBookDataClass2 = namedtuple("AddressBookDataClass2",
                                   ["key",
                                    "name",
                                    "phone_number",
                                    "address",
                                    "email",
                                    "birthday",
                                    "age"])
my_biography_2 = AddressBookDataClass2(1111,
                                       "Vitaliy",
                                       "222-44-55",
                                       "Kyiv",
                                       "zfdhhfhh@gmail.com",
                                       "today",
                                       20)
print(my_biography_2)
print(my_biography_2.address)
print(my_biography_2.age)


# 8 TASK

class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f"AddressBook: {self.key},{self.name},{self.phone_number}," \
               f"{self.address},{self.email},{self.birthday},{self.age}"


my_biography_3 = AddressBook(1111, "Vitaliy",
                             "222-44-55",
                             "Kyiv",
                             "zfdhhfhh@gmail.com",
                             "today",
                             20)
print(my_biography_3)


# 9 TASK
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    @property
    def what_is_age(self):
        return f"This name is {self.name}, and is {self.age} old!"


the_person = Person("John", 36, "USA")
the_person.age = 50
print(the_person.what_is_age)


# 10TASK
class Student:
    id = 1111
    name = "Vitaliy"
    email = "zfdhhfhh@gmail.com"

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email


vitaliy = Student(1111, "Vitaliy", "zfdhhfhh@gmail.com")
print(getattr(vitaliy, "email"))
print(getattr(vitaliy, "name"))
setattr(vitaliy, "Email", "new_email_zfdhhfhh@gmail.com")
print(getattr(vitaliy, "Email"))


# 11TASK

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, new_temperature):
        self._temperature = new_temperature


fahrenheit = Celsius(45)
fahrenheit.temperature = (fahrenheit.temperature * 1.8) + 32
print(fahrenheit.temperature)
