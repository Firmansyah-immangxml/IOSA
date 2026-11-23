def tambah(a: float, b: float) -> float:
    """Fungsi untuk penjumlahan dua angka."""
    return a + b


def kurang(a: float, b: float) -> float:
    """Fungsi untuk pengurangan dua angka."""
    return a - b


def kali(a: float, b: float) -> float:
    """Fungsi untuk perkalian dua angka."""
    return a * b


def bagi(a: float, b: float) -> float:
    """Fungsi untuk pembagian dua angka dengan penanganan pembagian nol."""
    if b == 0:
        raise ValueError("Pembagian dengan angka nol (0) tidak diperbolehkan.")
    return a / b


def input_angka(prompt: str) -> float:
    """Fungsi helper untuk mevalidasi bahwa input dari pengguna berupa angka."""
    while True:
        try:
            val = input(prompt)
            return float(val)
        except ValueError:
            print("[ERROR] Input tidak valid. Harap masukkan angka yang benar.")


def tampilkan_menu() -> None:
    """Menampilkan pilihan menu kalkulator."""
    print("\n=================================")
    print("      KALKULATOR IOSA CLI        ")
    print("=================================")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Keluar")
    print("=================================")


def main() -> None:
    """Fungsi utama program kalkulator interaktif."""
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "5":
            print("\nTerima kasih telah menggunakan program Kalkulator IOSA. Sampai jumpa!")
            break

        if pilihan in ("1", "2", "3", "4"):
            print("\n--- Input Angka ---")
            num1 = input_angka("Masukkan angka pertama: ")
            num2 = input_angka("Masukkan angka kedua  : ")

            print("\n--- Hasil ---")
            if pilihan == "1":
                hasil = tambah(num1, num2)
                print(f"Hasil: {num1} + {num2} = {hasil}")
            elif pilihan == "2":
                hasil = kurang(num1, num2)
                print(f"Hasil: {num1} - {num2} = {hasil}")
            elif pilihan == "3":
                hasil = kali(num1, num2)
                print(f"Hasil: {num1} * {num2} = {hasil}")
            elif pilihan == "4":
                try:
                    hasil = bagi(num1, num2)
                    print(f"Hasil: {num1} / {num2} = {hasil}")
                except ValueError as err:
                    print(f"[ERROR] {err}")
        else:
            print("[ERROR] Pilihan menu tidak valid. Harap pilih angka 1 hingga 5.")


if __name__ == "__main__":
    main()
