Description
-----------

This guide shows how to quickly deploy an FTP server to share files in a local network.

* Exemplary use case: you are in a WiFi network and want to share a file from a Mac to a Windows but do not have USB sticks.


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
