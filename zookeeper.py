"""
File: zookeeper.py
Description: A brief description of this Python module.
Author: Suruchi saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Integrity Policy.
"""
from staff import Staff
from enclosure import Enclosure
from animal import Animal

class Zookeeper(Staff):
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id,"zookeeper")

    def clean_enclosure(self, enclosure):
        if not isinstance(enclosure, Enclosure):
            raise ValueError("Invalid enclosure")
        if enclosure not in self._assigned_enclosures:
            return f"{self._name} is not assigned to clean enclosure {enclosure.get_enclosure_id()}"
        return f"Zookeeper {self._name} {enclosure.clean()}"

    def feed_animal(self, animal):
        if not isinstance(animal, Animal):
            raise ValueError("Invalid animal")

        # Check if animal is in any enclosure this zookeeper is assigned to
        animal_enclosure = animal.get_enclosure()
        if animal_enclosure and animal_enclosure in self._assigned_enclosures:
            return f"Zookeeper {self._name} feeds {animal.get_name()}: {animal.eat()}"
        else:
            return f"{self._name} is not responsible for feeding {animal.get_name()}"


