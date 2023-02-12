Install 
-------
Install the bridge utils: `$ sudo apt install bridge-utils`

This software allows you to set up and use the bridge interface. The bridge interface appears as a new interface in ip link, much like eth0 or eth1. It does not physically exist on your computer, but instead it is a virtual interface that just takes the packets from one physical interface, and transparently routes them to the other.


Configure
---------
1. Create bridge network adapter: `$ sudo brctl addbr br0`
2. Specify the network interfaces to bridge (e.g. eth0 and eth1): `$ sudo brctl addif br0 eth0 eth1`
3. Edit your `$ sudo vim /etc/network/interfaces` to make the bridge permanent and configure the IP network parameters:
```
 # The loopback network interface
 auto lo
 iface lo inet loopback

 # Set up interfaces manually, avoiding conflicts with, e.g., network manager
 iface eth0 inet manual
 iface eth1 inet manual

 # Bridge setup
 auto br0
 iface br0 inet static
    bridge_ports eth0 eth1
        address 192.168.1.2
        broadcast 192.168.1.255
        netmask 255.255.255.0
        gateway 192.168.1.1
```
