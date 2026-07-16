from app.core.logger import get_logger
from app.database.mongodb import get_incident_collection
from pymongo.errors import PyMongoError

logger = get_logger(__name__)


class IncidentRepository:
    """
    Repository responsible for all Incident database operations.
    """

    def __init__(self):
        """
        Initialize the MongoDB collection.
        """
        self.collection = get_incident_collection()

    def save(self, incident: dict):
        """
        Save a new incident to MongoDB.

        Args:
            incident (dict): Incident data.

        Returns:
            InsertOneResult: MongoDB insert result.
        """
        logger.info(
            "Saving incident. Incident ID=%s",
            incident["incident_id"],
        )

        result = self.collection.insert_one(incident)

        logger.info(
            "Incident saved successfully. Incident ID=%s Mongo ID=%s",
            incident["incident_id"],
            result.inserted_id,
        )

        return result

    def get_all(self) -> list[dict]:
        """
        Retrieve all incidents from MongoDB.

        Returns:
            list[dict]: List of incidents.
        """
        logger.info("Reading incidents from MongoDB.")

        incidents = list(
            self.collection.find({}, {"_id": 0})
        )

        logger.info(
            "Successfully loaded %d incidents from MongoDB.",
            len(incidents),
        )

        return incidents
    def update_ai_result(self,incident_id:str,ai_result:dict)->None:
        logger.info("Updating AI summary for Incidnet ID = %s",
                    incident_id,)
        try:
            result = self.collection.update_one(
                {"incident_id": incident_id},
                {
                    "$set": {
                        "ai": ai_result
                    }
                }
            )

            if result.matched_count == 0:
                logger.Warning("No Records found | Incident ID = %s",incident_id)
                
            else:
                logger.info("AI result updated successfully | Incident ID=%s",
                incident_id,)
                
        except PyMongoError:
            logger.exception(
                    "Failed to update AI result | Incident ID=%s",
                    incident_id,
                )
            raise

        