from app.repositories.incident_repository import IncidentRepository

class IncidentService:
    def __init__(self):
        self.repository = IncidentRepository()
    def create_incident(self, incident: dict):
        """Creates a new incident and saves it to the repository."""

        #Buisness logic can be added here, e.g., validation, transformation, etc.
        incident["status"] = "Open"  # Default status for new incidents
        self.repository.save(incident)

        return {
            "message": "Incident created successfully",
            "incident_id": incident["incident_id"]

        }
    def get_all_incidents(self) -> list[dict]:
        """Retrieve all incidents from the repository."""
        return self.repository.get_all()