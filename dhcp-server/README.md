Install DHCP server
-------------------
```
$ sudo apt install isc-dhcp-server
```

Configure the DHCP server
-------------------------
1. Edit config file `$ sudo vim /etc/dhcp/dhcpd.conf` and add:

```
default-lease-time 600;
max-lease-time 7200;
authoritative;
 
subnet 192.168.8.0 netmask 255.255.255.0 {
 range 192.168.8.100 192.168.8.200;
 option routers 192.168.8.1;
 option domain-name-servers 8.8.8.8, 4.4.4.4;
#option domain-name "mydomain.example";
}
```

2. Specify the listening interfaces editing `$ sudo vim /etc/default/isc-dhcp-server`, e.g.:
```
INTERFACESv4="wlan0"
```

3. Set it to run at boot: 
```
$ sudo systemctl enable isc-dhcp-server
```

Configure the system to behave as a NAT router
----------------------------------------------
1. Create firewall + gateway configuration file ```$ sudo vim /etc/network/if-up.d/nat```:
```bash
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
iptables -t nat -A POSTROUTING -s '192.168.8.0/24' -o eth0 -j MASQUERADE
```

2. Give execution permissions: 
```
$ sudo chmod +x /etc/network/if-up.d/nat
```
