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
            raise ValueError("Employee ID must be positive Integer")
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
        if not isinstance(animal, Animal):
            raise ValueError("Can only assign Animal")
        if animal not in self._assigned_animals:
            self._assigned_animals.append(animal)

    def assign_to_enclosure(self, enclosure):
        if not isinstance(enclosure, Enclosure):
            raise ValueError("Can only assign Enclosure")
        if enclosure not in self._assigned_enclosures:
            self._assigned_enclosures.append(enclosure)

