Install
-------


1. Create a user called `non-root-docker` to run the Docker daemon. 

2. Follow the official guide [here](https://docs.docker.com/engine/security/rootless)



Config file (daemon.json)
-------------------------

Edit `/home/non-root-docker/.config/docker/daemon.json`:

```
{
        "data-root": "<CUSTOM_DATA_ROOT_HERE>",
        "exec-opts": ["native.cgroupdriver=cgroupfs"]
}
```


SystemD service to run the rootless Docker
------------------------------------------

Edit `/etc/systemd/system/non-root-docker.service`:

```
[Unit]
Description=Docker daemon (non-root)
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
User=non-root-docker
Environment="XDG_RUNTIME_DIR=/home/non-root-docker/.docker/run"
ExecStartPre=/bin/rm -rf /home/non-root-docker/.docker/run/*
ExecStart=/usr/bin/dockerd-rootless.sh
ExecStartPost=/bin/bash -c "sleep 30 && chmod ugo+rw /home/non-root-docker/.docker/run/docker.sock"

[Install]
WantedBy=multi-user.target
```

User config
-----------

Append `export DOCKER_HOST=unix:///home/non-root-docker/.docker/run/docker.sock` to the `~/.bashrc` or `~/.zshrc` file of any user that wants to use Docker. 
