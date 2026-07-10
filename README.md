Presentation
      ↓
FastAPI

Business
      ↓
Incident Service

Data
      ↓
Incident Repository

Storage
      ↓
CSV



| Responsibility       | Layer                 |
| -------------------- | --------------------- |
| Receive HTTP Request | API                   |
| Validate Request     | API (Pydantic Schema) |
| Apply Business Rules | Service               |
| Save Incident        | Repository            |
| Return Response      | API                   |
