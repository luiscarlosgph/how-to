Install
-------
```
$ sudo apt install hostapd
```

Configure
---------
1. Edit config file: `$ sudo vim /etc/hostapd.conf`
```
# @brief   Hostap configuration for a simple but secure access point with minimal
#          compatibility for current hardware: 802.11b/g/n with WPA2-PSK and CCMP.

# Choose the userspace API to access the wireless stack
driver=nl80211

# The wireless interface used by the AP
interface=wlan0

# WARNING! IF YOU ARE NOT USING A BRIDGE, COMMENT THE NEXT LINE (i.e. bridge=br0)
# This option is only useful when you are running a DHCP server in a bridge
# interface (e.g. br0), for example a bridge between WiFi and Ethernet
bridge=br0

# "g" simply means 2.4GHz band
hw_mode=g

# The channel to use
channel=5

# QoS support, also required for full speed on 802.11n/ac/ax
wmm_enabled=1

# Name of the access point
ssid=Mango

# 1=wpa, 2=wep, 3=both
auth_algs=1

# WPA2 only
wpa=2
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
wpa_passphrase=1234567890
```

Run from boot
-------------
Edit `$ sudo vim /etc/default/hostapd` and uncomment the line:
```
DAEMON_CONF="/etc/hostapd.conf"
```
