```
# Download and install
$ cd /usr/local/src/
$ sudo wget http://www.noip.com/client/linux/noip-duc-linux.tar.gz
$ sudo tar xf noip-duc-linux.tar.gz
$ cd noip-2.1.9-1/
$ sudo make install

# Configure the DNS names to be updated
$ sudo /usr/local/bin/noip2 -C
```

To start the no-ip client from boot run `crontab -e` as root and add `@reboot /usr/local/bin/noip2`.
