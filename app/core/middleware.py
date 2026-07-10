import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logger import get_logger

logger = get_logger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware responsible for:
    - Generating a Request ID
    - Logging incoming requests
    - Measuring request processing time
    - Logging outgoing responses
    - Logging unexpected exceptions
    """

    async def dispatch(self, request: Request, call_next):

        # Generate a unique request ID
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id
        client_ip = request.client.host if request.client else "unknown"
        user_agent = request.headers.get("user-agent", "unknown")
        # Start timer
        start_time = time.perf_counter()

        logger.info(
            "Incoming Request | Request ID=%s | Client_IP=%s | User-Agent=%s | Method=%s | Path=%s",
            request_id,
            client_ip,
            user_agent,
            request.method,
            request.url.path,
        )

        try:
            response = await call_next(request)

        except Exception:
            logger.exception(
                "Unhandled exception | Request ID=%s | Method=%s | Path=%s",
                request_id,
                request.method,
                request.url.path,
            )
            raise

        processing_time = (time.perf_counter() - start_time) * 1000

        logger.info(
            "Outgoing Response | Request ID=%s | Status=%d | Duration=%.2f ms",
            request_id,
            response.status_code,
            processing_time,
        )

        return response