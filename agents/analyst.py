from core.brain import IOSABrain


class AnalystAgent:

    def __init__(self):

        self.brain = IOSABrain()

        self.role = "Software Requirements Analyst"

    def analyze(self, instruction):

        prompt = f"""
Kamu adalah IOSA Analyst Agent.

ROLE:
{self.role}

TUGAS:
Analisis instruksi dari System Owner
sebelum pekerjaan dilakukan.

INSTRUKSI OWNER:
{instruction}

Buat analisis dengan struktur berikut:

1. RINGKASAN
Jelaskan apa yang diminta Owner.

2. MASALAH
Identifikasi masalah yang ingin diselesaikan.

3. TUJUAN
Jelaskan tujuan proyek atau pekerjaan.

4. KEBUTUHAN
Identifikasi kebutuhan utama.

5. RUANG LINGKUP
Jelaskan batasan pekerjaan.

6. RENCANA KERJA
Buat langkah-langkah pengerjaan
secara berurutan.

7. RISIKO
Identifikasi kemungkinan masalah.

8. REKOMENDASI
Berikan rekomendasi langkah berikutnya.

Gunakan bahasa Indonesia yang jelas.
Jangan mengarang informasi yang tidak diketahui.
Jika terdapat asumsi, tandai sebagai asumsi.
Jangan melakukan coding pada tahap analisis.
"""

        return self.brain.think(prompt)