from pathlib import Path


class IOSAWorkspace:

    def __init__(self):

        self.root = Path("workspace").resolve()

        self.root.mkdir(
            parents=True,
            exist_ok=True
        )

    # ==========================================
    # CREATE FILE
    # ==========================================

    def create_file(self, filename, content):

        relative_path = Path(filename)

        if relative_path.is_absolute():
            return {
                "success": False,
                "message": "Path absolut tidak diizinkan."
            }

        target = (
            self.root / relative_path
        ).resolve()

        try:
            target.relative_to(self.root)

        except ValueError:
            return {
                "success": False,
                "message": "Akses di luar workspace ditolak."
            }

        if target.exists():

            return {
                "success": False,
                "message": (
                    f"File sudah ada: {filename}. "
                    "IOSA tidak akan menimpa file."
                )
            }

        try:

            target.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            target.write_text(
                content,
                encoding="utf-8"
            )

            if target.exists():

                return {
                    "success": True,
                    "message": "File berhasil dibuat.",
                    "path": str(target),
                    "size": target.stat().st_size
                }

            return {
                "success": False,
                "message": "Verifikasi file gagal."
            }

        except Exception as error:

            return {
                "success": False,
                "message": str(error)
            }

    # ==========================================
    # UPDATE FILE - AUTO REPAIR
    # ==========================================

    def update_file(self, filename, content):

        relative_path = Path(filename)

        if relative_path.is_absolute():

            return {
                "success": False,
                "message": "Path absolut tidak diizinkan."
            }

        target = (
            self.root / relative_path
        ).resolve()

        # Keamanan: pastikan target tetap
        # berada di dalam workspace

        try:

            target.relative_to(self.root)

        except ValueError:

            return {
                "success": False,
                "message": "Akses di luar workspace ditolak."
            }

        # File harus sudah ada

        if not target.exists():

            return {
                "success": False,
                "message": (
                    f"File tidak ditemukan: {filename}"
                )
            }

        if not target.is_file():

            return {
                "success": False,
                "message": "Target bukan file."
            }

        # Proses perbaikan

        try:

            target.write_text(
                content,
                encoding="utf-8"
            )

            # Verifikasi hasil penyimpanan

            saved_content = target.read_text(
                encoding="utf-8"
            )

            if saved_content == content:

                return {
                    "success": True,
                    "message": "File berhasil diperbarui.",
                    "path": str(target),
                    "size": target.stat().st_size
                }

            return {
                "success": False,
                "message": (
                    "Verifikasi perubahan file gagal."
                )
            }

        except Exception as error:

            return {
                "success": False,
                "message": str(error)
            }

    # ==========================================
    # READ FILE
    # ==========================================

    def read_file(self, filename):

        target = (
            self.root / filename
        ).resolve()

        try:

            target.relative_to(self.root)

        except ValueError:

            return None

        if not target.exists():
            return None

        if not target.is_file():
            return None

        try:

            return target.read_text(
                encoding="utf-8"
            )

        except Exception:

            return None

    # ==========================================
    # LIST FILES
    # ==========================================

    def list_files(self):

        files = []

        for file in self.root.rglob("*"):

            if file.is_file():

                files.append(
                    str(
                        file.relative_to(
                            self.root
                        )
                    )
                )

        return files