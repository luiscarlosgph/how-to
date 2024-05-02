Configure a Samba server in Ubuntu/Debian
-----------------------------------------

Edit `/etc/samba/smb.conf` and add:

```
[<share_name>]
    path = <share_path>
    read only = no
    browsable = yes
```
