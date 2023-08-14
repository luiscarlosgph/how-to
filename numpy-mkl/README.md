Description
-----------

This tutorial explains how to install numpy linked to [Intel MKL](https://en.wikipedia.org/wiki/Math_Kernel_Library).

Numpy usually comes linked to [OpenBLAS](https://www.openblas.net). Intel MKL is faster, that is the point of this tutorial.

1. Install Intel MKL as shown [here](https://github.com/luiscarlosgph/how-to/tree/main/intel-mkl).

2. Download numpy source code:

   ```bash
   $ git clone https://github.com/numpy/numpy.git
   ```

3. Find the last release [here](https://github.com/numpy/numpy/releases) and get it:

   ```bash
   $ git checkout v1.25.2
   ```

4. Compile numpy linked to MKL:

   ```bash
   $ mkdir build
   $ cd build
   $ TODO
   ```
