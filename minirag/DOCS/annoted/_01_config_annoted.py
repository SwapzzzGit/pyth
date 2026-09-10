import os  # os is a module that helps codebase to talk with operating system.

from dotenv import (
    load_dotenv,
)  # load_dotenv is used to load the environment variables in .env file

load_dotenv()  # load_dotenv() runs the moment the file is imported.


class Settings:  # It is a plain container class with no __init__ in it. where no per object state is needed
    """GEMINI EMBEDDING"""

    GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

    """LLM MODELS"""

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = "openai/gpt-oss-20b"
    GROQ_FALLBACK_API_KEY = os.getenv["GROQ_FALLBACK_API_KEY"]

    """VECTOR DATABASE (QDRANT)"""

    QDRANT_API_KEY = os.getenv["QDRANT_API_KEY"]
    QDRANT_CLUSTER_ENDPOINT = os.getenv["QDRANT_CLUSTER_ENDPOINT"]
    QDRANT_COLLECTION = "enterprise-rag"


settings = (
    Settings()
)  # one shared instance , from app.config import settings gets THIS object.
