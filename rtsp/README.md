1. Install dependencies:

```
$ sudo apt install linux-headers-current-sunxi64 bison libbison-dev flex libfl-dev liblog4cpp5-dev cmake libvpx-dev libx264-dev libx265-dev libjpeg-dev libtool
```

2. TODO:

```bash
$ cd /usr/src/linux-headers-6.6.62-current-sunxi64/
$ sudo make scripts
$ cd
$ git clone https://github.com/umlaeute/v4l2loopback.git
$ cd v4l2loopback/
$ make && sudo make install
$ sudo depmod -a
$ cd
$ git clone https://github.com/mpromonet/libv4l2cpp.git
$ cd libv4l2cpp/
$ mkdir build
$ cd build
$ cmake ..
$ make
$ sudo mkdir /usr/include/libv4l2cpp/
$ sudo cp liblibv4l2cpp.a /usr/include/libv4l2cpp/
```
