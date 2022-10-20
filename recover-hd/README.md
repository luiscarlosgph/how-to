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
   $ sudo ddrescue -d -r 3 /dev/sdb failing_hd.img image_recovery.log
   ```

Mount/unmount image of the hard drive
-----------------------------
<!--
$ sudo apt install -y multipath-tools
$ sudo kpartx -a -r failing_hd.img
$ sudo mount -o loop /dev/mapper/loop0p2 /mnt/p2
-->

```bash
# Mount disk image
$ sudo losetup /dev/loop10 failing_hd.img
$ sudo kpartx -as /dev/loop10

# Run fdisk to check all the partitions of the disk
$ sudo fdisk -l

# Mount the partition number 2 of the disk
$ sudo losetup /dev/loop11 /dev/mapper/loop10p2
$ sudo mkdir /mnt/recovered_partition
$ sudo mount /dev/loop11 /mnt/recovered_partition
```

Unmount:
```bash
$ umount disk
$ losetup -d /dev/loop1
$ kpartx -ds /dev/loop0
$ losetup -d /dev/loop0
$ rmdir disk
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
