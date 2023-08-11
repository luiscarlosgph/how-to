Guide to install the CUDA tookit
--------------------------------

Before you install the CUDA toolkit, you need to install the NVIDIA driver, to do so, follow [this](https://github.com/luiscarlosgph/how-to/tree/main/nvidia-driver) guide.

1. Find the CUDA version you want:

   Browse to [https://developer.nvidia.com/cuda-toolkit-archive](https://developer.nvidia.com/cuda-toolkit-archive), you will see something like this:

   ![Screenshot 2023-08-11 at 18 24 45](https://github.com/luiscarlosgph/how-to/assets/3996630/da4183b6-a081-496e-a52d-adc46f7713ea)

   Click on the version you want, you will see something like this:

   ![Screenshot 2023-08-11 at 18 27 28](https://github.com/luiscarlosgph/how-to/assets/3996630/0344480b-3c71-42f1-9c4e-fb876aa651b8)


2. Download the CUDA toolkit:

   Copy the download command that is displayed in the website, and append `-O /tmp/cuda.run`, as you see below:

   ```bash
   $ wget https://developer.download.nvidia.com/compute/cuda/12.2.1/local_installers/cuda_12.2.1_535.86.10_linux.run -O /tmp/cuda.run
   ```

3. Install the CUDA toolkit:

   ```bash
   $ cd /tmp
   $ sudo chmod +x cuda.run
   $ sudo ./cuda.run
   ```

   When you run this command on your terminal, you will see something like this:

   [image here]

   Untick the checkbox that installs the driver, if you have followed this guide your NVIDIA driver is already installed. 

5. Delete the cuda installation file: `$ rm /tmp/cuda.run`
