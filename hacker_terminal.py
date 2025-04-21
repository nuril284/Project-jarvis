import os
import time
import random

# Warna terminal
hijau = "\033[92m"
merah = "\033[91m"
kuning = "\033[93m"
biru = "\033[94m"
reset = "\033[0m"

# Animasi ngetik
def ketik(teks, delay=0.02):
    for char in teks:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Banner
def banner():
    os.system("clear")
    print(hijau + "="*50)
    print(kuning + "||    SIMULASI TERMINAL HACKER - BY NURIL    ||")
    print(hijau + "="*50 + reset)

# Loading
def loading(teks, waktu=3):
    for i in range(waktu):
        print(f"{teks}{'.'*i}", end='\r')
        time.sleep(0.5)
    print(f"{teks}... Done!")

# Fungsi palsu scan IP
def fake_scan():
    ketik(biru + "[*] Mengakses jaringan publik..." + reset)
    time.sleep(1)
    for i in range(1, 6):
        ip = f"192.168.1.{random.randint(2, 254)}"
        ketik(hijau + f"[+] IP ditemukan: {ip} → Port 22 Open" + reset)
        time.sleep(0.5)
    ketik(merah + "[!] Simulasi selesai. Sistem aman." + reset)

# MAIN
banner()
loading("[*] Menyiapkan sistem")
ketik(hijau + "[*] Login sebagai: Nuril" + reset)
time.sleep(1)
ketik(kuning + "[*] Mengaktifkan mode stealth..." + reset)
time.sleep(1)

while True:
    print()
    print(kuning + "=== MENU ===" + reset)
    print("1. Simulasi Scan IP")
    print("2. Lihat info sistem")
    print("3. Keluar")

    pilihan = input(">> Pilih opsi: ")

    if pilihan == "1":
        fake_scan()
    elif pilihan == "2":
        ketik(hijau + "[*] Info Sistem:" + reset)
        os.system("uname -a")
    elif pilihan == "3":
        ketik(merah + "[!] Menutup sistem... Selamat tinggal, Nuril!" + reset)
        break
    else:
        print(merah + "[!] Opsi tidak valid!" + reset)
