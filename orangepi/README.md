Description
-----------

Configuration files and how-to guides for the [Orange Pi](http://www.orangepi.org/).

Setup apt
---------

   Usually the card comes with unofficial repos, replace the existing `/etc/apt/sources.list` by this one:
   
   ```
   deb http://ports.ubuntu.com/ubuntu-ports jammy main restricted universe multiverse
   #deb-src http://ports.ubuntu.com/ubuntu-ports jammy main restricted universe multiverse

   deb http://ports.ubuntu.com/ubuntu-ports jammy-security main restricted universe multiverse
   #deb-src http://ports.ubuntu.com/ubuntu-ports jammy-security main restricted universe multiverse

   deb http://ports.ubuntu.com/ubuntu-ports jammy-updates main restricted universe multiverse
   #deb-src http://ports.ubuntu.com/ubuntu-ports jammy-updates main restricted universe multiverse

   deb http://ports.ubuntu.com/ubuntu-ports jammy-backports main restricted universe multiverse
   #deb-src http://ports.ubuntu.com/ubuntu-ports jammy-backports main restricted universe multiverse
   ```

Configure Orange Pi as a wireless access point (AP)
---------------------------------------------------

1. **Setup AP**:

   ```
   $ sudo apt install hostapd
   ```
   
   `$ sudo vim /etc/hostapd.conf`:
   
   ```
   driver=nl80211
   interface=wlan0
   ssid=Orange
   #bridge=br0
   hw_mode=g
   channel=5
   wmm_enabled=1
   auth_algs=1
   wpa=2
   wpa_key_mgmt=WPA-PSK
   rsn_pairwise=CCMP
   wpa_passphrase=1234567890
   ```
 
   `$ sudo vim /etc/default/hostapd`:
   
   ```
   DAEMON_CONF="/etc/hostapd.conf"
   ```
   
2. **Uninstall network-manager**: it interferes with the configuration in `/etc/network/interfaces`
   
   ```bash
   $ sudo apt remove network-manager
   ```
   
3. **Wireless DHCP server**: 
   
   ```bash
   $ sudo apt install isc-dhcp-server
   ```
   
   `$ sudo vim /etc/dhcp/dhcpd.conf`:
   
   ```
   default-lease-time 600;
   max-lease-time 7200;
   authoritative;
 
   subnet 10.0.0.0 netmask 255.255.255.0 {
      range 10.0.0.1 10.0.0.254;
      option broadcast-address 10.0.0.255; 
      option routers 10.0.0.1;
      option domain-name-servers 8.8.8.8;
   }
   ```
   
   `$ sudo vim /etc/default/isc-dhcp-server`:
   
   ```
   INTERFACESv4="wlan0"
   ```
   
   Configure IP address of the wireless adapter, `$ sudo vim /etc/network/interfaces`:
   
   ```
   auto lo
   iface lo inet loopback

   allow-hotplug eth0
   iface eth0 inet dhcp

   auto wlan0
   iface wlan0 inet static
	    address 10.0.0.1/24
   ```
   
   Enable DHCP server:
   
   ```
   $ sudo systemctl enable isc-dhcp-server
   ```
   
4. **Redirect wireless traffic to the wired connection**:
   
   Create a firewall script via `sudo vim /etc/network/if-up.d/nat`:
   
   ```
   #!/bin/bash

   # Flush previous rules, delete chains and reset counters
   iptables -F
   iptables -X
   iptables -Z
   iptables -t nat -F

   # Default policies
   iptables -P INPUT   DROP
   iptables -P OUTPUT  ACCEPT
   iptables -P FORWARD ACCEPT

   # Allow local programs that use loopback (Unix sockets)
   iptables -A INPUT -s 127.0.0.0/8 -d 127.0.0.0/8 -i lo -j ACCEPT

   # Allow established connections (the responses to our outgoing traffic)
   iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

   # Allow incoming connections to our SSH server
   iptables -A INPUT -p tcp --dport 22 -m state --state NEW -j ACCEPT

   # Behave as a NAT router
   echo 1 > /proc/sys/net/ipv4/ip_forward
   iptables -t nat -A POSTROUTING -s '10.0.0.0/24' -o eth0 -j MASQUERADE
   ```
   
   Give execution permissions to the firewall script above:
   ```
   $ sudo chmod +x /etc/network/if-up.d/nat
   ```

<!--
Network failover
----------------

Let's say we have two network interfaces, `eth0` and `usb0`. By default, we want to use `eth0`, but when there is no Internet access via `eth0`, we want to switch to `usb0`.
-->


Connect Orange Pi to a wireless access point from boot
------------------------------------------------------

1. Create a script in `/home/orangepi/wpa_client.sh`:
   ``` 
   #!/bin/bash

   IFACE="wlan0"
   ESSID="WIFI_NAME_HERE"
   PASSWORD="WIFI_PASSWORD_HERE"

   # Store ESSID and password
   wpa_passphrase "$ESSID" "$PASSWORD" | sudo tee /etc/wpa_supplicant.conf

   # Connect to the wireless access point in the background
   sudo wpa_supplicant -B -c /etc/wpa_supplicant.conf -i $IFACE

   # Setup IP address, netmask, DNS, and gateway with the information provided by the DHCP server
   sudo dhclient $IFACE
   ```

2. Give execution permissions: `chmod +x /home/orangepi/wpa_client.sh`

3. Stop wpa supplicant daemon:
   ```
   $ sudo systemctl stop wpa_supplicant
   $ sudo systemctl disable wpa_supplicant
   ```

4. Edit `/etc/rc.local` and add `/home/orangepi/wpa_client.sh` before the `exit 0` line.
