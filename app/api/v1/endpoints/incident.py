from fastapi import APIRouter
from app.services.incident_service import IncidentService
from app.schemas.incident_schema import IncidentCreate
#create router and service instances
router = APIRouter()
incident_service = IncidentService()

#create post endpoint receive an incidentCreate object and call the service to create an incident  

@router.post("/incidents")
def create_incident(incident: IncidentCreate):
    """
    Create a new incident.

    Receives an incident details from the client,
    passes them to the service for creation.
    Returns a success message and the created incident details.
    """
    return incident_service.create_incident(incident.model_dump())

@router.get("/incidents")
def get_all_incidents():
    """
    Retrieve all incidents.

    Calls the service to fetch all incidents from the repository.
    Returns a list of incidents.
    """
    return incident_service.get_all_incidents()