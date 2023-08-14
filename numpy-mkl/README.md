Description
-----------

This tutorial explains how to install numpy linked to [Intel MKL](https://en.wikipedia.org/wiki/Math_Kernel_Library).

Numpy usually comes linked to [OpenBLAS](https://www.openblas.net). Intel MKL is faster, that is the point of this tutorial.

1. Install Intel MKL as shown [here](https://github.com/luiscarlosgph/how-to/tree/main/intel-mkl) and then make it visible:

   ```bash
   $ export LD_LIBRARY_PATH=/opt/intel/oneapi/mkl/latest/lib/intel64:${LD_LIBRARY_PATH}
   ```

3. Download numpy source code:

   ```bash
   $ git clone https://github.com/numpy/numpy.git
   ```

4. Find the last release [here](https://github.com/numpy/numpy/releases) and get it:

   ```bash
   $ git checkout v1.25.2
   ```

5. Install numpy linked to MKL:

   ```bash
   $ echo "[mkl]" >> site.cfg
   $ echo "library_dirs = /opt/intel/oneapi/mkl/latest/lib/intel64" >> site.cfg
   $ echo "include_dirs = /opt/intel/oneapi/mkl/latest/include" >> site.cfg
   $ echo "libraries = mkl_rt" >> site.cfg
   $ python setup.py install
   ```
