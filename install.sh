#!/bin/bash

printf "Start installing Dummy-DNS package\n"

# shellcheck disable=SC1091
source .venv/bin/activate

printf "Biulding script...\n"
pyinstaller --onefile main.py

printf "Copying files...\n" 
sudo cp dist/main /usr/local/bin/dummy-dns
sudo chmod +x usr/local/bin/dummy-dns

printf "Save default config into /etc/dummy-dns/deafult.conf\n"
sudo cp /etc/resolv.conf /etc/dummy-dns/default.conf

printf "Installation is completed.\n"
