import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")

    UPLOAD_FOLDER = "static/uploads"
    OUTPUT_FOLDER = "static/outputs"
    DB_PATH = "database.db"
