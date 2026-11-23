import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

IOSA_MODEL = os.getenv(
    "IOSA_MODEL",
    "gemini-3.8-flash"
)

IOSA_FALLBACK_MODELS = [
    model.strip()
    for model in os.getenv(
        "IOSA_FALLBACK_MODELS",
        "gemini-3.7-flash,gemini-2.5-flash,gemini-3.5-flash"
    ).split(",")
    if model.strip()
]

IOSA_NAME = "IOSA"

IOSA_IDENTITY = (
    "IMMANG Orchestra Software Agency"
)