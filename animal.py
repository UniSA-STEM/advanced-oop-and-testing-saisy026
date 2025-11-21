"""
File: animal.py
Description: A brief description of this Python module.
Author: Suruchi saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Integrity Policy.
"""
from health_record import HealthRecord

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
        self._health_status = "healthy"

# Getters
    def get_name(self):
        return self._name

    def get_species(self):
        return self._species

    def get_age(self):
        return self._age

    def get_dietary_needs(self):
        return self._dietary_needs

    def get_category(self):
        return self._category

    def get_required_environment(self):
        return self._required_environment

    def get_enclosure(self):
        return self._enclosure

    def get_health_status(self):
        return self._health_status

    def is_under_treatment(self):
        return self._health_status == "under treatment"

# Health management
    def add_health_record(self, record):
        if not isinstance(record, HealthRecord):
            raise ValueError("Must be a HealthRecord object")
        self._health_records.append(record)
        if record.get_severity() > 5:
            self._health_status = "under treatment"

# Basic actions
    def make_sound(self):
        return "Some specific animal sound"

    def eat(self):
        return f"{self._name} is eating {self._dietary_needs}"

    def sleep(self):
        return f"{self._name} is sleeping"
