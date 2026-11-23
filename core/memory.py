import json
from pathlib import Path

class IOSAMemory:

    def __init__(self):

        self.memory_file = Path("memory/data.json")

        self.memory_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.memory_file.exists():

            self.memory_file.write_text(
                "[]",
                encoding="utf-8"
            )

    def save(self, instruction, response):

        data = self.load()

        record = {
            "instruction": instruction,
            "response": response
        }

        data.append(record)

        self.memory_file.write_text(
            json.dumps(
                data,
                indent=4,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )

    def load(self):

        try:

            return json.loads(
                self.memory_file.read_text(
                    encoding="utf-8"
                )
            )

        except (json.JSONDecodeError, FileNotFoundError):

            return []

    def show_history(self):

        history = self.load()

        if not history:
            return "Belum ada riwayat."

        return history