import os  # what is os where does it come from ?

from dotenv import load_dotenv  # what is dotenv where does it come from ?

load_dotenv()


class Settings:  # what is class ? -> a class with no __init__.py and slef is allowed?
    # LLM model

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # why it is fetched ?
    GROQ_MODEL = "openai/gpt-oss-20b"  # why it is directly typed ?
    GROQ_FALLBACK_API_KEY = os.getenv("GROQ_FALLBACK_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # Qdrant Vector DB Settings

    QDRANT_URL = os.getenv("QDRANT_CLUSTER_ENDPOINT")
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    QDRANT_COLLECTION = "enterprise_rag"


settings = Settings()  # why it is called and stored in variable and what is purpose of varible ? why to make a object at bottom of the file ?
