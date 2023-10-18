Description
-----------

This guide explains how to run a virtual screen in a headless server and access it remotely via SSH.


Install dependencies
--------------------

```bash
$ sudo apt install x11vnc xvfb
```

Run virtual screen
------------------

1. Run virtual screen with `xvfb`:

   ```bash
   $ Xvfb :22 -screen 0 1920x1080x24 -ac +extension GLX +render +iglx -noreset
   ```

2. Launch VNC server:

   ```bash
   $ x11vnc -display :22
   ```
