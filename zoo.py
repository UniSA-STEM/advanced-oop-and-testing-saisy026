"""
File: zoo.py
Description: A brief description of this Python module.
Author: Suruchi saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Zoo:
    def __init__(self):
        self._name = 'Oop Zoo'
        self._animals = []
        self._enclosures = []
        self._staff = []

    def add_animal(self, animal):
        if animal in self._animals:
            return False
        self._animals.append(animal)
        return True

    def add_enclosure(self, enclosure):
        if enclosure in self._enclosures:
            return False
        self._enclosures.append(enclosure)
        return True

