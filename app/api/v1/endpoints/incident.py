from fastapi import APIRouter
from app.services.incident_service import IncidentService
from app.schemas.incident_schema import IncidentCreate
from app.core.logger import get_logger

#create router and service instances
router = APIRouter()
incident_service = IncidentService()
logger = get_logger(__name__)
#create post endpoint receive an incidentCreate object and call the service to create an incident  

@router.post("/incidents")
def create_incident(incident: IncidentCreate):
    """
    Create a new incident.

    Receives an incident details from the client,
    passes them to the service for creation.
    Returns a success message and the created incident details.
    """
    logger.info("Received request to create incident with ID=%s", incident.incident_id)
    return incident_service.create_incident(incident.model_dump())

@router.get("/incidents")
def get_all_incidents():
    """
    Retrieve all incidents.

    Calls the service to fetch all incidents from the repository.
    Returns a list of incidents.
    """
    logger.info("Received request to fetch all incidents.")
    return incident_service.get_all_incidents()