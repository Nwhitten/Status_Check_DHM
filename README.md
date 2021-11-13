
## Installation

### Automatic

`wget -O - https://raw.githubusercontent.com/nwhitten/Status_Check_DHM/main/install.sh | sudo bash`


you will also need to install the following:


`sudo apt update`
`sudo raspi-config nonint do_spi 0`
`sudo apt install python-rpi.gpio python-spidev python-pip python-pil python-numpy`
`sudo pip3 install st7789`

PiHole-api `sudo python3 -m pip install --no-cache-dir PiHole-api`

`(crontab -l; echo "*/1 * * * * python3 /usr/local/bin/status_check_DHM/DHM_update.py";) | crontab -`
to install cron job to refresh pihole stats on inky-phat every 1 min