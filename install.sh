#!/bin/bash

printf "Start installing Dummy-DNS package\n"

# Set APP_ENV for production
printf "Setting up the environment..."
export APP_ENV=production

printf "Building script ...\n"
pyinstaller --onefile main.py

printf "Copying files...\n" 
sudo cp -v -f ./dist/main /usr/local/bin/dummy-dns
sudo chmod +x /usr/local/bin/dummy-dns

printf "Save default config into /etc/dummy-dns/default.conf\n"
# Check if /etc/dummy-dns exists or not
if [ ! -d "/etc/dummy-dns" ]; then
    sudo mkdir /etc/dummy-dns
fi

# Backup configuration file
sudo cp /etc/resolv.conf /etc/dummy-dns/default.conf

printf "Installation is completed.\n"
