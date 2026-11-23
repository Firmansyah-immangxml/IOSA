from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("IOSA_MODEL", "gemini-3.8-flash")

if not api_key:
    print("API Key tidak ditemukan!")
    exit()

client = genai.Client(api_key=api_key)

print("=" * 40)
print("IOSA - AI CONNECTION TEST")
print("=" * 40)
print(f"Model: {model_name}")
print("Mengirim instruksi ke AI...\n")

try:
    response = client.models.generate_content(
        model=model_name,
        contents="Perkenalkan dirimu sebagai AI Brain yang akan menjadi otak IOSA."
    )

    print("STATUS: BERHASIL")
    print("-" * 40)
    print(response.text)

except Exception as error:
    print("STATUS: GAGAL")
    print("-" * 40)
    print(error)