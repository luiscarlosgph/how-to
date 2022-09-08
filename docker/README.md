Description
-----------

Guide to setup [Docker](https://www.docker.com) in Ubuntu. The official install guide is [here](https://docs.docker.com/engine/install/ubuntu/).


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
    $ curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
    ```

6. Install CUDA support for Docker:
    ```
    $ sudo apt update
    $ sudo apt install -y nvidia-docker2
    ```

7. Restart the Docker daemon so you enjoy the CUDA support:
    ```
    $ sudo systemctl restart docker
    ```
    
8. Add your user to the group `docker` so you can actually use Docker (e.g. for the user **john**):
    ```
    $ sudo usermod -a -G docker john
    ```
    Now you need to **log out (and log in again) from your Ubuntu session** for this change to take effect (don't worry, if you log out without closing your web browser you will get your million tabs back).
    
9. Install Portainer:
    ```
    $ docker volume create portainer_data
    $ docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:2.9.3
    ```

10. Access [https://127.0.0.1:9443](https://127.0.0.1:9443) and enjoy your graphical Docker. The first time you do this, you will see this (or similar, depending on the web browser you use):
    
    ![Screenshot from 2022-09-08 01-59-37](https://user-images.githubusercontent.com/3996630/189010590-6a92f7e0-c661-4750-b534-c7bd272e352f.png)
    
    Ignore this message, click the **Advanced...** button, and you will then see this:
    
    ![Screenshot from 2022-09-08 02-01-57](https://user-images.githubusercontent.com/3996630/189010757-8e6c0838-5c84-4359-adb9-746037acd8a3.png)

