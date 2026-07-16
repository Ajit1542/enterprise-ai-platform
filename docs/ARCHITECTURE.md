## Architecture

Presentation Layer
      ↓
FastAPI

Business Layer
      ↓
Incident Service

Data Layer
      ↓
Incident Repository

Storage Layer
      ↓
CSV



## Components Responsiblities
### API Layer
Responsibilities:
- Receive requests
- Validate input
- Call the service
- Return responses

Should NOT:
- Contain business logic
- Access CSV or database directly

### Service Layer
Responsibilities:
- Business rules
- Orchestrate workflows
- Call repositories and integrations

### Repository Layer
Responsibilities:
- Read/write data
- Hide storage implementation from the service layer

Key takeaway:
The service should not know whether data is stored in a CSV, PostgreSQL, or ServiceNow.


## API FLOW

## Logger.py

logger.py is responsible for configuring the application's logging system.

It should:

1. Create logger instances.
2. Configure log format.
3. Configure log level.
4. Configure console logging.
5. Configure file logging.
6. Return configured logger instances.

## FINAL Architecture

                   FastAPI
                      │
        ┌─────────────┴─────────────┐
        │                           │
   Middleware                Exception Handler
        │
        ▼
      API Layer
        │
        ▼
    Service Layer
        │
        ├──────────────┐
        ▼              ▼
 Repository         AI Engine
        │              │
        ▼              ▼
 PostgreSQL      Ollama (LLM)
        │              │
        └──────┬───────┘
               ▼
          RAG Pipeline
               │
               ▼
             Kafka
               │
               ▼
         Notification Service


## After Integrating AI 

                FastAPI
                   │
                   ▼
          IncidentService
          (Business Workflow)
          ┌─────────┴─────────┐
          ▼                   ▼
 Repository             AIService
     │                      │
     ▼                      ▼
 MongoDB             Prompt Builder
                            │
                            ▼
                      LLM Factory
                            │
                            ▼
                      Ollama Client
                            │
                            ▼
                       HTTP Client
                            │
                            ▼
                         Ollama