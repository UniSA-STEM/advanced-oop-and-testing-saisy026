"""
File: enclosure.py
Description: A brief description of this Python module.
Author: Suruchi saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal

class Enclosure:
    def __init__(self, enclosure_id, size, environment_type, max_capacity):
        if not enclosure_id or not isinstance(enclosure_id, str):
            raise ValueError("Enclosure ID must be string")
        if not isinstance(size, (int, float)) or size <= 0:
            raise ValueError("Size must be a positive number")
        if not environment_type or not isinstance(environment_type, str):
            raise ValueError("Environment type must be string")
        if not isinstance(max_capacity, int) or max_capacity <= 0:
            raise ValueError("Max capacity must be a positive integer")

        self._enclosure_id = enclosure_id
        self._size = size
        self._environment_type = environment_type
        self._max_capacity = max_capacity
        self._animals = []
        self._cleanliness = 100
        self._allowed_category = None

# Getters
    def get_enclosure_id(self):
        return self._enclosure_id

    def get_environment_type(self):
        return self._environment_type

    def get_cleanliness(self):
        return self._cleanliness

    def get_animals(self):
        return self._animals.copy()

    def get_current_occupancy(self):
        return len(self._animals)

    def get_max_capacity(self):
        return self._max_capacity

    def is_full(self):
        return len(self._animals) >= self._max_capacity

    def clean(self,cleanliness_increase):
        cleanliness_increase = 50
        self._cleanliness = min(100, self._cleanliness + cleanliness_increase)
        return f" Enclosure {self._enclosure_id} cleaned. Cleanliness now: {self._cleanliness}% "

    def reduce_cleanliness(self,amount):
        amount = 10
        self._cleanliness = max(0, self._cleanliness - amount)

    def can_add_animal(self, animal):
        if not isinstance(animal, Animal):
            return False
        if self.is_full():
            return False
        if animal.get_required_environment().lower() != self._environment_type.lower():
            return False
        if self._allowed_category is None:
            return True
        return animal.get_category() == self._allowed_category

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise ValueError("Only Animal objects can be added")
        if animal.get_enclosure() is not None:
            raise ValueError(f"{animal.get_name()} is already in another enclosure")
        if animal.is_under_treatment():
            raise ValueError(f"{animal.get_name()} is under treatment and cannot be moved")
        if not self.can_add_animal(animal):
            raise ValueError(f"Cannot add {animal.get_species()} to {self._enclosure_id}")

        self._animals.append(animal)
        if self._allowed_category is None:
            self._allowed_category = animal.get_category()

        animal.set_enclosure(self)
        self.reduce_cleanliness(5)
        return f"{animal.get_name()} added to {self._enclosure_id}"

    def remove_animal(self, animal):
        if animal not in self._animals:
            raise ValueError(f"{animal.get_name()} not in this enclosure")

        self._animals.remove(animal)
        animal.remove_from_enclosure()  # Clean way
        if not self._animals:
            self._allowed_category = None
        return f"{animal.get_name()} removed from {self._enclosure_id}"

    def __str__(self):
        animal_list = ", ".join([a.get_name() for a in self._animals]) or "Empty"
        return (f"Enclosure {self._enclosure_id}\n"
                f"Type: {self._environment_type}\n"
                f"Occupancy: {len(self._animals)}/{self._max_capacity}\n"
                f"Cleanliness: {self._cleanliness}%\n"
                f"Animals: {animal_list}")


