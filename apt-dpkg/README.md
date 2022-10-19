How to edit a .deb file to remove a dependency
----------------------------------------------

```bash
$ mkdir tmp
$ dpkg-deb -R original.deb tmp
$ vim tmp/DEBIAN/control  # Change the list of dependencies here
$ dpkg-deb -b tmp fixed.deb
```
