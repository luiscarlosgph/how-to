Description
-----------

This guide explains you how to install any version of the NVIDIA driver without using the repositories of your Linux distribution. 

* Why not using the repositories? There are many ocassions when you need a specific version of the NVIDIA driver (e.g. CUDA support, bugs), and there is a limited offer of NVIDIA driver versions in the repos.


Install
-------

1. Find out which graphics card you have:
  ```
  $ lspci | grep VGA
  01:00.0 VGA compatible controller: NVIDIA Corporation GP102 [TITAN X] (rev a1)
  ```

2. Go to the NVIDIA website [here](https://www.nvidia.com/Download/Find.aspx) and search for your model (TITAN X following the example above):

  ![nvidia_search](https://user-images.githubusercontent.com/3996630/189359318-debc0b8a-7060-4c7d-a8b5-978ee308a218.png)

  Click `Search` and you will see this:
  
  ![driver_version](https://user-images.githubusercontent.com/3996630/189361233-afedb1de-32c6-4996-94b0-5ddc29a9a668.png)
  
  Click on the driver version you want. If you are in doubt, pick the most recent version number. After you click on a particular version you will see this:
  
  ![driver_download](https://user-images.githubusercontent.com/3996630/189362593-58cc9c69-e049-47e6-9547-c582b0409317.png)
  
  Click on `Download` and you will see this:
  
  ![actual_download](https://user-images.githubusercontent.com/3996630/189362659-cef006e2-3dd5-4202-921e-a9a6652b9fae.png)

  Right-click on the `Download` button and select `Copy link`. You now have copied the URL pointing to the driver in your clipboard.
  
3. Download driver:
  ```
  $ cd ~/Downloads
  $ wget <paste_link_from_clipboard_here>
  ```
  For example:
  ```
  $ cd ~/Downloads
  $ wget https://us.download.nvidia.com/XFree86/Linux-x86_64/515.65.01/NVIDIA-Linux-x86_64-515.65.01.run
  ```
  
4. Blacklist [nouveau](https://en.wikipedia.org/wiki/Nouveau_(software)) drivers:
   
   [Nouveau](https://en.wikipedia.org/wiki/Nouveau_(software)) is an open source driver for NVIDIA cards that comes installed in many Linux distributions. You do not want it because it does not support CUDA. Therefore, let's blacklist it so that the Linux kernel does not use it:
   
   ```
   TODO
   ```
   
5. Close graphical environment:

6. Install NVIDIA driver:

7. Reboot and enjoy!
   
