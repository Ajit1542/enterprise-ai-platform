from app.core.logger import get_logger
from app.intelligence.llm_factory import get_llm_client
from app.intelligence.prompts.incident_analysis import build_analysis_prompt
from app.intelligence.parsers.analysis_parser import parse_analysis_response

logger = get_logger(__name__)


class AIService:
    """
    Service responsible for AI-powered incident analysis.
    """

    def __init__(self):
        self.client = get_llm_client()

    def analyze_incident(self, incident: dict) -> dict:
        """
        Analyze an incident using the configured LLM.

        Args:
            incident: Incident details.

        Returns:
            Standardized AI analysis result.
        """

        logger.info(
            "Generating AI analysis | Incident ID=%s",
            incident["incident_id"],
        )

        # Step 1: Build Prompt
        prompt = build_analysis_prompt(incident)
        try:

        # Step 2: Call LLM
            llm_response = self.client.generate(prompt)

            # Step 3: Parse Response
            analysis = parse_analysis_response(
                llm_response["content"]
            )

            logger.info(
                "AI analysis generated successfully | Incident ID=%s",
                incident["incident_id"],
            )
        except Exception : 
            logger.exception("AI summary generation failed | Incident ID = %s",
                             incident["incident_id"],)
            raise
        # Step 4: Standardize Result
        return {
            "status": "SUCCESS",
            "analysis": analysis,
            "provider": llm_response["metadata"]["provider"],
            "model": llm_response["metadata"]["model"],
            "latency_ns": llm_response["metadata"]["latency_ns"],
        }