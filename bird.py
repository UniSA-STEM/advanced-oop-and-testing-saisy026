"""
File: bird.py
Description: A brief description of this Python module.
Author: Suruchi saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal

class Bird(Animal):
    def __init__(self, name, species, age,dietary_needs, required_environment):
        super().__init__(name,species,age,dietary_needs,"bird",required_environment)

    def make_sound(self):
        return f"{self.get_name()} chirps!"
