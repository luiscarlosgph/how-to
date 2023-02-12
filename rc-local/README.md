1. Create a SystemD service `$ sudo vim /etc/systemd/system/rc-local.service`:
```
[Unit]
 Description=/etc/rc.local Compatibility
 ConditionPathExists=/etc/rc.local

[Service]
 Type=forking
 ExecStart=/etc/rc.local start
 TimeoutSec=0
 StandardOutput=tty
 RemainAfterExit=yes
 SysVStartPriority=99

[Install]
 WantedBy=multi-user.target
```

2. Create the `rc.local` file with `$ sudo vim /etc/rc.local`:
```
#!/bin/bash

# Run your commands here
```

3. Give execution permissions: `$ sudo chmod +x /etc/rc.local`

4. Enable the service on boot: `$ sudo systemctl enable rc-local`
