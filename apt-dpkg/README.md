How to edit a .deb file to remove a dependency
----------------------------------------------

```bash
$ mkdir tmp
$ dpkg-deb -R original.deb tmp
# edit DEBIAN/control
$ dpkg-deb -b tmp fixed.deb
```
