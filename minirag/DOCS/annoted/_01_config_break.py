from app.config import Settings

print("Qudrant cluster collection :", Settings.QDRANT_COLLECTION)
print("GROQ MODEL :", Settings.GROQ_MODEL)
print("GROQ key present :", Settings.GROQ_API_KEY is not None)
print("GROQ Fallback key present :", Settings.GROQ_FALLBACK_API_KEY is not None)
