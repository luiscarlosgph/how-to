Install [faiss](https://github.com/facebookresearch/faiss) with GPU support, usually called `faiss-gpu`
-------------------------------------------------------------------------------------------------------

1. Install the dependencies:
          
   * A C++17 compiler (with support for OpenMP version 2 or higher):
     
      `g++` supports C++17 since version 7, so you should have a `g++` version >= 7. Do not worry about the OpenMP requirement, OpenMP 4.5 is fully supported since `g++` version 6. To install it run:

      ```bash
      $ sudo apt install -y build-essential g++ git
      ```

   * Install the last version of CMake:
       * Delete current versions of CMake: `$ sudo apt remove --purge --auto-remove cmake`
       * Download CMake: `$ git clone https://github.com/Kitware/CMake.git`
       * Install the last stable release (you can find the last stable release [here](https://github.com/Kitware/CMake/releases)):
      
          ```bash
          $ cd CMake
          $ git checkout v3.27.2
          $ ./bootstrap
          $ make -j
          $ sudo make install
          ```
        
   * A BLAS implementation (use Intel MKL for best performance), see [this](https://github.com/luiscarlosgph/how-to/tree/main/intel-mkl) tutorial on how to install it.
   
   * CUDA toolkit, see [this](https://github.com/luiscarlosgph/how-to/tree/main/cuda-toolkit) tutorial on how to install it.
   
   * Python >= 3.10 with NumPy-MKL:
      * To install Python version >= 3.10 follow [this](https://github.com/luiscarlosgph/how-to/tree/main/pyenv) tutorial.
      * To install NumPy with MKL support: 

         ```bash
         $ TODO
         ```

   
1. Download faiss: `$ git clone https://github.com/facebookresearch/faiss.git`


2. Install the last release (you can find the last release version [here](https://github.com/facebookresearch/faiss/releases)):

   ```bash
   $ cd faiss
   $ git checkout v1.7.4
   $ mkdir build
   $ cd build
   $ cmake -DFAISS_ENABLE_GPU=ON -DFAISS_ENABLE_PYTHON=ON -DBUILD_TESTING=OFF -DBUILD_SHARED_LIBS=ON -DFAISS_ENABLE_C_API=ON -DCMAKE_BUILD_TYPE=Release -DFAISS_OPT_LEVEL=avx2 -DBLA_VENDOR=Intel10_64_dyn -DBLA_VENDOR=Intel10_64_dyn -DMKL_LIBRARIES="-L/opt/intel/oneapi/mkl/latest/lib/intel64 -lmkl_core -lmkl_sequential" -DCUDAToolkit_ROOT=/usr/local/cuda -DPython_EXECUTABLE=$HOME/.pyenv/shims/python -DPython_INCLUDE_DIRS=$HOME/.pyenv/versions/3.10.12/include -DPython_LIBRARIES=$HOME/.pyenv/versions/3.10.12/lib ..
   $ make -j faiss
   $ make -j swigfaiss
   $ sudo make install
   $ cd faiss/python && python setup.py install
   ```

   The `$ cmake` line above assumes that:
      1. You are using `pyenv` (as shown [here](https://github.com/luiscarlosgph/how-to/tree/main/pyenv)) with Python version `3.10.12`.
      2. You have your MKL libraries located in `/opt/intel/oneapi/mkl/latest/lib/intel64`.

   If you have a different configuration in your system, you have to modify the CMake variables accordingly.

<!--
4. Run the test suite to check that it works:

   ```bash
   $ make test
   $ cd faiss/python && python setup.py build
   $ PYTHONPATH="$(ls -d ./faiss/python/build/lib*/)" pytest tests/test_*.py
   ```
-->
