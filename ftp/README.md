Description
-----------

This guide shows how to quickly deploy an FTP server to share files in a local network.

* Use case: you are in a WiFi network and want to share a file from a Mac to a Windows but do not have USB sticks.


Inatall and configure FTP server on a Mac
-----------------------------------------

1. Install Python 3 if you do not have it. You have a simple tutorial to install it [here](https://github.com/luiscarlosgph/how-to/tree/main/pyenv).

2. Install the server:
   ```bash
   $ pip install pyftpdlib
   ```
     
3. Run FTP server:
   ```bash
   $ python3 -m pyftpdlib -p 2121 -d Public
   ```
   * `-p` indicates the listening port.
   * `-d` the path to the directory that will be shared via FTP.

4. Get your IP address from `System Settings` -> `Wi-Fi` -> `Details` -> `TCP/IP` -> `IP address`. 

5. Connect to `ftp://<ip_address>:2121` from your other computer. For example, `ftp://192.168.0.124:2121`.
   I use [Cyberduck](https://cyberduck.io/) as FTP client, but you can use whichever your prefer, including
   the one that comes natively with Windows and Mac.
