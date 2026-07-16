from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    """Application configuration."""

    MONGODB_URI = os.getenv("MONGODB_URI")
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME")

    LLM_PROVIDER = os.getenv("LLM_PROVIDER")
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
    
    def validate(self):
        """Validate required configuration."""

        required_settings = {
            "MONGODB_URI": self.MONGODB_URI,
            "DATABASE_NAME": self.DATABASE_NAME,
            "COLLECTION_NAME": self.COLLECTION_NAME,
        }

        missing = [
            key for key, value in required_settings.items()
            if not value
        ]

        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}"
            )


settings = Settings()
settings.validate()