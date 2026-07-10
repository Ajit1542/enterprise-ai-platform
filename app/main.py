from fastapi import FastAPI
from app.api.v1.endpoints.incident import router as incident_router
from app.core.logger import get_logger
from app.core.middleware import RequestLoggingMiddleware
from app.core.exception_handler import global_exception_handler


logger = get_logger(__name__)

logger.info("**********************************")
logger.info("Starting the FastAPI application.")

# initialize FastAPI application
app = FastAPI(
    title="Enterprise AI Incident Automation Platform",
    version="1.0.0",
) # This line initializes a FastAPI application instance, which will be used to define routes and handle incoming HTTP requests.'''We're creating the application object.Later Uvicorn will run this object.Everything in our project revolves around this app.'''

# Add the request logging middleware to the FastAPI application
app.add_middleware(RequestLoggingMiddleware)  

# Add a global exception handler to catch unhandled exceptions and return a standardized error response
app.add_exception_handler(Exception, global_exception_handler)

# Include the incidents router with a prefix for versioning
app.include_router(
    incident_router,
    prefix="/api/v1",
    tags=["Incidents"]
    )  

# Define a root endpoint that returns basic information about the application
@app.get("/")
def root():
    return {
        "application": "Enterprise AI Incident Automation Platform",
        "version": "1.0.0",
        "status": "running"
    }
# Define a health check endpoint that returns the health status of the application
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

