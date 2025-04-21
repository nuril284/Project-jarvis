import time
import os
import sys

# Fungsi buat animasi ngetik
def print_delay(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Fungsi loading animasi
def loading(teks):
    for i in range(4):
        print(f"{teks}{'.'*i}", end='\r')
        time.sleep(0.5)
    print(f"{teks}... Done!\n")

# Tampilan intro
intro = [
    ">> Mengakses sistem keamanan...",
    ">> Mendeteksi lingkungan virtual...",
    ">> Menyambungkan AI Jarvis...",
    ">> Versi Private - Launcher by Nuril...",
    ">> Menyiapkan antarmuka...",
]

for kalimat in intro:
    print_delay(kalimat, 0.05)
    time.sleep(0.3)

os.system("clear")
print("="*50)
print_delay("||         JARVIS PRIVATE LAUNCHER - NURIL         ||", 0.03)
print("="*50)
print()

# Autentikasi
print_delay(">> Autentikasi Nuril... VALID", 0.05)
# Suara (jika support)
try:
    os.system('espeak "Authentication success. Welcome back, Nuril"')
except:
    pass

# Menu utama
while True:
    print("\n=== MENU UTAMA ===")
    print("1. Scan IP Publik")
    print("2. Info Device")
    print("3. Keluar")
    
    cmd = input(">> Pilih opsi: ")

    if cmd == "1":
        loading(">> Memindai IP target")
        os.system("curl ifconfig.me")
    elif cmd == "2":
        loading(">> Mengambil info sistem")
        os.system("uname -a")
    elif cmd == "3":
        print_delay(">> Menutup sistem... Sampai jumpa, Nuril!", 0.05)
        break
    else:
        print(">> Opsi tidak valid!")
