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

