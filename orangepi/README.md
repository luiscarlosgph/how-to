Description
-----------

Configuration files and how-to guides for the [Orange Pi](http://www.orangepi.org/).

Setup
-----

* **apt**: 

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

* **Wireless Access Point (AP)**: 

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
   
* **Wireless DHCP server**: 
   
   TODO
   
* **Uninstall network-manager**: it interferes with the configuration in `/etc/network/interfaces`
   
   ```bash
   $ sudo apt remove network-manager
   ```
