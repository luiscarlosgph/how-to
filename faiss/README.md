Install [faiss](https://github.com/facebookresearch/faiss) with GPU support, usually called `faiss-gpu`
------------------------------------------------------------

1. Install the dependencies:
   * A C++17 compiler (with support for OpenMP version 2 or higher):
     
      `g++` supports C++17 since version 7, so you should have a `g++` version >= 7. Do not worry about the OpenMP requirement, OpenMP 4.5 is fully supported since `g++` version 6.
        
      In Ubuntu `22.04`, the `g++` version is `11.4.0`, which complies with both requirements, to install it along with CMake, which is also needed, run:

      ```bash
      $ sudo apt install g++ build-essential git cmake
      ```
        
      * A BLAS implementation (use Intel MKL for best performance), see [this](https://github.com/luiscarlosgph/how-to/tree/main/intel-mkl) tutorial on how to install it.
      * CUDA toolkit, see [this](https://github.com/luiscarlosgph/how-to/tree/main/cuda-toolkit) tutorial on how to install it.
      * Python 3 with numpy: if you do not have it already, you could install any Python 3 version >= 3.10 following [this](https://github.com/luiscarlosgph/how-to/tree/main/pyenv) tutorial, and then install numpy with `pip install numpy`.

2. Download faiss: `$ git clone https://github.com/facebookresearch/faiss.git`

3. Choose the last release (you can find the last release version [here](https://github.com/facebookresearch/faiss/releases)):
   ```bash
   $ cd faiss
   $ git checkout v1.7.4
   $ mkdir build
   $ 
   ```
