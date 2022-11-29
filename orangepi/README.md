Description
-----------

Configuration files and how-to guides for the [Orange Pi](http://www.orangepi.org/).

Setup
-----

1. **apt**: 

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

2. **Wireless Access Point (AP)**: 

   Setup AP following [this guide](https://github.com/luiscarlosgph/how-to/tree/main/access_point), but use this configuration for `/etc/hostapd.conf`:

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
   
3. **Wireless DHCP server**: 
   
   ```bash
   $ sudo apt install isc-dhcp-server
   ```
   
   Edit config file `$ sudo vim /etc/dhcp/dhcpd.conf`:
   
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
   
   Edit config file `$ sudo vim /etc/default/isc-dhcp-server`:
   
   ```
   INTERFACESv4="wlan0"
   ```
   
   Configure IP address of the wireless adapter, edit `$ sudo vim /etc/network/interfaces`:
   
   ```
   TODO
   ```
   
   Enable DHCP server:
   
   ```
   $ sudo systemctl enable isc-dhcp-server
   ```
   
4. **Uninstall network-manager**: it interferes with the configuration in `/etc/network/interfaces`
   
   ```bash
   $ sudo apt remove network-manager
   ```
