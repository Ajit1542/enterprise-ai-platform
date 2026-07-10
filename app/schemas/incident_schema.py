from pydantic import BaseModel
from typing import Literal

class IncidentCreate(BaseModel):
    incident_id: str
    short_description: str
    priority: Literal["Low", "Medium", "High", "Critical"]