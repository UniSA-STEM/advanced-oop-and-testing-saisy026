"""
File: staff.py
Description: A brief description of this Python module.
Author: Suruchi saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Integrity Policy.
"""
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
