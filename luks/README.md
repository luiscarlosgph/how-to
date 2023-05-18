Description
-----------

This page explains how to use a hard drive that has been encrypted with LUKS.


How to create an encrypted drive
--------------------------------

* Install parted: `sudo apt install parted`
* Run parted and create a GPT partition table and a primary partition (**do not do this on a drive that has contains data, you will lose it**): 
   ```
   select /dev/sdX  # Replace `/dev/sdX` with your drive path, e.g. `/dev/sde`
   mklabel gpt
   mkpart primary ext4 0% 100%
   quit
   ```
* Encrypt the partition with LUKS (replace `/dev/sdX1` with your partition path, e.g. `/dev/sde1`): 
   ```bash
   $ cryptsetup luksFormat --type luks2 /dev/sdX1
   ```
   
* Find the UUID of your `/dev/sdX1` partition: 
   ```bash
   $ lsblk --fs
   ```

* Format the encrypted partition with `ext4`:
   ```bash
   $ cryptsetup luksOpen /dev/disk/by-uuid/<WRITE_THE_UUID_HERE> <WRITE_WHATEVER_PARITION_NAME_YOU_FANCY_HERE>
   $ mkfs.ext4 -L <WRITE_WHATEVER_PARITION_NAME_YOU_FANCY_HERE> /dev/mapper/<WRITE_WHATEVER_PARITION_NAME_YOU_FANCY_HERE>
   $ cryptsetup luksClose <WRITE_WHATEVER_PARITION_NAME_YOU_FANCY_HERE>
   ```

How to use an encrypted drive
-----------------------------

Let's assume that you have a drive with a single primary partition (encrypted with LUKS) that occupies the whole drive.

* Bash code snippet to **mount** the encrypted partition:

   ```bash
   #!/bin/bash

   HDD_UUID="<WRITE_HERE_YOUR_PARTITION_UUID>"  # You can find this out with `lsblk --fs`
   HDD_NAME="<WRITE_HERE_THE_LABEL_OF_YOUR_PARTITION>"  # You can choose any name
   MOUNT_POINT="/mnt/$HDD_NAME"

   # Check that the disk is not already decrypted
   echo -e "\n[INFO] Checking that the disk is not already decrypted"
   decrypted=`ls /dev/mapper | grep $HDD_NAME`
   if [ ! -z "${decrypted}" ]; then
     echo -e "[ERROR] It seems that the hard drive has been already decrypted."
     exit 1
   fi

   # Decrypt HDD
   echo -e "\n[INFO] Decrypting disk with LUKS"
   cryptsetup luksOpen /dev/disk/by-uuid/$HDD_UUID $HDD_NAME

   # Check that nothing else is mounted on the mountpoint
   mounted=`mount | grep "$MOUNT_POINT"`
   if [ ! -z "${mounted}" ]; then
     echo -e "[ERROR] It seems that the partition in the encrypted drive is already mounted."
     exit 1
   fi

   # Create /mnt/backup if it does not exist
   if [ ! -d "$MOUNT_POINT" ]; then
     echo -e "[INFO] Creating mountpoint directory $MOUNT_POINT because it does not exist."
     mkdir -p $MOUNT_POINT
   fi

   # Mount encrypted partition
   echo -e "\n[INFO] Mounting encrypted partition."
   mount /dev/mapper/$HDD_NAME $MOUNT_POINT
   ```

* Bash code snippet to **unmount** an encrypted device:

   ```bash
   #!/bin/bash

   HDD_NAME="<WRITE_HERE_THE_LABEL_OF_YOUR_PARTITION>"
   MOUNT_POINT="/mnt/$HDD_NAME"

   # Umount the encrypted partition
   echo -e "\n[INFO] Unmounting encrypted partition."
   umount $MOUNT_POINT

   # Close the partition
   echo -e "\n[INFO] Closing partition with LUKS."
   cryptsetup luksClose $HDD_NAME
   ```
