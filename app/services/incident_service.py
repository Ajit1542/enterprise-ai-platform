from app.repositories.incident_repository import IncidentRepository
from app.core.logger import get_logger

logger = get_logger(__name__)

class IncidentService:
    def __init__(self):
        self.repository = IncidentRepository()
    def create_incident(self, incident: dict):
        """Creates a new incident and saves it to the repository."""
        logger.info("Creating a new incident with ID=%s", incident["incident_id"])
        #Buisness logic can be added here, e.g., validation, transformation, etc.
        incident["status"] = "Open"  # Default status for new incidents
        self.repository.save(incident)
        logger.info(
            "Incident created successfully. Incident ID=%s Priority=%s Status=%s",
            incident["incident_id"],
            incident["priority"],
            incident["status"]
        )
        return {
            "message": "Incident created successfully",
            "incident_id": incident["incident_id"]
        }
    def get_all_incidents(self) -> list[dict]:
        """Retrieve all incidents from the repository."""
        logger.info("Fetching all incidents from the repository.")
        return self.repository.get_all()