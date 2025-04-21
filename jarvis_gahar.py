import os
import time
import random

# Warna terminal
R = '\033[91m'  # Merah
G = '\033[92m'  # Hijau
Y = '\033[93m'  # Kuning
B = '\033[94m'  # Biru
C = '\033[96m'  # Cyan
W = '\033[0m'   # Reset

# Efek ngetik
def type(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Banner gahar
def banner():
    os.system("clear")
    print(G + r"""
███████╗ █████╗ ██████╗ ██╗   ██╗███████╗
██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝
███████╗███████║██████╔╝ ╚████╔╝ ███████╗
╚════██║██╔══██║██╔═══╝   ╚██╔╝  ╚════██║
███████║██║  ██║██║        ██║   ███████║
╚══════╝╚═╝  ╚═╝╚═╝        ╚═╝   ╚══════╝
        """)
    print(R + "[ JARVIS PRIVATE MODE - NURIL EDITION ]" + W)
    print("-" * 50)

# Simulasi sistem
def booting():
    msgs = [
        "Memulai sistem keamanan...",
        "Memeriksa file enkripsi...",
        "Mengaktifkan firewall...",
        "Melakukan bypass port...",
        "Sistem siap tempur..."
    ]
    for msg in msgs:
        type(Y + "[•] " + msg + W, 0.05)
        time.sleep(0.5)

# Fake scan
def scan():
    type(C + "\n[*] Menyusup ke jaringan target...\n" + W)
    for i in range(1, 6):
        ip = f"192.168.1.{random.randint(10, 250)}"
        vuln = random.choice(["Terbuka", "Tertutup", "Terdeteksi celah", "Firewall aktif"])
        print(f"{G}[+] {ip} | Status: {R}{vuln}{W}")
        time.sleep(0.7)
    type(B + "\n[✓] Proses selesai. Data disimpan.\n" + W)

# Main
def main():
    banner()
    booting()
    while True:
        print(Y + "\n=== MENU ===" + W)
        print("1. Jalankan Scan")
        print("2. Keluar")
        pilih = input(G + ">> Pilihan: " + W)
        if pilih == "1":
            scan()
        elif pilih == "2":
            type(R + "[!] Keluar dari mode JARVIS..." + W)
            break
        else:
            type(R + "[!] Pilihan tidak valid!" + W)

# Run
main()
