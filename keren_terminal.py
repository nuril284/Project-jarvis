import os
import time
import random

# Warna terminal
H = '\033[92m'  # Hijau
K = '\033[93m'  # Kuning
B = '\033[94m'  # Biru
M = '\033[91m'  # Merah
W = '\033[0m'   # Reset warna

# Fungsi animasi ngetik
def ketik(teks, delay=0.01):
    for char in teks:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Banner ASCII Art
def banner():
    os.system("clear")
    print(H + r"""
   ______           _       _     
  |  ____|         (_)     | |    
  | |__   _ __ ___  _ _ __ | |__  
  |  __| | '_ ` _ \| | '_ \| '_ \ 
  | |____| | | | | | | | | | | | |
  |______|_| |_| |_|_|_| |_|_| |_| 
  """)
    print(K + "  Terminal Keren - Nuril Edition" + W)
    print("="*50)

# Fungsi loading
def loading(pesan="Loading"):
    for i in range(3):
        print(f"{pesan}{'.' * (i+1)}", end='\r')
        time.sleep(0.5)
    print(f"{pesan}... Done!")

# Fake scan palsu
def fake_scan():
    ketik(B + "[*] Memulai pemindaian jaringan..." + W)
    time.sleep(1)
    for i in range(5):
        ip = f"192.168.0.{random.randint(2, 254)}"
        status = random.choice(["Port 80 OPEN", "Port 443 OPEN", "Firewall Aktif", "Vulnerable Service"])
        ketik(f"{H}[+] {ip} - {status}{W}")
        time.sleep(0.6)
    ketik(M + "[!] Simulasi selesai. Sistem diamankan." + W)

# Info sistem
def info_sistem():
    ketik(K + "[*] Informasi sistem:" + W)
    os.system("uname -a")

# Main Menu
def main():
    banner()
    loading("Menyiapkan sistem")
    while True:
        print()
        print(K + "=== MENU ===" + W)
        print("1. Simulasi Scan IP")
        print("2. Info Sistem")
        print("3. Keluar")
        pilih = input(H + ">> Pilih opsi: " + W)
        if pilih == "1":
            fake_scan()
        elif pilih == "2":
            info_sistem()
        elif pilih == "3":
            ketik(M + "[!] Keluar... Sampai jumpa Nuril!" + W)
            break
        else:
            print(M + "[!] Opsi tidak dikenal!" + W)

# Jalankan
main()
