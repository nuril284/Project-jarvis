#!/data/data/com.termux/files/usr/bin/bash

cd ~/Project-jarvis
echo ">>> Backup dimulai..."
git add .
git commit -m "Backup otomatis $(date)"
git push origin main
