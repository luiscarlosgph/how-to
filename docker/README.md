Description
-----------

Guide to setup [Docker](https://www.docker.com) in Ubuntu. The official install guide is [here](https://docs.docker.com/engine/install/ubuntu/).


Install a nice Docker environment
---------------------------------

What do I mean by nice? Docker with CUDA support so we can run [PyTorch](https://pytorch.org/get-started/locally) to train deep learning models and [Portainer](https://www.portainer.io) so we can download images and deploy containers quickly.

1. Uninstall old versions:
    ```$ sudo apt remove docker docker-engine docker.io containerd runc```
    
2. Install dependencies:
    ```
    $ sudo apt update
    $ sudo apt-get install ca-certificates curl gnupg lsb-release
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
    $ sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin
    ```
