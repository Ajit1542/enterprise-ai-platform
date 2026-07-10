from app.core.logger import get_logger
from app.database.mongodb import get_incident_collection


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