from agents.analyst import AnalystAgent
from agents.developer import DeveloperAgent
from agents.tester import TesterAgent
from core.memory import IOSAMemory


class IOSAOrchestrator:

    MAX_REPAIR_ATTEMPTS = 3

    def __init__(self):

        self.analyst = AnalystAgent()
        self.developer = DeveloperAgent()
        self.tester = TesterAgent()
        self.memory = IOSAMemory()

        print("[IOSA] Engine berhasil diinisialisasi.")
        print("[IOSA] Analyst Agent siap.")
        print("[IOSA] Developer Agent siap.")
        print("[IOSA] Tester Agent siap.")

    # ==========================================
    # ANALYSIS ONLY
    # ==========================================

    def execute(self, instruction):

        print("\n[IOSA] Menerima instruksi...")
        print("[IOSA] Mengaktifkan Analyst Agent...")
        print("[IOSA] Menganalisis instruksi...")

        response = self.analyst.analyze(instruction)

        self.memory.save(
            instruction,
            response
        )

        print("[IOSA] Analisis selesai.")

        return response

    # ==========================================
    # AUTONOMOUS BUILD WORKFLOW
    # ==========================================

    def build(self, filename, instruction):

        print("\n" + "=" * 60)
        print("IOSA AUTONOMOUS BUILD WORKFLOW")
        print("=" * 60)

        # --------------------------------------
        # STEP 1 - ANALYSIS
        # --------------------------------------

        print("\n[WORKFLOW 1/3] ANALYSIS")

        analysis = self.analyst.analyze(
            instruction
        )

        if not analysis:

            final_result = (
                "WORKFLOW GAGAL\n\n"
                "Analyst Agent gagal melakukan analisis."
            )

            self.memory.save(
                instruction,
                final_result
            )

            return final_result

        if (
            "IOSA tidak berhasil mendapatkan respons"
            in analysis
            or "IOSA mengalami kesalahan"
            in analysis
        ):

            final_result = (
                "WORKFLOW GAGAL\n\n"
                "Analisis tidak berhasil.\n\n"
                + analysis
            )

            self.memory.save(
                instruction,
                final_result
            )

            return final_result

        print("\n[IOSA] Analisis selesai.")

        # --------------------------------------
        # STEP 2 - DEVELOPMENT
        # --------------------------------------

        print("\n[WORKFLOW 2/3] DEVELOPMENT")

        development_instruction = f"""
INSTRUKSI SYSTEM OWNER:
{instruction}

HASIL ANALISIS:
{analysis}

TUGAS:
Buat program berdasarkan instruksi Owner
dan hasil analisis di atas.

Pastikan program memenuhi kebutuhan
yang telah dianalisis.
"""

        development = self.developer.create_file(
            filename,
            development_instruction
        )

        print("\n[IOSA] Hasil Development:")
        print(development)

        if "PEMBANGUNAN BERHASIL" not in development:

            final_result = (
                "WORKFLOW BERHENTI\n\n"
                "Tahap Development gagal.\n"
                "Testing tidak dijalankan.\n\n"
                + development
            )

            self.memory.save(
                instruction,
                final_result
            )

            return final_result

        # --------------------------------------
        # STEP 3 - TESTING & AUTO REPAIR
        # --------------------------------------

        print("\n[WORKFLOW 3/3] TESTING")

        repair_attempts = 0

        testing = self.tester.test_file(
            filename
        )

        print("\n[IOSA] Hasil Testing:")
        print(testing)

        # --------------------------------------
        # AUTO REPAIR LOOP
        # --------------------------------------

        while (
            "Status: LULUS" not in testing
            and repair_attempts
            < self.MAX_REPAIR_ATTEMPTS
        ):

            repair_attempts += 1

            print("\n" + "=" * 60)

            print(
                f"[IOSA AUTO REPAIR] "
                f"Percobaan {repair_attempts}/"
                f"{self.MAX_REPAIR_ATTEMPTS}"
            )

            print("=" * 60)

            # DEVELOPER MEMPERBAIKI

            repair_result = self.developer.repair_file(
                filename,
                testing
            )

            print("\n[IOSA] Hasil Auto Repair:")
            print(repair_result)

            # Jika perbaikan gagal, hentikan loop

            if "AUTO REPAIR BERHASIL" not in repair_result:

                print(
                    "\n[IOSA] Auto Repair gagal."
                )

                break

            # TESTER MENGUJI KEMBALI

            print(
                "\n[IOSA] Menjalankan pengujian ulang..."
            )

            testing = self.tester.test_file(
                filename
            )

            print("\n[IOSA] Hasil Retest:")
            print(testing)

        # --------------------------------------
        # FINAL REPORT
        # --------------------------------------

        if "Status: LULUS" in testing:

            final_result = (
                "WORKFLOW SELESAI\n\n"
                "Status: BERHASIL\n\n"
                "Analisis: SELESAI\n"
                "Development: BERHASIL\n"
                "Testing: LULUS\n"
                f"Auto Repair: {repair_attempts} kali\n\n"
                f"File: {filename}\n\n"
                "Program berhasil dibuat dan "
                "lolos pemeriksaan syntax Python.\n"
                "Program belum diuji secara "
                "fungsional atau menyeluruh."
            )

        else:

            final_result = (
                "WORKFLOW SELESAI\n\n"
                "Status: PERLU PERBAIKAN\n\n"
                "Analisis: SELESAI\n"
                "Development: BERHASIL\n"
                "Testing: GAGAL\n"
                f"Auto Repair: {repair_attempts} kali\n\n"
                f"File: {filename}\n\n"
                "IOSA belum berhasil memastikan "
                "program lolos pengujian.\n\n"
                "Laporan pengujian terakhir:\n"
                + testing
            )

        self.memory.save(
            instruction,
            final_result
        )

        print("\n[IOSA] Workflow selesai.")

        return final_result