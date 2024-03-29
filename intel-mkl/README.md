Install Intel MKL in Ubuntu:

1. Add Intel repo to `apt`:

   ```bash
   $ sudo apt install -y wget
   $ wget https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB
   $ gpg --dearmor GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB
   $ sudo mv GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB.gpg /usr/share/keyrings/oneapi-archive-keyring.gpg
   $ echo "deb [signed-by=/usr/share/keyrings/oneapi-archive-keyring.gpg] https://apt.repos.intel.com/oneapi all main" > /etc/apt/sources.list.d/oneAPI.list
   $ sudo apt update
   ```


2. Installing the library and Python packages (15GB of free space required):

   ```bash
   $ sudo apt install intel-basekit    
   ```
   

   If you want all the Intel openAPI packages, run this instead (19GB of free space required):

   ```bash
   $ sudo apt install intel-basekit intel-hpckit intel-iotkit intel-dlfdkit intel-aikit intel-renderkit
   ```


3. Make the Intel MKL headers visible to the C/C++ compiler adding the following line at the end of your `$HOME/.bashrc` (if you use bash) or `$HOME/.zshrc` (if you use zsh):

   ```bash
   $ export CPATH=/opt/intel/oneapi/mkl/latest/include:${CPATH}
   ```


4. Make the Intel MKL libraries visible to [ld](https://linux.die.net/man/1/ld) adding the following line at the end of your `$HOME/.bashrc` (if you use bash) or `$HOME/.zshrc` (if you use zsh):

   ```bash
   $ export LD_LIBRARY_PATH=/opt/intel/oneapi/mkl/latest/lib/intel64:${LD_LIBRARY_PATH}
   ```
