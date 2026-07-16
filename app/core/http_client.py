import httpx

from app.core.config import settings
from app.core.logger import get_logger

logger = get_logger(__name__)

_http_client = httpx.Client(
    base_url=settings.OLLAMA_BASE_URL,
    timeout=30.0,
)


def get_http_client() -> httpx.Client:
    """
    Return the shared HTTP client instance.

    The same client is reused throughout the application to
    benefit from connection pooling and improved performance.
    """
    return _http_client