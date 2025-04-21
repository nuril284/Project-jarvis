import time
import os

def header():
    os.system("clear")  # Bersihin layar
    print("\033[1;31m")
    print("╔══════════════════════════════╗")
    print("║    TERMINAL LAUNCHER GAHAR   ║")
    print("║         by NURIL V2          ║")
    print("╚══════════════════════════════╝")
    print("\033[0m")

def spam_teks():
    teks = input("\nMasukkan teks yang ingin di-spam: ")
    jumlah = int(input("Masukkan jumlah spam: "))
    for i in range(jumlah):
        print(f"{i+1}. {teks}")
        time.sleep(0.1)

def loading_animasi():
    animasi = ["[■□□□□]", "[■■□□□]", "[■■■□□]", "[■■■■□]", "[■■■■■]"]
    for frame in animasi:
        print(f"\rLoading {frame}", end="")
        time.sleep(0.4)
    print("\nSelesai!")

def menu():
    header()
    print("1. Info System")
    print("2. Spam Teks")
    print("3. Loading Animasi")
    print("4. Exit\n")

while True:
    menu()
    pilihan = input("Pilih opsi (1-4): ")

    if pilihan == "1":
        os.system("uname -a")  # info sistem linux
        input("\nTekan ENTER untuk kembali ke menu...")
    elif pilihan == "2":
        spam_teks()
        input("\nTekan ENTER untuk kembali ke menu...")
    elif pilihan == "3":
        loading_animasi()
        input("\nTekan ENTER untuk kembali ke menu...")
    elif pilihan == "4":
        print("Keluar dari Launcher...")
        break
    else:
        print("Pilihan tidak valid!")
        time.sleep(1)
