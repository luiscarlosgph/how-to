Description
-----------

This is a quick guide to setup [Docker](https://www.docker.com) in Ubuntu.


Install a nice Docker environment
---------------------------------

What do I mean by nice? Docker with CUDA support so we can run [PyTorch](https://pytorch.org/get-started/locally) to train deep learning models and [Portainer](https://www.portainer.io) so we can download images and deploy containers quickly with a web [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface).

1. Uninstall old versions:
    ```
    $ sudo apt remove docker docker-engine docker.io containerd runc
    ```
    
2. Install dependencies:
    ```
    $ sudo apt update
    $ sudo apt install -y ca-certificates curl gnupg lsb-release
    ```
3. Add Docker repo to your list of `apt` repositories:
    ```
    $ sudo mkdir -p /etc/apt/keyrings
    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    $ echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ```
    
4. Install Docker:
    ```
    $ sudo apt update
    $ sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
    ```

5. Add repo to install the CUDA support for Docker (i.e. the [nvidia-docker2](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/overview.html) runtime):
    ```
    $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
    $ curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
    $ sudo su
    $ echo "deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://nvidia.github.io/libnvidia-container/stable/ubuntu20.04/amd64 /" >> /etc/apt/sources.list
    ```
<!--
     $ curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
-->

More info on the previous command [here](https://nvidia.github.io/libnvidia-container).

6. Install CUDA support for Docker:
    ```
    $ sudo apt update
    $ sudo apt install -y nvidia-docker2
    ```

7. Restart the Docker daemon so you enjoy the CUDA support:
    ```
    $ sudo systemctl restart docker
    ```
    
8. Add your user to the group `docker` so you can actually use Docker:
    ```
    $ sudo usermod -a -G docker <your_username_here>
    ```
    Now you need to **log out (and log in again) from your Ubuntu session** for this change to take effect (don't worry, if you log out without closing your web browser you will get your million tabs back). Rebooting your PC also works.
    
9. Install Portainer:
    ```
    $ docker volume create portainer_data
    $ docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
    ```

10. Access [https://127.0.0.1:9443](https://127.0.0.1:9443). The first time you do this, you will see this (or similar, depending on the web browser you use):
    
    ![Screenshot from 2022-09-08 01-59-37](https://user-images.githubusercontent.com/3996630/189010590-6a92f7e0-c661-4750-b534-c7bd272e352f.png)
    
    Ignore this message, click the `Advanced...` button, and you will then see this:
    
    ![Screenshot from 2022-09-08 02-01-57](https://user-images.githubusercontent.com/3996630/189010757-8e6c0838-5c84-4359-adb9-746037acd8a3.png)
    
    Click `Accept the Risk and Continue`, you will never see this message again. Portainer will now prompt you for your new username and password (to access Portainer). After you set them up, Docker and Portainer have been installed. 
    
    If you click on the `Containers` button (for example), you should see something like this:
    
    ![Screenshot from 2022-09-08 03-25-29](https://user-images.githubusercontent.com/3996630/189019774-d1d91794-8be2-4aee-b473-6982d8804ee5.png)

    Enjoy!
    
    PS, you do not need to use the same password everywhere, you can use [KeePassX](https://www.keepassx.org) to store all your passwords. You can save the encrypted password file (\*.kdbx) in Dropbox and open it from all your devices, also from your iPhone (Strongbox app) and your Android (Keepass2Android app).


How to change the location of the Docker container data
-------------------------------------------------------

Classic situation where you have a lot of Docker containers and they occupy all the space in your drive. This is how to change the location:

1. Stop Docker daemon: `$ sudo systemctl stop docker && sudo systemctl stop docker.socket && sudo systemctl stop containerd`
2. Create your new Docker data directory: `$ sudo mkdir -p /new_data_dir`
3. Copy your Docker data to the new data directory: `$ rsync -vah --progress /var/lib/docker/ /new_data_dir/`
4. Edit the file `/etc/docker/daemon.json` and add:

   ```
   {
     "data-root": "/new_data_dir/docker"
   }
   ```
5. Reboot or restart Docker daemon with `$ sudo systemctl start docker`
6. Check that Docker works properly with `$ docker info -f '{{ .DockerRootDir}}'`
7. Delete your previous data directory: `$ sudo rm -r /var/lib/docker`


How to run a Docker container of Ubuntu from Mac
------------------------------------------------

You need to install Docker downloading it from [the Docker website](https://docs.docker.com/desktop/install/mac-install/).

1. Download the image of Ubuntu 22.04 LTS:

   ```bash
   $ docker pull ubuntu:jammy
   ```
   
3. Run a Docker container with Ubuntu:

   ```bash
   $ docker run --name dev -v /Users:/home ubuntu:jammy /bin/bash -c "apt update && apt install sudo -y && adduser --uid $(id -u) --gid $(id -g)    --disabled-password --gecos '' --no-create-home $USER && usermod -a -G sudo $USER && echo \"$USER ALL=(ALL) NOPASSWD: ALL\" >> /etc/sudoers && sleep infinity" &
   ```
   
   This command looks like it gets stuck, just press Enter and you will get your terminal back.

2. Get a terminal of the Ubuntu container:

   ```
   $ docker exec -it --user $(id -u):$(id -g) dev /bin/bash
   ```
   Inside the container you have your Mac's home mounted on `/home/<username>` and you should be able to use sudo without issues.
