```bash
$ sudo apt install bison libbison-dev flex libfl-dev
$ sudo apt install linux-headers-current-sunxi64
$ cd /usr/src/linux-headers-6.6.62-current-sunxi64/
$ sudo make scripts
$ cd
$ git clone https://github.com/umlaeute/v4l2loopback.git
$ cd v4l2loopback/
$ make && sudo make install
$ sudo depmod -a
$ cd
$ sudo apt install liblog4cpp5-dev cmake
$ git clone https://github.com/mpromonet/libv4l2cpp.git
$ cd libv4l2cpp/
$ mkdir build
$ cd build
$ cmake ..
$ make
$ sudo mkdir /usr/include/libv4l2cpp/
$ sudo make install
```
