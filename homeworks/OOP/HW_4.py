# 1TASK
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


MyVehicle = Vehicle(200, 300)
print(MyVehicle)


# 2TASK
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, capacity):
        super().__init__(max_speed, mileage)
        self.capacity = capacity

    def seat_capacity(self):
        print(f"I need a bus numbered {self.capacity}")


My_bus = Bus(25, 35, 44)

# 3TASK
print(type(My_bus))

# 4TASK
print(isinstance(My_bus, Vehicle))


# 5TASK
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


# 6TASK
class School_Bus(School, Bus):
    def __init__(self, max_speed, mileage, capacity,
                 bus_school_color, get_school_id, number_of_students):
        School.__init__(self, get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, capacity)
        self.bus_school_color = bus_school_color


MySchool_Bus = School_Bus(25, 35, 44, "Red", 22, 51)
print(MySchool_Bus.bus_school_color)


# 7TASK
class Bear:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print("Arrr")


class Wolf:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print("Ayyy")


animals1 = Bear("Arrr")
animals2 = Wolf("Ayyy")

for animal in (animals1, animals2):
    (animal.make_sound())


# 8TASK

# class City:
#     def __init__(self, name, population):
#         self.name = name
#         self.population = population
#
#     def verify_population(self):
#         if self.population > 1500:
#             return self.population
#         else:
#             return ("Your city is small!")
#
#
# Kyiv = City("Kyiv", 4139598)
# Xarkov = City("Xarkov", 582478)
# Poltava = City("Poltava", 1234)
#
# cities = (Kyiv, Xarkov, Poltava)
#
# for i in cities:
#     print(i.verify_population())
