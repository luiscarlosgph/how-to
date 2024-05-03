Configure a Samba server in Ubuntu/Debian
-----------------------------------------

* In the <strong>server</strong>:
  
  1. Install the Samba server: `$ sudo apt install samba`
     
  2. Edit `/etc/samba/smb.conf` and add:
    
     ```
     [global]
        workgroup = WORKGROUP
        interfaces = <network_interface>
        bind interfaces only = yes
        log file = /var/log/samba/log.%m
        max log size = 10000
        logging = file
        panic action = /usr/share/samba/panic-action %d
        server role = standalone server
        obey pam restrictions = yes
        unix password sync = yes
        passwd program = /usr/bin/passwd %u
        passwd chat = *Enter\snew\s*\spassword:* %n\n *Retype\snew\s*\spassword:* %n\n *password\supdated\ssuccessfully* .
        pam password change = yes
        map to guest = bad user
        usershare max shares = 0
        usershare allow guests = no

     [<your_share_name>]
        comment = <Write something about your share here>
        path = <the_path_you_want_to_share>
        browseable = yes
        read only = no
        create mask = 0700
        directory mask = 0700
        valid users = <your_username_in_the_server>
     ```
    
  3. Add your user to the list of samba users: `$ sudo smbpasswd -a <your_username_in_the_server>`

* In the <strong>client</strong>:
  
  1. Install the Samba client:
     
     ```
     $ sudo apt install cifs-utils
     ```
     
  3. Create a credentials file `/etc/samba-credentials`:
     
     ```
     username=<your_username_in_the_server>
     password=<your_password_in_the_server>
     ```
     
  4. Set the right permissions for the credentials file:

     ```
     $ sudo chown root: /etc/samba-credentials
     $ sudo chmod 600 /etc/samba-credentials
     ```
     
  6. Mount the remote share:
     
     ```
     $ sudo mount -t cifs -o credentials=/etc/samba-credentials,uid=<your_uid>,gid=<your_gid> //<your_server_ip>/<your_share_name> <mount_point>
     ```
     The `uid` and the `gid` should be the ones of your user in the client machine. You can see them running: `$ id`.
     
  8. If you want to mount the share from boot, add this line to your `/etc/fstab`:
     
     ```
     //<your_server_ip>/<your_share_name>  <mount_point>  cifs  credentials=/etc/samba-credentials,uid=<your_uid>,gid=<your_gid>  0  0
     ```
