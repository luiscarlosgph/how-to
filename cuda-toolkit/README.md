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
   $ sudo ./cuda.run  # This command takes a bit of time to run, do not worry :)
   ```

   When you run this command on your terminal, you will see something like what is shown in the screenshots bellow, follow the same steps:

   ![Screenshot 2023-08-11 at 18 49 43](https://github.com/luiscarlosgph/how-to/assets/3996630/661f3bbd-d09b-4aca-a9a9-60efe01b65a2)

   ![Screenshot 2023-08-11 at 18 50 05](https://github.com/luiscarlosgph/how-to/assets/3996630/0f1bac1e-85c5-465e-a91d-2e9123b0560a)

   ![Screenshot 2023-08-11 at 18 50 43](https://github.com/luiscarlosgph/how-to/assets/3996630/cd162f1b-4441-4d41-b638-0df65c141b5e)

   **It is very important that you untick the checkbox of the driver**, if you have followed this guide your NVIDIA driver is already installed.

   Click `Install` to install the CUDA toolkit.
   

5. Delete the CUDA installation file: `$ rm /tmp/cuda.run`
