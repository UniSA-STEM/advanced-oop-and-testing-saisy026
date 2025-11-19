"""
File: filename.py
Description: A brief description of this Python module.
Author: Suruchi saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Integrity Policy.
"""
from datetime import date

class HealthRecord:
    def __init__(self, description, date_recorded, severity, treatment):
        if not description:
            raise ValueError("Description required")
        if not isinstance(date_recorded, date):
            raise ValueError("Invalid date")
        if severity not in range(1, 11):
            raise ValueError("Severity must be 1–10")
        if treatment is not None and not isinstance(treatment, str):
            raise ValueError("Treatment must be a string or None.")

        self._description = description
        self._date_recorded = date_recorded
        self._severity = severity
        self._treatment = treatment

# Getters
    def get_description(self):
        return self._description

    def get_date_recorded(self):
        return self._date_recorded

    def get_severity(self):
        return self._severity

    def get_treatment(self):
        return self._treatment

# Setters
    def set_treatment(self, treatment):
        if not isinstance(treatment, str):
            raise ValueError("Treatment must be a string")
        self._treatment = treatment

# String display method
    def __str__(self):
        return (f"Date: {self._date_recorded}"
                f"Severity level: {self._severity} "
                f"Description: {self._description} "
                f"Treatment: {self._treatment or 'None'}")
