class LLMError(Exception):
    """Base exception for all LLM errors."""
    ...


class LLMConnectionError(LLMError):
    """Raised when the LLM cannot be reached."""
    ...


class LLMTimeoutError(LLMError):
    """Raised when the request times out."""
    ...


class InvalidLLMResponseError(LLMError):
    """Raised when the LLM returns an invalid response."""
    ...

class UnsupportedLLMProviderError(LLMError):
    """Raised when the configured LLM provider is not supported."""
    ...