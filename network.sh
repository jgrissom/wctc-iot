#!/bin/bash
clear
read -p 'Username: ' uservar
read -sp 'Password: ' passvar

# Hash your password
hashed_password=`echo -n $passvar | iconv -t utf16le | openssl md4`
hashed_password=$(echo $hashed_password | cut -d'=' -f 2)
hashed_password=${hashed_password:1}
# Clear your terminal history
history -c
history -w
# Create the wpa_suplicant.conf file
sudo rm /etc/wpa_supplicant/wpa_supplicant.conf

sudo tee /etc/wpa_supplicant/wpa_supplicant.conf <<EOF
ctrl_interface=DIR=/var/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
     ssid="WCTCSecure"
     priority=1
     proto=RSN
     key_mgmt=WPA-EAP
     pairwise=CCMP
     auth_alg=OPEN
     eap=PEAP
     identity="$uservar"
     password=hash:$hashed_password
     phase1="peaplabel=0"
     phase2="auth=MSCHAPV2"
}
EOF

sudo reboot 
