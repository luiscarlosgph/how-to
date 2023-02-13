This guide illustrates how to create a service that runs at boot.

`$ sudo vim /etc/systemd/system/<name_of_your_service_here>.service`:

```
[Unit]
Description=Whatever service
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=<your_username>
ExecStart=<your_command>

[Install]
WantedBy=multi-user.target
```

**NOTE**: change the `User=` and the `ExecStart=` to the user and command you want to run. 

* Enable the service at boot: `$ sudo systemctl enable <name_of_your_service_here>`.
* Start the service: `$ sudo systemctl start <name_of_your_service_here>`
* Stop the service: `$ sudo systemctl stop <name_of_your_service_here>`
