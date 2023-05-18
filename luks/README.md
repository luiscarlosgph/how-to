Description
-----------

This page explains how to use a hard drive that has been encrypted with LUKS.


How to use an encrypted drive
-----------------------------

* Get the UUID of your drive (less prone to problems compared to the legacy `/dev/sdX` device names):

   ```
   $ lsblk --fs
   ```
