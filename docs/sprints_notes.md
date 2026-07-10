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
CSV Storage

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