api/ --> Contains the HTTP endpoints.
services/ --> Contains Business logic.
models/ --> Defines the data structures using Pydantic.
core/ --> Shared application functionality like logging,configuration,exceptions,etc..
utils/ --> Small Helper Functions like date formatting,csv helpers, string utilities.
config/ --> Loads the configuration from .env file
repositories/ --> The repository's responsibility is reading and writing data.{today we are using csv later we can use other databases like servicenow, postgrSql..}
schemas/ --> FastAPI uses Pydantic models for requests and responses.
models/ --> These represent database entities.