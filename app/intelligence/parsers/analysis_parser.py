#parser that:
# Validates the AI response.
# Parses it into a Python dictionary.
# Raises a custom exception if the JSON is invalid.
# Prevents bad AI output from corrupting MongoDB.

import json

from app.core.logger import get_logger
from app.intelligence.exceptions import InvalidLLMResponseError

logger = get_logger(__name__)

REQUIRED_ANALYSIS_FIELDS = [
    "summary",
    "root_cause",
    "assignment_group",
    "severity",
    "confidence",
    "recommendation",
]


def parse_analysis_response(response: str) -> dict:
    """
    Parse and validate the AI analysis response.

    Args:
        response: Raw JSON string returned by the LLM.

    Returns:
        Parsed dictionary.

    Raises:
        InvalidLLMResponseError
    """

    logger.info("Parsing AI analysis response.")

    try:
        result = json.loads(response)

    except json.JSONDecodeError as e:
        logger.exception("Invalid JSON received from LLM.")
        raise InvalidLLMResponseError(
            "LLM returned invalid JSON."
        ) from e

    for field in REQUIRED_ANALYSIS_FIELDS:

        if field not in result:

            logger.error(
                "Missing required field '%s' in AI response.",
                field,
            )

            raise InvalidLLMResponseError(
                f"Missing required field: {field}"
            )

    logger.info("AI response parsed successfully.")

    return result
