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

        self._description = description
        self._date_recorded = date_recorded
        self._severity = severity
        self._treatment = treatment
