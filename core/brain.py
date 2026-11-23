import time

from google import genai

from config.settings import (
    GEMINI_API_KEY,
    IOSA_MODEL,
    IOSA_FALLBACK_MODELS,
    IOSA_NAME,
    IOSA_IDENTITY
)


class IOSABrain:

    def __init__(self):

        if not GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY belum diatur di .env"
            )

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.model = IOSA_MODEL

        self.models = list(dict.fromkeys(
            [IOSA_MODEL] + IOSA_FALLBACK_MODELS
        ))

        self.system_instruction = f"""
Kamu adalah {IOSA_NAME}.

Identitas:
{IOSA_IDENTITY}

Kamu merupakan AI dalam sistem
Autonomous Software Engineering.

System Owner adalah pemilik dan pengambil
keputusan utama.

Prinsip kerja:
- Understand First
- Analyze Before Design
- Design Before Build
- Modular Development
- Verify Everything
- Security First
- Human Control
- Continuous Improvement

Jangan mengarang hasil eksekusi.
Jangan mengaku telah menguji kode jika
pengujian belum benar-benar dilakukan.
Jangan mengaku telah mengubah file jika
belum memiliki akses filesystem.
Gunakan bahasa Indonesia.
"""

    def think(self, instruction):

        instruction = instruction.strip()

        if not instruction:
            return "Instruksi kosong."

        errors = []

        for model_name in self.models:

            print(
                f"\n[IOSA Brain] Menggunakan model: "
                f"{model_name}"
            )

            for attempt in range(2):

                try:

                    response = self.client.models.generate_content(
                        model=model_name,
                        contents=instruction,
                        config={
                            "system_instruction":
                                self.system_instruction
                        }
                    )

                    if response.text:

                        self.model = model_name

                        print(
                            f"[IOSA Brain] "
                            f"Respons berhasil dari {model_name}"
                        )

                        return response.text

                    errors.append(
                        f"{model_name}: respons kosong"
                    )

                    break

                except Exception as error:

                    error_message = str(error)

                    errors.append(
                        f"{model_name}: {error_message}"
                    )

                    permanent_error = (
                        "API_KEY_INVALID" in error_message
                        or "API key not valid" in error_message
                        or "401" in error_message
                        or "403" in error_message
                    )

                    if permanent_error:

                        return (
                            "IOSA gagal mengakses API.\n"
                            "Periksa API Key dan izin API."
                        )

                    temporary_error = (
                        "503" in error_message
                        or "UNAVAILABLE" in error_message
                        or "429" in error_message
                        or "RESOURCE_EXHAUSTED"
                        in error_message
                        or "500" in error_message
                    )

                    if temporary_error and attempt == 0:

                        print(
                            "[IOSA Brain] Model sedang sibuk. "
                            "Mencoba ulang dalam 2 detik..."
                        )

                        time.sleep(2)

                        continue

                    print(
                        f"[IOSA Brain] Model "
                        f"{model_name} gagal."
                    )

                    break

            print(
                "[IOSA Brain] Beralih ke model cadangan..."
            )

        return (
            "IOSA tidak berhasil mendapatkan respons "
            "dari seluruh model AI.\n\n"
            "Detail:\n"
            + "\n".join(errors)
        )