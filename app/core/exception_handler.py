from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.logger import get_logger

logger = get_logger(__name__)

async def global_exception_handler(request: Request, exc: Exception):
    """
    Handle all unhandled exceptions in the application.

    Logs the exception and returns a standardized
    HTTP 500 response.
    """
    request_id = getattr(request.state, "request_id", "N/A")
    logger.exception(
    "Unhandled exception | Request ID=%s | Method=%s | Path=%s | Error=%s",
    request_id,
    request.method,
    request.url.path,
    str(exc),
    )
    return JSONResponse(
    status_code=500,
    content={
        "success": False,
        "message": "Internal Server Error",
        "request_id": request_id,
    },
    )