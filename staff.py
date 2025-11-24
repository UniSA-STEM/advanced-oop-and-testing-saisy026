"""
File: staff.py
Description: A brief description of this Python module.
Author: Suruchi saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal
from enclosure import Enclosure
from health_record import HealthRecord

class Staff:
    def __init__(self, name, employee_id, role):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be string")
        if not employee_id or not isinstance(employee_id, str):
            raise ValueError("Employee ID must be a string")
        if role not in ["zookeeper", "veterinarian"]:
            raise ValueError("Role must be 'zookeeper' or 'veterinarian'")

        self._name = name
        self._employee_id = employee_id
        self._role = role
        self._assigned_animals = []  # Animals staff member looks after
        self._assigned_enclosures = []  # Enclosures staff member is responsible for

# Getters

    def get_name(self):
        return self._name

    def get_role(self):
        return self._role

    def get_assigned_animals(self):
        return self._assigned_animals

    def get_assigned_enclosures(self):
        return self._assigned_enclosures

# Assign methods

    def assign_to_animal(self, animal):
        if self._role != "veterinarian":
            raise ValueError(f"Only veterinarians can be assigned to individual animals, not {self._role}s")
        if not isinstance(animal, Animal):
            raise ValueError("Can only assign an Animal object")
        if animal not in self._assigned_animals:
            self._assigned_animals.append(animal)
        return True  # Optional: makes it clear it succeeded

    def assign_to_enclosure(self, enclosure):
        if self._role != "zookeeper":
            raise ValueError(f"Only zookeepers can be assigned to enclosures, not {self._role}s")
        if not isinstance(enclosure, Enclosure):
            raise ValueError("Can only assign an Enclosure object")
        if enclosure not in self._assigned_enclosures:
            self._assigned_enclosures.append(enclosure)
        return True

# Basic action

    def feed_animal(self, animal):
        if animal not in self._assigned_animals:
            return f"{self._name} is not assigned to care for {animal.get_name()}"
        return f"{self._name} ({self._role}) feeds {animal.get_name()}: {animal.eat()}"

# String representation

    def __str__(self):
        return (f"{self._role.capitalize()}: {self._name}\n"
                f"ID: {self._employee_id}")