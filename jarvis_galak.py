import os
import time

os.system("clear")

def print_delay(teks, delay=0.03):
    for huruf in teks:
        print(huruf, end='', flush=True)
        time.sleep(delay)
    print()

def garis():
    print("\033[1;31m" + "="*60 + "\033[0m")

banner = """
\033[1;31m
     ██╗ █████╗ ██████╗ ██╗██╗     ██████╗ 
     ██║██╔══██╗██╔══██╗██║██║     ██╔══██╗
     ██║███████║██████╔╝██║██║     ██║  ██║
██   ██║██╔══██║██╔═══╝ ██║██║     ██║  ██║
╚█████╔╝██║  ██║██║     ██║███████╗██████╔╝
 ╚════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═════╝ 
\033[1;37m     >>> SYSTEM LOCKED by NURIL <<<
"""

os.system("termux-vibrate -d 150")
print(banner)
garis()
print_delay(">> WARNING: Akses tidak sah akan dilaporkan otomatis.", 0.04)
print_delay(">> Autentikasi Nuril... VALID", 0.05)
print_delay(">> Menyuntikkan sistem pemantauan jaringan...", 0.04)
print_delay(">> Sistem perlindungan AKTIF", 0.04)
garis()

while True:
    print("""
\033[1;31m[1] Pantau Aktivitas IP
[2] Tampilkan Log Sistem
[3] Bersihkan Jejak
[4] Keluar (Nonaktifkan Sistem)\033[0m
""")
    cmd = input(">> Nuril_Sec > ")

    if cmd == "1":
        print_delay(">> Memindai IP target...", 0.03)
        os.system("curl ifconfig.me")
    elif cmd == "2":
        print_delay(">> Mengakses file log...", 0.03)
        os.system("dmesg | tail -n 10")
    elif cmd == "3":
        print_delay(">> Menghapus jejak digital...", 0.03)
        os.system("clear")
        print(banner)
    elif cmd == "4":
        print_delay(">> Sistem dihentikan. Otentikasi ulang diperlukan...", 0.03)
        break
    else:
        print_delay(">> PERINTAH TIDAK DIKENALI. SISTEM MENGAWASI.", 0.03)
