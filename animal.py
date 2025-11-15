"""
File: filename.py
Description: A brief description of this Python module.
Author: Suruchi saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Animal:
    def __init__(self, name, species, age, dietary_needs, category, required_environment  ):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not species or not isinstance(species, str):
            raise ValueError("Species must be a string")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer")
        if not dietary_needs or not isinstance(dietary_needs, str):
            raise ValueError("Dietary needs must be a string")
        if not category or not isinstance(category, str):
            raise ValueError("Category must be a string")
        if not required_environment or not isinstance(required_environment, str):
            raise ValueError("Environment required must be a non-empty string")

        self._name = name
        self._species = species
        self._age = age
        self._dietary_needs = dietary_needs
        self._category = category
        self._required_environment = required_environment
        self._health_records = []
        self._enclosure = None

