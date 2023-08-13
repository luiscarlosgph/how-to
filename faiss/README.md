Install [faiss](https://github.com/facebookresearch/faiss) with GPU support, usually called `faiss-gpu`
-------------------------------------------------------------------------------------------------------

1. Install the dependencies:
   * A C++17 compiler (with support for OpenMP version 2 or higher):
     
      `g++` supports C++17 since version 7, so you should have a `g++` version >= 7. Do not worry about the OpenMP requirement, OpenMP 4.5 is fully supported since `g++` version 6.
        
      In Ubuntu `20.04`, the `g++` version is `X.X.X`, which complies with both requirements, to install it along with CMake, which is also needed, run:

      ```bash
      $ sudo apt install g++ build-essential git cmake
      ```
        
      * A BLAS implementation (use Intel MKL for best performance), see [this](https://github.com/luiscarlosgph/how-to/tree/main/intel-mkl) tutorial on how to install it.
      * CUDA toolkit, see [this](https://github.com/luiscarlosgph/how-to/tree/main/cuda-toolkit) tutorial on how to install it.
      * Python 3 with numpy: if you do not have it already, you could install any Python 3 version >= 3.10 following [this](https://github.com/luiscarlosgph/how-to/tree/main/pyenv) tutorial, and then install numpy with `$ pip install numpy`.
   
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


2. Download faiss: `$ git clone https://github.com/facebookresearch/faiss.git`


3. Inatall the last release (you can find the last release version [here](https://github.com/facebookresearch/faiss/releases)):
   ```bash
   $ cd faiss
   $ git checkout v1.7.4
   $ mkdir build
   $ cd build
   $ cmake -DFAISS_ENABLE_GPU=ON -DFAISS_ENABLE_PYTHON=ON -DBUILD_TESTING=ON -DBUILD_SHARED_LIBS=ON -DFAISS_ENABLE_C_API=ON -DCMAKE_BUILD_TYPE=Release -DFAISS_OPT_LEVEL=avx2 -DBLA_VENDOR=Intel10_64_dyn -DBLA_VENDOR=Intel10_64_dyn -DMKL_LIBRARIES=/opt/intel/oneapi/mkl/latest/lib -DCUDAToolkit_ROOT=/usr/local/cuda -DPython_EXECUTABLE=$HOME/.pyenv/shims/python -DPython_INCLUDE_DIRS=$HOME/.pyenv/versions/3.10.12/include -DPython_LIBRARIES=$HOME/.pyenv/versions/3.10.12/lib ..
   $ make -j faiss
   $ make -j swigfaiss
   $ (cd build/faiss/python && python setup.py install)
   $ sudo make install
   ```


4. Run the test suite to check that it works:

   ```bash
   $ make -C build test
   $ (cd build/faiss/python && python setup.py build)
   $ PYTHONPATH="$(ls -d ./build/faiss/python/build/lib*/)" pytest tests/test_*.py
   ```
