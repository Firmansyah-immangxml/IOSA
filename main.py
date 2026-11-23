
from core.orchestrator import IOSAOrchestrator
from tools.workspace import IOSAWorkspace


def main():

    print("=" * 60)
    print("IOSA")
    print("IMMANG Orchestra Software Agency")
    print("Autonomous Software Engineering System")
    print("=" * 60)

    iosa = IOSAOrchestrator()
    workspace = IOSAWorkspace()

    print("\nIOSA siap menerima perintah.")
    print("\nDAFTAR PERINTAH:")
    print("  analisis <instruksi>")
    print("  buat file <nama_file> | <instruksi>")
    print("  build <nama_file> | <instruksi>")
    print("  test file <nama_file>")
    print("  daftar file")
    print("  baca file <nama_file>")
    print("  history")
    print("  exit\n")

    while True:

        instruction = input("OWNER > ").strip()

        if not instruction:
            continue

        command = instruction.lower()

        # EXIT
        if command == "exit":

            print("\nIOSA: Sistem dihentikan.")
            break

        # HISTORY
        if command == "history":

            history = iosa.memory.show_history()

            print("\nRIWAYAT IOSA:")
            print(history)
            continue

        # LIST FILES
        if command == "daftar file":

            files = workspace.list_files()

            print("\n[IOSA Workspace] Daftar file:")

            if files:

                for file in files:
                    print(f"- {file}")

            else:

                print("Workspace masih kosong.")

            result = (
                "Daftar file workspace:\n"
                + "\n".join(files)
                if files
                else "Workspace masih kosong."
            )

            iosa.memory.save(instruction, result)
            continue

        # READ FILE
        if command.startswith("baca file "):

            filename = instruction[10:].strip()

            content = workspace.read_file(filename)

            print("\n[IOSA Workspace] Membaca file...")

            if content is not None:

                print(f"\nFILE: {filename}")
                print("=" * 60)
                print(content)
                print("=" * 60)

                result = (
                    f"Isi file {filename}:\n\n"
                    f"{content}"
                )

            else:

                print(
                    f"File '{filename}' tidak ditemukan "
                    "di workspace IOSA."
                )

                result = (
                    f"File {filename} "
                    "tidak ditemukan di workspace."
                )

            iosa.memory.save(instruction, result)
            continue

        # TESTER AGENT
        if command.startswith("test file "):

            filename = instruction[10:].strip()

            if not filename:

                print("\nNama file harus diisi.")
                continue

            print("\n[IOSA] Mengaktifkan Tester Agent...")

            result = iosa.tester.test_file(filename)

            print("\nIOSA >")
            print(result)

            iosa.memory.save(instruction, result)

            print("-" * 60)
            continue

        # AUTONOMOUS BUILD WORKFLOW
        if command.startswith("build "):

            request = instruction[6:].strip()

            if "|" not in request:

                print("\nFormat perintah salah.")
                print(
                    "Gunakan:\n"
                    "build nama_file.py | "
                    "instruksi program"
                )
                continue

            filename, task = request.split("|", 1)

            filename = filename.strip()
            task = task.strip()

            if not filename or not task:

                print(
                    "\nNama file dan instruksi "
                    "harus diisi."
                )
                continue

            result = iosa.build(
                filename,
                task
            )

            print("\nIOSA >")
            print(result)

            print("-" * 60)
            continue

        # DEVELOPER AGENT ONLY
        if command.startswith("buat file "):

            request = instruction[10:].strip()

            if "|" not in request:

                print("\nFormat perintah salah.")
                print(
                    "Gunakan:\n"
                    "buat file nama.py | "
                    "instruksi pembuatan program"
                )
                continue

            filename, task = request.split("|", 1)

            filename = filename.strip()
            task = task.strip()

            if not filename or not task:

                print(
                    "\nNama file dan instruksi "
                    "harus diisi."
                )
                continue

            print(
                "\n[IOSA] Mengaktifkan Developer Agent..."
            )

            result = iosa.developer.create_file(
                filename,
                task
            )

            print("\nIOSA >")
            print(result)

            iosa.memory.save(instruction, result)

            print("-" * 60)
            continue

        # ANALYST AGENT
        if command.startswith("analisis "):

            task = instruction[9:].strip()

            if not task:

                print("Instruksi analisis kosong.")
                continue

            response = iosa.execute(task)

            print("\nIOSA >")
            print(response)

            print("-" * 60)
            continue

        # DEFAULT COMMAND
        response = iosa.execute(instruction)

        print("\nIOSA >")
        print(response)

        print("-" * 60)


if __name__ == "__main__":
    main()
