# Sprint 1 - Incident Creation

## Objective

Build the foundation of an enterprise backend using Layered Architecture.

---

## Architecture

Client
        │
        ▼
FastAPI API Layer
        │
        ▼
Service Layer
        │
        ▼
Repository Layer
        │
        ▼
CSV Storage/MongoDB/ServiceNow

---

## Responsibilities

### API Layer

- Accept HTTP requests.
- Validate incoming data using Pydantic.
- Call the Service Layer.
- Return HTTP responses.

The API should never contain business logic.

---

### Service Layer

Responsible for business logic.

Examples:

- Default incident status = Open
- Duplicate validation
- AI summary generation (future)
- Event publishing (future)

The Service Layer coordinates the application.

---

### Repository Layer

Responsible for data access only.

Responsibilities:

- Read data
- Write data
- Update data
- Delete data

The Repository does not contain business rules.

---

## Design Principles Learned

- Separation of Concerns
- Layered Architecture
- Repository Pattern
- Single Responsibility Principle

---

## Input Validation vs Business Validation

Input Validation

Performed in API Layer using Pydantic.

Examples:

- Required fields
- Enum validation
- Data types

Business Validation

Performed in Service Layer.

Examples:

- Duplicate Incident IDs
- Status assignment
- Team assignment

# Sprint 2 - Incident Retrieval

## User Story

As a Service Desk Analyst,
I want to retrieve incidents,
so that I can monitor them.

---

## Flow

Browser

↓

GET /api/v1/incidents

↓

API Layer

↓

Incident Service

↓

Incident Repository

↓

CSV

---

## Repository Design

Repository returns Python dictionaries instead of CSV objects.

Reason:

The Service Layer should not know whether data comes from:

- CSV
- PostgreSQL
- MongoDB
- ServiceNow

This abstraction allows storage implementation to change without affecting business logic.

---

## Why Repository Returns List[dict]

Repository should expose business-friendly Python objects instead of storage-specific objects.

Good

List[dict]

Bad

csv.DictReader

file object

database cursor

---

## Empty Data Handling

If CSV does not exist:

Return:

[]

Reason:

No incidents is a valid business state.

Exceptions should represent unexpected failures, not expected situations.

---

## Pagination Discussion

Instead of:

GET /incidents

Enterprise APIs use:

GET /incidents?page=1&size=20

Reasons:

- Better performance
- Reduced memory usage
- Lower network bandwidth
- Better user experience

# Sprint 3 - Observability

## Completed

- Implemented centralized logging utility
- Configured rotating file handler
- Added API layer logging
- Added Service layer logging
- Added Repository layer logging
- Implemented Request Logging Middleware
- Generated unique Request ID for every request
- Measured API processing time
- Added Global Exception Handler
- Standardized HTTP 500 error responses
- Logged stack traces using logger.exception()

## Engineering Learnings

- Middleware executes before and after every request.
- Request IDs help correlate logs across layers.
- Repository raises exceptions instead of returning HTTP responses.
- Exception handling belongs at the application boundary.
- Logging is a cross-cutting concern and should be centralized.
- `time.perf_counter()` is better suited for measuring elapsed time than `time.time()`.
- Lower layers raise exceptions; higher layers decide how to present them.
# Sprint 4 - MongoDB Migration

## Completed

- Replaced CSV repository implementation with MongoDB
- Added centralized MongoDB connection module
- Added configuration management using .env
- Introduced Settings class for application configuration
- Successfully migrated without changing API or Service layers
- Verified repository pattern by swapping storage implementation only

## Engineering Learnings

- Repository abstracts the storage implementation.
- MongoClient should be created once and reused.
- Configuration belongs in .env and config.py.
- MongoDB collections are dependencies initialized in the repository.
- Layered architecture minimizes the impact of infrastructure changes.