Bash script to connect your Linux to a WPA/WPA2 network:

```
#!/bin/bash

IFACE="wlan0"
ESSID="TYPE_WIFI_NAME_HERE"
PASSWORD="TYPE_PASSWORD_HERE"

# Store ESSID and password
wpa_passphrase $ESSID $PASSWORD | sudo tee /etc/wpa_supplicant.conf

# Connect to the wireless access point in the background
sudo wpa_supplicant -B -c /etc/wpa_supplicant.conf -i $IFACE

# Setup IP address, netmask, DNS, and gateway with the information provided by the DHCP server
sudo dhclient $IFACE
```
