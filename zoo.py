"""
File: zoo.py
Description: A brief description of this Python module.
Author: Suruchi saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal
from datetime import datetime

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

    def add_staff(self, staff):
        self._staff.append(staff)

    def generate_animal_report(self):
        print(f"\n Animal Report for {self._name}")
        for animal in self._animals:
            enc = animal.get_enclosure().get_enclosure_id() if animal.get_enclosure() else "None"
            status = animal.get_health_status()
            print(f"Name: {animal.get_name()}\n"
                  f"Species: {animal.get_species()}\n"
                  f"Age: {animal.get_age()}\n"
                  f"Enclosure: {enc}\n"
                  f"Health: {status}")

    def generate_enclosure_report(self):
        print(f"\n Enclosure Status Report")
        for enc in self._enclosures:
            print(enc)

    def get_animals_needing_attention(self):
        return [a for a in self._animals if a.is_under_treatment()]


