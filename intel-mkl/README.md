Install Intel MKL in Ubuntu:

1. Add Intel repo to the `apt` list:

   ```bash
   $ sudo apt install -y wget
   $ wget -O- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB | gpg --dearmor | sudo tee /usr/share/keyrings/oneapi-archive-keyring.gpg > /dev/null
   $ echo "deb [signed-by=/usr/share/keyrings/oneapi-archive-keyring.gpg] https://apt.repos.intel.com/oneapi all main" | sudo tee /etc/apt/sources.list.d/oneAPI.list
   ```


2. Installing the library and Python packages:

   ```bash
   $ sudo apt update
   $ sudo apt install intel-mkl intelpython3
   ```
