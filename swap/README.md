Show currently enabled swaps
-----------------------------
```bash
$ sudo swapon --show
```

Remove existing swapfile
------------------------
1. Disable current swapfile: ```sudo swapoff -v /swapfile```.
2. Comment out the existing swap file entry from the ```/etc/fstab``` file.
3. Remove the actual swapfile: ```sudo rm /swapfile```.

Create new swapfile
-------------------
1. Create swapfile: ```sudo fallocate -l 32G /swapfile```.
2. Set the file permissions to 600 to prevent regular users to write and read the file: ```sudo chmod 600 /swapfile```.
3. Create a Linux swap area on the file: ```sudo mkswap /swapfile```.
4. Activate the swap file: ```sudo swapon /swapfile```.
5. Make swap permanent adding the line ```/swapfile none swap sw 0 0``` to ```/etc/fstab```.

Swappiness
-----------
**Attention here**! Swappiness is a Linux kernel property that defines how often the system will use the swap space. It can have a value between 0 and 100 (the default on Ubuntu is 60). A low value will make the kernel to try to avoid swapping whenever possible, while a higher value will make the kernel to use the swap space more aggressively.

To make this parameter persistent across reboots, append the following line to the ```/etc/sysctl.conf``` file:
```
vm.swappiness=10
```
