import os
import socket
import requests
import platform

def banner():
    os.system("clear")
    print("\033[1;36m")
    print("╔═════════════════════════════╗")
    print("║      NETWORK TOOLS v1.0     ║")
    print("║        By: Nuril Project    ║")
    print("╚═════════════════════════════╝\033[0m")

def check_connection():
    try:
        requests.get("https://www.google.com", timeout=5)
        print("\033[1;32m[✔] Koneksi Internet: Tersambung\033[0m")
    except:
        print("\033[1;31m[✘] Koneksi Internet: Tidak Tersambung\033[0m")

def get_local_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(f"\033[1;34m[•] IP Lokal: {ip}\033[0m")

def get_public_ip():
    try:
        ip = requests.get("https://api.ipify.org").text
        print(f"\033[1;34m[•] IP Publik: {ip}\033[0m")
    except:
        print("\033[1;31m[!] Gagal mengambil IP publik\033[0m")

def ping_target():
    target = input("Masukkan host (contoh: google.com): ")
    os.system(f"ping -c 4 {target}")

def scan_lan():
    print("\n\033[1;33m[!] Scan hanya menampilkan IP aktif di jaringan...\033[0m")
    ip_base = input("Masukkan IP dasar (contoh 192.168.1): ")
    for i in range(1, 10):
        ip = f"{ip_base}.{i}"
        response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null")
        if response == 0:
            print(f"\033[1;32m[+] Aktif: {ip}\033[0m")
        else:
            print(f"\033[1;31m[-] Tidak aktif: {ip}\033[0m")

def menu():
    while True:
        print("\n1. Cek Koneksi Internet")
        print("2. Lihat IP Lokal & Publik")
        print("3. Ping Target")
        print("4. Scan Perangkat di Jaringan")
        print("5. Exit")
        pilih = input("\nPilih opsi: ")

        if pilih == "1":
            check_connection()
        elif pilih == "2":
            get_local_ip()
            get_public_ip()
        elif pilih == "3":
            ping_target()
        elif pilih == "4":
            scan_lan()
        elif pilih == "5":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    banner()
    menu()
