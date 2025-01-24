Config file (daemon.json)
-----------

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
