"""
File: veterinarian.py
Description: A brief description of this Python module.
Author: Suruchi saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Integrity Policy.
"""
from staff import Staff
from animal import Animal
from health_record import HealthRecord
from datetime import date

class Veterinarian(Staff):
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id, "veterinarian")

    def perform_health_check(self, animal):
        if not isinstance(animal, Animal):
            raise ValueError("Invalid animal")
        return f"Veterinarian {self._name} performs a full health check on {animal.get_name()} (Age: {animal.get_age()})"

    def record_health_issue(self, animal, description, severity, treatment = None):
        if not isinstance(animal, Animal):
            raise ValueError("Invalid animal")
        if severity not in range(1, 11):
            raise ValueError("Severity must be between 1 and 10")
        record = HealthRecord(description, date.today(), severity, treatment)
        animal.add_health_record(record)
        return f"Vet {self._name} recorded a severity {severity} issue for {animal.get_name()} on {date.today()}."
