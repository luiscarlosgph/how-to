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
   
   If the output of this command does not show the exact model of your GPU, but something like:
   ```
   00:02.0 VGA compatible controller: Intel Corporation Device 9a60 (rev 01)
   01:00.0 VGA compatible controller: NVIDIA Corporation Device 24b8 (rev a1)
   ```
   Let's ignore the Intel GPU and concentrate on discovering what model of NVIDIA card you have. In the example above, the Device PCI ID of the NVIDIA card is `24b8`. To find out which model corresponds to this Device PCI ID:
   1. Click [here](https://download.nvidia.com/XFree86/Linux-x86_64/latest.txt) and check what is the lastest version of the NVIDIA driver. You will see two columns separated by a space, the version is located in the first column, it should be something like `515.76`.
   2. Go [here](https://download.nvidia.com/XFree86/Linux-x86_64/) and click on the link corresponding to the lastest version of the driver (which you discovered in the previous step), e.g. `515.76`.
   3. Navigate to `README` -> `A. Supported NVIDIA GPU Products` (usually located at the bottom of the page).
   4. Find the device number, e.g. `24b8` in the example above. Your NVIDIA card model will be written next to it.
   
2. Go to the NVIDIA website [here](https://www.nvidia.com/Download/Find.aspx) and search for your model (TITAN X following the example above):
   
   If you do not know the `Product Series` of your card, you can probably find it [here](https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units) if you search for your card model.

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
   $ wget <paste_link_from_clipboard_here> -O nvidia_driver.sh
   ```
   For example:
   ```
   $ cd ~/Downloads
   $ wget https://us.download.nvidia.com/XFree86/Linux-x86_64/515.65.01/NVIDIA-Linux-x86_64-515.65.01.run -O nvidia_driver.sh
   ```
  
4. Blacklist [nouveau](https://en.wikipedia.org/wiki/Nouveau_(software)) drivers:
   
   [Nouveau](https://en.wikipedia.org/wiki/Nouveau_(software)) is an open source driver for NVIDIA cards that comes installed in many Linux distributions. You do not want it because it does not support CUDA. Therefore, let's blacklist it so that the Linux kernel does not use it:
   
   ```
   $ sudo bash -c "echo blacklist nouveau > /etc/modprobe.d/blacklist-nvidia-nouveau.conf"
   $ sudo bash -c "echo options nouveau modeset=0 >> /etc/modprobe.d/blacklist-nvidia-nouveau.conf"
   $ sudo update-initramfs -u
   $ sudo reboot
   ```
   
5. Warning! Before you keep going, open this website in another computer/phone, in the next step your monitor will turn into a black screen with a single terminal which will not allow you to browse the Internet. 

6. Press `Ctrl+Alt+F4`, a black screen will appear in front of you with a terminal asking you to `login:`. Write your username, click Enter, write your password, click Enter again. Now you are logged in and should see a terminal.

7. Now you need to kill your display manager. It is possible that you have no idea what a display manager is, in that case you might want to read [this](https://itsfoss.com/display-manager). It might also happen that you do not know which display manager you are using. Two typical ones are [lightdm](https://en.wikipedia.org/wiki/LightDM) and [GDM](https://en.wikipedia.org/wiki/GNOME_Display_Manager), but if you are not sure just kill them all:
   ```
   $ sudo /etc/init.d/gdm3 stop
   $ sudo /etc/init.d/lightdm stop
   ```
   
   Naturally, when you run the command to kill the display manager that you do not have you will see a message like `command not found`, no worries, keep killing them.
   After you kill your display manager with any of the commands above, your screen might turn black, to come back to your terminal simply press `Ctrl+Alt+F4`.
   
8. Remove old NVIDIA drivers that might be installed in your system:

   ```
   $ sudo apt remove 'nvidia-*'
   ```

9. Install the downloaded NVIDIA driver:

   ```
   $ cd ~/Downloads
   $ chmod +x nvidia_driver.sh
   $ sudo ./nvidia_driver.sh
   ```
   
   Click always the options that will allow you to continue with the installation, and say that **you do not want**, neither the 32-bit compatibility libraries, nor [DKMS](https://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support). Reply `Yes` to running the `nvidia-config` utility.
   
10. Run `$ sudo rm /etc/X11/xorg.conf` to delete the config file of the X server and let it detect your screen setup automatically.

11. Reboot with `$ sudo reboot` and enjoy!
   
