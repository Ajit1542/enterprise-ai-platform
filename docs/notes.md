# Day 1

## FastAPI
- FastAPI is the web framework that exposes our application as REST APIs.
- Uvicorn is the ASGI server that runs the FastAPI app.

## API Layer
Responsibilities:
- Receive requests
- Validate input
- Call the service
- Return responses

Should NOT:
- Contain business logic
- Access CSV or database directly

## Service Layer
Responsibilities:
- Business rules
- Orchestrate workflows
- Call repositories and integrations

## Repository Layer
Responsibilities:
- Read/write data
- Hide storage implementation from the service layer

Key takeaway:
The service should not know whether data is stored in a CSV, PostgreSQL, or ServiceNow.

## Why use Pydantic?
"Pydantic validates incoming data at the API boundary, ensuring malformed requests never reach the business layer. This keeps the service layer focused on business logic rather than input validation."

# Difference between Input Validation and Business Validation

## Input Validation (API Layer)
Purpose:
- Verify the request structure and data types.
- Reject malformed or invalid requests before they reach the business logic.

Examples:
- Required fields
- Allowed enum values
- Valid email format

## Business Validation (Service Layer)
Purpose:
- Enforce company or domain rules.

Examples:
- Duplicate Incident IDs are not allowed.
- Only managers can create Critical incidents.
- Assign incidents based on category and priority.

Key takeaway:
Input validation answers "Is this request well-formed?"
Business validation answers "Is this request allowed according to business rules?"


# Engineering Lessons

## Lesson 1

Think in responsibilities, not code.

Before writing code ask:

Who owns this responsibility?

---

## Lesson 2

Repository answers:

"What data exists?"

Service answers:

"What should we do with the data?"

---

## Lesson 3

Business rules belong in Service.

Storage logic belongs in Repository.

HTTP concerns belong in API.

---

## Lesson 4

A change in storage should only affect the Repository.

CSV

↓

PostgreSQL

↓

MongoDB

↓

ServiceNow

The API and Service should remain unchanged.

---

## Lesson 5

Design first.

Code later.

Requirement

↓

Architecture

↓

Layer

↓

Class

↓

Method

↓

Implementation