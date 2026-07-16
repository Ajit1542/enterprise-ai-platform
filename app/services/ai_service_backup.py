from app.intelligence.llm_factory import get_llm_client
from app.core.logger import get_logger
from app.intelligence.prompts.incident_summary import build_summary_prompt

logger = get_logger(__name__)
class AIService:
    """
Service responsible for generating AI-powered incident summaries.

This service builds the appropriate prompt,
invokes the configured LLM client,
and returns the normalized AI response.
"""
    def __init__(self):
        self.client = get_llm_client()

    def generate_summary(self, incident: dict) -> dict:
        """
    Generate an AI summary for the provided incident.

    Args:
        incident: Incident details.

    Returns:
        Standardized AI response from the configured LLM client.
    """
        logger.info("Generating AI Summary | Incident ID = %s",
                    incident["incident_id"],
                    )
        prompt = build_summary_prompt(incident)
        result = self.client.generate(prompt)
        logger.info(
                    "AI summary generated successfully | Incident ID=%s",
                    incident["incident_id"],
                    )
        return result
        