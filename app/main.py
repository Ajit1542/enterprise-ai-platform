from fastapi import FastAPI
from app.api.v1.endpoints.incident import router as incident_router

app = FastAPI(
    title="Enterprise AI Incident Automation Platform",
    version="1.0.0",
) 
# This line initializes a FastAPI application instance, which will be used to define routes and handle incoming HTTP requests.
'''We're creating the application object.Later Uvicorn will run this object.Everything in our project revolves around this app.'''

app.include_router(
    incident_router,
    prefix="/api/v1",
    tags=["Incidents"]
    )  
# Include the incidents router with a prefix for versioning

@app.get("/")
def root():
    return {
        "application": "Enterprise AI Incident Automation Platform",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

