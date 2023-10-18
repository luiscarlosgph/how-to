Description
-----------

This guide explains how to run a virtual screen in a headless server and access it remotely via SSH.


Run virtual screen in remote server
-----------------------------------

> **_NOTE:_**  These commands should be executed in your remote server via SSH.

1. Install dependencies:

   ```bash
   $ sudo apt install x11vnc xvfb
   ```

2. Run virtual screen with `Xvfb`:

   ```bash
   $ Xvfb :22 -screen 0 1920x1080x24 -ac +extension GLX +render +iglx -noreset &
   $ disown
   ```

3. Launch VNC server:

   ```bash
   $ x11vnc -display :22 -rfbport 5900
   ```


Run a graphical program in your remote screen
---------------------------------------------

> **_NOTE:_**  These commands should be executed in your remote server via SSH.

As an example, we will run `xclock`, a GUI that displays a clock. This program comes within the `x11-apps` package, so we install it first.
Then, to run a program with GUI in the virtual screen, we must set the `DISPLAY` environment variable pointing to the display number chosen for the virtual screen (which is `:22` in our case, see `Xvfb` command above).

   ```bash
   $ sudo apt install x11-apps
   $ export DISPLAY=:22
   $ xclock
   ```
   
Access remote screen from local computer
----------------------------------------

> **_NOTE:_**  These commands should be executed in your local computer.

1. Create an SSH tunnel to the server:

   ```bash
   $ ssh -L ssh -L 50900:127.0.0.1:5900 <remote_server_hostname>
   ```
   
2. Open your favourite VNC client and connect to `127.0.0.1:5900`, you should see the screen 

