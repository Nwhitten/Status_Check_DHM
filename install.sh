#!/bin/bash

echo ""

echo "Downloading files..."

wget https://raw.githubusercontent.com/nwhitten/Status_Check_DHM/main/DHM_update.py
wget https://raw.githubusercontent.com/nwhitten/Status_Check_DHM/main/DHM_updateLoop.py

wget https://raw.githubusercontent.com/nwhitten/Status_Check_DHM/main/inky-hole_assets/DHM_cog.jpg
wget https://raw.githubusercontent.com/nwhitten/Status_Check_DHM/main/inky-hole_assets/DHM_pihole.jpg
wget https://raw.githubusercontent.com/nwhitten/Status_Check_DHM/main/inky-hole_assets/DHM_rasp.jpg

wget https://raw.githubusercontent.com/nwhitten/Status_Check_DHM/main/inky-hole_assets/ArialUnicode.ttf
wget https://raw.githubusercontent.com/nwhitten/Status_Check_DHM/main/inky-hole_assets/ArialBold.ttf

echo ""

echo "Removing old files files..."
rm -r /usr/local/bin/status_check_DHM
rm /usr/share/fonts/ArialUnicode.ttf
rm /usr/share/fonts/ArialBold.ttf

echo ""

mkdir /usr/local/bin/status_check_DHM/

echo "Moving files..."

mv DHM_update.py /usr/local/bin/status_check_DHM/
mv DHM_updateLoop.py /usr/local/bin/status_check_DHM/

mv DHM_cog.jpg /usr/local/bin/status_check_DHM/
mv DHM_pihole.jpg /usr/local/bin/status_check_DHM/
mv DHM_rasp.jpg /usr/local/bin/status_check_DHM/

mv ArialUnicode.ttf /usr/share/fonts/
mv ArialBold.ttf /usr/share/fonts/

