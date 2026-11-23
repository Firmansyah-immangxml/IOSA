def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan."
    return a / b

def main():
    print("=== KALKULATOR SEDERHANA ===")
    print("Pilih Operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")

    while True:
        pilihan = input("\nMasukkan pilihan (1/2/3/4) atau 'q' untuk keluar: ").strip()

        if pilihan.lower() == 'q':
            print("Terima kasih telah menggunakan kalkulator.")
            break

        if pilihan in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Masukkan angka pertama: "))
                num2 = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Error: Input harus berupa angka.")
                continue

            if pilihan == '1':
                print(f"Hasil: {num1} + {num2} = {tambah(num1, num2)}")
            elif pilihan == '2':
                print(f"Hasil: {num1} - {num2} = {kurang(num1, num2)}")
            elif pilihan == '3':
                print(f"Hasil: {num1} * {num2} = {kali(num1, num2)}")
            elif pilihan == '4':
                hasil = bagi(num1, num2)
                print(f"Hasil: {num1} / {num2} = {hasil}")
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, atau 'q'.")

if __name__ == "__main__":
    main()
