from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API Key tidak ditemukan di .env")
    exit()

client = genai.Client(api_key=api_key)

print("Memeriksa model Gemini yang tersedia...\n")

try:
    for model in client.models.list():
        actions = getattr(model, "supported_actions", [])

        if "generateContent" in actions:
            print(model.name)

except Exception as error:
    print("Gagal:")
    print(error)