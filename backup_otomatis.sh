#!/bin/bash

echo "[*] Menyiapkan backup otomatis ke GitHub..."
git add .
git commit -m "Backup otomatis $(date)"
git push

echo "[✓] Backup selesai bro!"
