Description
-----------

Configuration files and how-to guides for the [Orange Pi](http://www.orangepi.org/).

Setup
-----

* **apt**: 

   Usually the card comes with unofficial repos, replace the existing `/etc/apt/sources.list` by [this one](sources.list).

* **Wireless access point**. Setup AP following [this guide](https://github.com/luiscarlosgph/how-to/tree/main/access_point), but use this configuration for `/etc/hostapd.conf`:

   ```
   interface=wlan0
   driver=nl80211
   #bridge=br0
   hw_mode=g
   channel=5
   ieee80211n=1
   wmm_enabled=1
   ht_capab=[HT40]
   macaddr_acl=0
   ssid=Orange
   auth_algs=1
   wpa=2
   wpa_key_mgmt=WPA-PSK
   rsn_pairwise=CCMP
   wpa_passphrase=1234567890
   ```
