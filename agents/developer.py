
import re

from core.brain import IOSABrain
from tools.workspace import IOSAWorkspace


class DeveloperAgent:

    def __init__(self):

        self.brain = IOSABrain()
        self.workspace = IOSAWorkspace()
        self.role = "Software Developer Agent"

    # ==========================================
    # CREATE PROGRAM
    # ==========================================

    def create_file(self, filename, instruction):

        print("\n[IOSA Developer] Memahami tugas...")
        print("[IOSA Developer] Merancang kode...")
        print("[IOSA Developer] Menghubungi IOSA Brain...")

        prompt = f"""
Kamu adalah IOSA Developer Agent.

Tugas:
Membuat kode program lengkap.

NAMA FILE:
{filename}

INSTRUKSI:
{instruction}

ATURAN:
- Buat kode lengkap, bukan potongan.
- Jangan menambahkan penjelasan.
- Fokus hanya pada satu file.
- Jangan mengklaim kode sudah diuji.
- Gunakan format penanda berikut secara tepat.

<<<IOSA_CODE>>>
(kode program lengkap)
<<<END_IOSA_CODE>>>
"""

        generated_code = self.brain.think(prompt)

        if not generated_code:
            return "Developer Agent gagal mendapatkan kode."

        if (
            "IOSA tidak berhasil mendapatkan respons"
            in generated_code
            or "IOSA mengalami kesalahan"
            in generated_code
        ):
            return generated_code

        match = re.search(
            r"<<<IOSA_CODE>>>(.*?)<<<END_IOSA_CODE>>>",
            generated_code,
            re.DOTALL
        )

        if not match:

            return (
                "Developer Agent gagal membaca kode.\n"
                "Format respons AI tidak sesuai."
            )

        code = match.group(1).strip()

        if not code:
            return "Kode yang dihasilkan kosong."

        print("[IOSA Developer] Kode berhasil dibuat.")
        print("[IOSA Developer] Menyimpan file...")

        result = self.workspace.create_file(
            filename,
            code + "\n"
        )

        if result["success"]:

            print("[IOSA Developer] File berhasil dibuat.")

            return (
                "PEMBANGUNAN BERHASIL\n\n"
                f"File: {filename}\n"
                f"Lokasi: {result['path']}\n"
                f"Ukuran: {result['size']} byte\n\n"
                "Kode berhasil disimpan di workspace IOSA.\n"
                "Kode belum dijalankan atau diuji."
            )

        return (
            "PEMBANGUNAN GAGAL\n\n"
            + result["message"]
        )

    # ==========================================
    # AUTO REPAIR
    # ==========================================

    def repair_file(self, filename, error_report):

        print("\n[IOSA Developer] Memulai Auto Repair...")
        print("[IOSA Developer] Membaca kode yang bermasalah...")

        existing_code = self.workspace.read_file(
            filename
        )

        if existing_code is None:

            return (
                "AUTO REPAIR GAGAL\n\n"
                f"File tidak ditemukan: {filename}"
            )

        print("[IOSA Developer] Menganalisis error...")
        print("[IOSA Developer] Merancang perbaikan...")
        print("[IOSA Developer] Menghubungi IOSA Brain...")

        prompt = f"""
Kamu adalah IOSA Developer Agent.

Tugas:
Memperbaiki kode program yang mengalami kesalahan.

NAMA FILE:
{filename}

KODE SAAT INI:
{existing_code}

LAPORAN TESTER:
{error_report}

ATURAN:
- Perbaiki penyebab kesalahan.
- Pertahankan fitur yang sudah ada.
- Jangan menghapus fungsi yang masih diperlukan.
- Jangan menambahkan fitur yang tidak diminta.
- Berikan kode lengkap hasil perbaikan.
- Jangan berikan penjelasan.
- Jangan berikan Markdown code fence.
- Jangan mengklaim program sudah berhasil diuji.
- Gunakan format penanda berikut secara tepat.

<<<IOSA_CODE>>>
(kode lengkap hasil perbaikan)
<<<END_IOSA_CODE>>>
"""

        generated_code = self.brain.think(prompt)

        if not generated_code:

            return (
                "AUTO REPAIR GAGAL\n\n"
                "Brain tidak memberikan kode perbaikan."
            )

        if (
            "IOSA tidak berhasil mendapatkan respons"
            in generated_code
            or "IOSA mengalami kesalahan"
            in generated_code
        ):

            return generated_code

        match = re.search(
            r"<<<IOSA_CODE>>>(.*?)<<<END_IOSA_CODE>>>",
            generated_code,
            re.DOTALL
        )

        if not match:

            return (
                "AUTO REPAIR GAGAL\n\n"
                "Format kode perbaikan tidak sesuai."
            )

        repaired_code = match.group(1).strip()

        if not repaired_code:

            return (
                "AUTO REPAIR GAGAL\n\n"
                "Kode hasil perbaikan kosong."
            )

        # ======================================
        # VALIDASI SEBELUM MENYIMPAN
        # ======================================

        print("[IOSA Developer] Memvalidasi hasil perbaikan...")

        try:

            compile(
                repaired_code,
                filename,
                "exec"
            )

        except SyntaxError as error:

            return (
                "AUTO REPAIR GAGAL\n\n"
                "Kode perbaikan masih memiliki "
                "Syntax Error.\n\n"
                f"Baris: {error.lineno}\n"
                f"Pesan: {error.msg}\n\n"
                "File lama tidak diubah."
            )

        # ======================================
        # UPDATE FILE
        # ======================================

        print("[IOSA Developer] Menyimpan perbaikan...")

        result = self.workspace.update_file(
            filename,
            repaired_code + "\n"
        )

        if result["success"]:

            print("[IOSA Developer] Perbaikan berhasil disimpan.")

            return (
                "AUTO REPAIR BERHASIL\n\n"
                f"File: {filename}\n"
                f"Lokasi: {result['path']}\n"
                f"Ukuran: {result['size']} byte\n\n"
                "Kode berhasil diperbaiki.\n"
                "Syntax hasil perbaikan valid.\n"
                "Program perlu diuji kembali oleh Tester."
            )

        return (
            "AUTO REPAIR GAGAL\n\n"
            + result["message"]
        )
