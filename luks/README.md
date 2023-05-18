Description
-----------

This page explains how to use a hard drive that has been encrypted with LUKS.


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

   HDD_NAME="backup"
   MOUNT_POINT="/mnt/$HDD_NAME"

   # Umount the encrypted partition
   echo -e "\n[INFO] Unmounting encrypted partition."
   umount $MOUNT_POINT

   # Close the partition
   echo -e "\n[INFO] Closing partition with LUKS."
   cryptsetup luksClose $HDD_NAME
   ```
