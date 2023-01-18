Description
-----------

Configure a Debian/Ubuntu system to mount an sshfs resource from boot.


Install
-------
```
$ sudo apt install autofs sshfs autossh
```

Configure
---------

1. Create folder where all the mounted resources will be: `$ mkdir ~/mounts`

2. Run `$ id` to get your local user and group id. 

3. Edit **autofs** configuration file with `$ sudo vim /etc/auto.master` and append the following line at the end of the file:

   ```
   /home/<local_username_here>/mounts /etc/autofs.sshfs uid=<local_user_id_here>,gid=<local_group_id_here>,--timeout=60,--ghost
   ```

4. For each remote resource that you want to mount, edit `$ sudo vim /etc/autofs.sshfs` and add a line like this one below:

   ```
   <resource_name> -fstype=fuse,rw,allow_other :sshfs\#<remote_username>@<remote_host>\:<remote_directory>
   ```

   **autofs** will create a folder named as specified in `<resource_name>` above and mount the remote directory there from boot.
