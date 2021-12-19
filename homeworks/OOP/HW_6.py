import time
import random
import uuid
from abc import ABC, abstractmethod


class Animal(ABC):
    types = ("Herbivorous", "Predator")

    def __init__(self, power, speed):
        self.id = uuid.uuid4()
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
        if self.current_power - power <= 0:
            self.small_power = True

    @abstractmethod
    def name(self):
        pass

    def animal_info(self):
        return self.name() + str(self.id)


class Predator(Animal):  # Хижак
    def name(self):
        return self.types[1]


class Herbivorous(Animal):  # Травоїдний
    def name(self):
        return self.types[0]


class Forest:  # Ліс
    def __init__(self):
        self.animals = dict()

    def add_animal(self, animal):
        self.animals[animal.id] = animal

    def remove_animal(self, animal):
        del self.animals[animal.id]

    def animals_count(self):
        return len(self.animals())

    @property
    def hunting_possible(self):
        if self.animals_count() <= 1:
            return False
        return True

    def get_animal(self, predator_id=None):
        if not isinstance(predator_id, type(None)):
            note_list = list(note for note in self.animals.keys()
                             if note != predator_id)
        else:
            note_list = list(self.animals.keys())
        animal_note = random.choice(note_list)
        return self.animals[animal_note]

    @staticmethod
    def print_animal_note():
        for animal in forest.animals.keys():
            print(forest.animals[animal].animal_info())

    def any_predator_left(self):
        for key in self.animals.keys():
            if isinstance(self.animals[key], Predator):
                return True
            return False

    def start_hunting(self):
        predator = Forest.get_animal(self)
        if isinstance(predator, Herbivorous):
            predator.eat(50)
        victim = Forest.get_animal(self, hunter_id)
        if hunter.speed > victim.speed and hunter.current_power > victim.current_power:
            hunter.eat(50)
            victim.out_power = True
        else:
            hunter.lose_power(30)
            victim.lose.power(30)
        if hunter.out_power:
            self.remove_animal(hunter)
        if victim.lose_power:
            self.remove_animal(victim)


class AnimalGeneartor:
    def __iter__(self):
        return self

    def __next__(self):
        animal_type = random.choice(Animal.types)

        if animal_type == "Predator":
            new_animal = Predator(random.randint(25, 100),
                                  random.randint(25, 100))
        else:
            new_animal = Herbivorous(random.randint(25, 100),
                                     random.randint(25, 100))

        return new_animal


if __name__ == "__main__":
    nature = AnimalGeneartor()
    forest = Forest()
    for i in range(8):
        animal = next(nature)
        forest.add_animal(animal)
    print("Who leaves in the forest?")
    forest.print_animal_note()

    print("Go hunting!")

    time.sleep(5)

    while forest.any_predator_left() and forest.hunting_possible:
        forest.start_hunting()

    print("Has anyone survived?")
    forest.print_animal_note()
