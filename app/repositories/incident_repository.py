import csv
import os
from typing import Optional


class IncidentRepository:
    FILE_PATH = "data/incidents.csv"

    def save(self, incident: dict):
        """Save an incident to CSV."""
        file_exists = os.path.isfile(self.FILE_PATH)

        with open(self.FILE_PATH, mode="a", newline="", encoding="utf-8") as file:
            fieldnames = [
                "incident_id",
                "short_description",
                "priority",
                "status",
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow(incident)
    def get_all(self) -> list[dict]:
        """"Retrieve all incidents.."""
        if not os.path.isfile(self.FILE_PATH):
            return []

        with open(self.FILE_PATH, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            incidents = []
            for row in reader:
                incidents.append(row)
            return incidents