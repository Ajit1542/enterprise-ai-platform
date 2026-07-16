import copy
from app.repositories.incident_repository import IncidentRepository
from app.services.ai_service import AIService
from app.core.logger import get_logger
from app.intelligence.exceptions import LLMError
logger = get_logger(__name__)

class IncidentService:
    def __init__(self):
        self.repository = IncidentRepository()
        self.ai_service = AIService()
    def create_incident(self, incident: dict):
        """Creates a new incident and saves it to the repository."""
        logger.info("Creating a new incident with ID=%s", incident["incident_id"])
        #Buisness logic can be added here, e.g., validation, transformation, etc.
        incident["status"] = "Open"  # Default status for new incidents
        incident_for_ai = copy.deepcopy(incident)
        # save incident
        self.repository.save(incident)
        #Generate AI summary 
        try :
            ai_result = self.ai_service.analyze_incident(incident_for_ai)
            self.repository.update_ai_result(incident["incident_id"],ai_result)
            logger.info(
                "AI summary generated successfully | Incident ID = %s",
                incident["incident_id"],
            )
        except LLMError as e:
            logger.exception("AI summary generation failed | Incident ID = %s",
                             incident["incident_id"],
                             )
            failed_ai_result = {
                "status":"FAILED",
                "summary": None,
                "error":str(e)
            }
            self.repository.update_ai_result(
                incident["incident_id"],
                failed_ai_result,
            )

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
    
