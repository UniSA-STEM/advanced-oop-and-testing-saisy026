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

