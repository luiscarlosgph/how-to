Install Intel MKL in Ubuntu:

1. Install the GPG key for the `apt` repository:

   ```bash
   $ sudo apt install -y wget
   $ wget -O- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB | gpg --dearmor | sudo tee /usr/share/keyrings/oneapi-archive-keyring.gpg > /dev/null
   ```


2. Installing the library and Python packages:

   ```bash
   $ sudo apt update
   $ sudo apt install intel-mkl intelpython3
   ```
