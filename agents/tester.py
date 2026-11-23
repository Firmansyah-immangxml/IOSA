
from pathlib import Path

from tools.workspace import IOSAWorkspace


class TesterAgent:

    def __init__(self):

        self.workspace = IOSAWorkspace()
        self.role = "Software Testing Agent"

    def test_file(self, filename):

        print("\n[IOSA Tester] Memulai pengujian...")
        print("[IOSA Tester] Memeriksa file...")

        content = self.workspace.read_file(filename)

        if content is None:

            return (
                "PENGUJIAN GAGAL\n\n"
                f"File tidak ditemukan: {filename}"
            )

        print("[IOSA Tester] Memeriksa syntax Python...")

        try:

            compile(
                content,
                filename,
                "exec"
            )

            print("[IOSA Tester] Syntax valid.")

            return (
                "HASIL PENGUJIAN\n\n"
                f"File: {filename}\n"
                "Status: LULUS\n"
                "Pemeriksaan: Syntax Python\n"
                "Hasil: Tidak ditemukan kesalahan syntax.\n\n"
                "Catatan: Pengujian ini hanya memeriksa "
                "syntax. Program belum dijalankan "
                "oleh Tester Agent."
            )

        except SyntaxError as error:

            return (
                "HASIL PENGUJIAN\n\n"
                f"File: {filename}\n"
                "Status: GAGAL\n"
                "Jenis: Syntax Error\n"
                f"Baris: {error.lineno}\n"
                f"Pesan: {error.msg}"
            )

        except Exception as error:

            return (
                "PENGUJIAN GAGAL\n\n"
                f"Error: {str(error)}"
            )
