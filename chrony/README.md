How to synchronise computers via NTP
------------------------------------
Chrony is both an NTP client and server.

Server
------
1. Install NTP server: `$ sudo apt install chrony`
2. Edit **chrony** configuration file: `$ sudo vim /etc/chrony/chrony.conf`
```
# NTP servers, go to https://www.ntppool.org and choose those from your desired country
server 0.fr.pool.ntp.org iburst
server 1.fr.pool.ntp.org iburst
server 2.fr.pool.ntp.org iburst
server 3.fr.pool.ntp.org iburst

# IP addresses or ranges allowed to access the chrony NTP server
allow 127.0.0.1
allow 10.0.0.0/8
allow 192.168.0.0/16

keyfile /etc/chrony/chrony.keys
driftfile /var/lib/chrony/chrony.drift
local stratum 8
manual
logdir /var/log/chrony
maxupdateskew 100.0
rtcsync
makestep 1 3
#smoothtime 400 0.01
```
3. Restart service: `$ sudo systemctl restart chrony`
4. Enable chrony from boot: `$ sudo systemctl enable chrony`

Clients
-------
1. Install NTP client: `$ sudo apt install chrony`
2. Edit **chrony** configuration file: `$ sudo vim /etc/chrony/chrony.conf`
```
# Assuming that 192.168.8.100 is the IP address of your NTP server
server 192.168.8.100 iburst prefer

keyfile /etc/chrony/chrony.keys
driftfile /var/lib/chrony/chrony.drift
logdir /var/log/chrony
maxupdateskew 100.0
rtcsync
makestep 1 3
```
3. Restart service: `$ sudo systemctl restart chrony`
4. Enable chrony from boot: `$ sudo systemctl enable chrony`

Setup your timezone and activate the use of NTP (both client and server)
------------------------------------------------------------------------
Timezone: 
```
$ sudo timedatectl set-timezone "Europe/Paris"
```

Set your computer's RTC to the local timezone:
```
$ sudo timedatectl set-local-rtc 1
```

Enable NTP sync:
```
$ sudo timedatectl set-ntp true
```
