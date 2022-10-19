Install dependencies
--------------------

```bash
$ sudo apt install gddrescue testdisk
```

Create image of the hard drive
------------------------------

Connect your failing drive and find its path using `sudo dmesg | grep -P 'hd|sd'` right after you have plugged it in, you should see a name like `/dev/sda`, `/dev/sdb`, `/dev/sdc`...

   ```bash
   $ sudo ddrescue 
   ```

   For example:
   ```bash
   $ ddrescue -d -r 3 /dev/sdb failing_hd.img image_recovery.log
   ```

Mount image of the hard drive
-----------------------------

```bash
$ sudo apt install -y multipath-tools
$ sudo kpartx -a failing_hd.img
$ sudo mount -o loop /dev/mapper/loop0p2 /mnt/p2
```

Recover files
-------------
   For this purpose we are going to use [TestDisk](https://www.cgsecurity.org/wiki/TestDisk) and [PhotoRec](https://www.cgsecurity.org/wiki/PhotoRec). Let's start with PhotoRec.
   
   ```
   $ sudo photorec <drive_or_image>
   ```
   For example:
   ```
   $ sudo photorec failing_hd.img
   ```
