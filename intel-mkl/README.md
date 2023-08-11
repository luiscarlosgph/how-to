Install Intel MKL in Ubuntu:

1. Install the GPG key for the `apt` repository:

   ```bash
   $ sudo apt install -y wget
   $ cd /tmp
   $ wget https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
   $ apt-key add GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
   $ rm GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
   ```

2. Add the `apt` repository:

   ```bash
   $ sudo wget https://apt.repos.intel.com/setup/intelproducts.list -O /etc/apt/sources.list.d/intelproducts.list
   $ sudo apt update
   ```

3. Installing the library and Python packages:

   ```bash
   $ sudo apt install intel-mkl intelpython3
   ```
