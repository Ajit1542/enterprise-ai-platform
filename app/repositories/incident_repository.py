import csv
import os
# from typing import Optional
from app.core.logger import get_logger

logger = get_logger(__name__)


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
            logger.info(
                "Incident saved successfully. Incident ID=%s Priority=%s Status=%s",
                incident["incident_id"],
                incident["priority"],
                incident["status"]   
            )
             
    def get_all(self) -> list[dict]:
        """"Retrieve all incidents.."""
        logger.info("Reading incidents from CSV.")
        if not os.path.isfile(self.FILE_PATH):
            logger.warning(f"File {self.FILE_PATH} does not exist. Returning empty list.")
            return []
        try:
            with open(self.FILE_PATH, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                incidents = []
                for row in reader:
                    incidents.append(row)
                logger.info(
                    "Successfully loaded %d incidents from CSV.",
                    len(incidents)
                )
                # raise Exception("Testing Global Exception Handler")
            
                return incidents
        except Exception as e:
            logger.exception("Error reading incidents from CSV: %s", str(e))
            raise

        