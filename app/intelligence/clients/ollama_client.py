from typing import Any

import httpx

from app.core.config import settings
from app.core.http_client import get_http_client
from app.core.logger import get_logger

from app.intelligence.clients.base_llm_client import BaseLLMClient
from app.intelligence.exceptions import (
    InvalidLLMResponseError,
    LLMConnectionError,
    LLMTimeoutError,
)

logger = get_logger(__name__)

required_fields = [
    "response",
    "model",
    "total_duration",
]

class OllamaClient(BaseLLMClient):
    """
    Client responsible for communicating with the Ollama API.
    """

    def __init__(self):
        self.client = get_http_client()
        self.model = settings.OLLAMA_MODEL

    def _build_payload(self, prompt: str) -> dict[str, Any]:
        """
        Build the request payload expected by Ollama.
        """
        return {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }

    def generate(self, prompt: str) -> dict[str, Any]:
        """
        Generate a response from Ollama.
        """
        payload = self._build_payload(prompt)

        logger.info(
            "Generating AI response | Provider=%s | Model=%s",
            settings.LLM_PROVIDER,
            self.model,
        )

        try:
            response = self.client.post(
                "/api/generate",
                json=payload,
            )

            response.raise_for_status()

        except httpx.ConnectError as exc:
            logger.exception("Unable to connect to Ollama.")
            raise LLMConnectionError(
                "Unable to connect to Ollama."
            ) from exc

        except httpx.TimeoutException as exc:
            logger.exception("Ollama request timed out.")
            raise LLMTimeoutError(
                "Ollama request timed out."
            ) from exc

        except httpx.HTTPStatusError as exc:
            logger.exception(
                "Ollama returned HTTP status %s",
                exc.response.status_code,
            )
            raise InvalidLLMResponseError(
                f"Ollama returned HTTP {exc.response.status_code}"
            ) from exc

        response_json = response.json()
        
        
        for field in required_fields:
            if field not in response_json:
                logger.error("Invalid response received from Ollama.")
                raise InvalidLLMResponseError(
                    "Missing 'response' field in Ollama response."
                )

        logger.info(
                "AI response generated successfully | Model=%s",
                self.model,
            ) 

        return {
            "success": True,
            "content": response_json["response"],
            "metadata": {
                "provider": settings.LLM_PROVIDER,
                "model": response_json.get("model"),
                "created_at": response_json.get("created_at"),
                "latency_ns": response_json.get("total_duration"),
                "prompt_tokens": response_json.get("prompt_eval_count"),
                "completion_tokens": response_json.get("eval_count"),
            },
        }