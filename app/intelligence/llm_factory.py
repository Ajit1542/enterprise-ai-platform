from app.core.config import settings
from app.intelligence.clients.base_llm_client import BaseLLMClient
from app.intelligence.clients.ollama_client import OllamaClient
from app.intelligence.exceptions import UnsupportedLLMProviderError


def get_llm_client() -> BaseLLMClient:
    """
    Return the configured LLM client.

    The provider is selected using the application configuration.
    """

    provider = settings.LLM_PROVIDER.lower()

    if provider == "ollama":
        return OllamaClient()

    raise UnsupportedLLMProviderError(
        f"Unsupported LLM provider: {provider}"
    )