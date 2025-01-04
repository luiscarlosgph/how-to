Using the system daemon
-----------------------

1. Install the required packages: `$ sudo apt install ifupdown net-tools wireless-tools`
   
2. Edit `$ vim /lib/systemd/system/wpa_supplicant.service` and modify the command line accordingly: 

```
ExecStart=/usr/sbin/wpa_supplicant -u -s -iwlan0 -c/etc/wpa_supplicant.conf -O "DIR=/run/wpa_supplicant GROUP=netdev"
```
If your wireless device is not `wlan0` modify the line above accordingly. 

3. Generate the configuration file: `$ wpa_passphrase "<essid>" "<password>" | sudo tee /etc/wpa_supplicant.conf

4. TODO

Standalone script
-----------------

Bash script to connect your Linux to a WPA/WPA2 network:

```
#!/bin/bash

IFACE="wlan0"
ESSID="TYPE_WIFI_NAME_HERE"
PASSWORD="TYPE_PASSWORD_HERE"

# Store ESSID and password
wpa_passphrase "$ESSID" "$PASSWORD" | sudo tee /etc/wpa_supplicant.conf

# Connect to the wireless access point in the background
sudo wpa_supplicant -B -c /etc/wpa_supplicant.conf -i $IFACE

# Setup IP address, netmask, DNS, and gateway with the information provided by the DHCP server
sudo dhclient $IFACE
```
