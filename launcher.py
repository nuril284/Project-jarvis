import os
import time

def menu():
    os.system("clear")
    print("="*40)
    print("        LAUNCHER TERMINAL - BY NURIL       ")
    print("="*40)
    print("1. Scan IP (simulasi)")
    print("2. Kalkulator")
    print("3. Info Developer")
    print("4. Keluar")
    print("="*40)

def scan_ip():
    for i in range(1, 6):
        ip = f"192.168.1.{i}"
        print(f"[+] Scanning {ip} ... [OK]")
        time.sleep(1)

def kalkulator():
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        hasil = a + b
        print(f"Hasil: {a} + {b} = {hasil}")
    except:
        print("Input tidak valid!")

def info():
    print("Developer: Nuril")
    print("Github   : https://github.com/nuril284")
    print("Status   : Terminal Project Active")

while True:
    menu()
    pilihan = input("Pilih menu >> ")
    
    if pilihan == "1":
        scan_ip()
    elif pilihan == "2":
        kalkulator()
    elif pilihan == "3":
        info()
    elif pilihan == "4":
        print("Keluar dari program...")
        break
    else:
        print("Pilihan tidak tersedia!")

    input("\nTekan Enter untuk kembali...")
