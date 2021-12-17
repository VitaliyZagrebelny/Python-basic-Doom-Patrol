import random
from abc import ABC, abstractmethod


class Animal:
    types = ("Herbivorous", "Predator")

    def __init__(self, power, speed):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.small_power = False
        self.speed = speed

    def eat(self, power):
        self.current_power += power
        if self.current_power + power >= self.max_power:
            self.current_power = self.max_power

    def lose_power(self, power):
        self.current_power -= power
        if self.current_power - power < 0:
            self.small_power = True

    @abstractmethod
    def name(self):
        pass

    def animal_info(self):
        return self.name() + str(self.id)


class Predator(Animal):  # Хижак
    def name(self):
        predator = ["Fox", "Wolf", "Bear"]
        return random.choice(predator)


class Herbivorous(Animal):  # Травоїдний
    def name(self):
        herbivorous = ["Bees", "Horses", "Koalas"]
        return random.choice(herbivorous)


class Forest:  # Ліс
    def __init__(self):
        self.animals = dict()

    def add_animal(self, animal):
        self.animals[animal.id] = animal

    def remove_animal(self, animal):
        del self.animals[animal.id]

    def animal_id(self, predator_id=None):
        if not isinstance(predator_id, type(None)):
            note_list = list(note for note in self.animals.keys()
                             if note != predator_id)
        else:
            note_list = list(self.animals.keys())
        animal_note = random.choice(note_list)
        return self.animals[animal_note]

    def animals_count(self):
        return len(self.animals())

    def stop(self):
        if self.animals_count() <= 1:
            return False
        return True

    @staticmethod
    def animal_note(self):
        for animal in forest.animals.keys():
            print(forest.animals[animal].animal_info())

    @staticmethod
    def animal_generator():
        animal_type = random.choice(Animal.types)

        if animal_type == "Predator":
            new_animal = Predator(random.randint(25, 100),
                                  random.randint(25, 100))
        else:
            new_animal = Herbivorous(random.randint(25, 100),
                                     random.randint(25, 100))

        return new_animal

    def any_predator_left(self):
        for key in self.animals.keys():
            if isinstance(self.animals[key], Predator):
                return True

        return False


if __name__ == "__main__":
    nature = animal_generator()
    forest = Forest()
    for i in range(8):
        animal = next(nature)
        forest.add_animal(animal)
    while forest.any_predator_left():
        for animal in forest:
            animal.eat(forest=forest)
            forest.number = 1
