Description
-----------
Guide to install OpenCV.

From the repositories
---------------------
* Ubuntu/Debian
```
$ sudo apt update
$ sudo apt install libopencv-dev python3-opencv
```

From source
-----------
```bash
# Install OpenCV dependencies
$ sudo apt update
$ sudo apt install build-essential cmake git unzip pkg-config libgtk-3-dev libjpeg-dev libpng-dev libtiff-dev libatlas-base-dev libx264-dev python3-dev libv4l-dev libavcodec-dev libavformat-dev libavresample-dev libswscale-dev libxvidcore-dev gfortran openexr libtbb2 libtbb-dev libdc1394-22-dev libopenexr-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev

# Download OpenCV
$ git clone https://github.com/opencv/opencv.git
$ git clone https://github.com/opencv/opencv_contrib.git
$ cd opencv_contrib
$ git checkout 4.5.1
$ cd ../opencv
$ git checkout 4.5.1

# Compile OpenCV
$ mkdir build
$ cd build
$ cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_C_EXAMPLES=OFF -D INSTALL_PYTHON_EXAMPLES=OFF -D OPENCV_GENERATE_PKGCONFIG=ON -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules -D BUILD_EXAMPLES=OFF -D OPENCV_ENABLE_NONFREE=ON ..
$ make -j8

# Install OpenCV
$ sudo make install
$ sudo ldconfig
```
