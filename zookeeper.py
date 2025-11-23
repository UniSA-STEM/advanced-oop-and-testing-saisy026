"""
File: zookeeper.py
Description: A brief description of this Python module.
Author: Suruchi saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Integrity Policy.
"""
from staff import Staff

class Zookeeper(Staff):
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id,"zookeeper")
