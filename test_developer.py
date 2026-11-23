from agents.developer import DeveloperAgent


print("=" * 45)
print("IOSA - DEVELOPER AGENT TEST")
print("=" * 45)

developer = DeveloperAgent()

result = developer.create_file(
    filename="hello.py",
    instruction="""
Buat program Python sederhana.

Program harus menampilkan:

HELLO, SAYA IOSA
Developer Agent berhasil membuat program.
Ini adalah program pertama yang dibuat IOSA.
"""
)

print("\n")
print(result)
print("=" * 45)