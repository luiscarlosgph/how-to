How to edit a .deb file to remove a dependency
----------------------------------------------

```bash
$ mkdir tmp
$ dpkg-deb -R original.deb tmp
$ vim tmp/DEBIAN/control  # Change the list of dependencies here
$ dpkg-deb -b tmp fixed.deb
```

Install a package from a .deb file
----------------------------------

```bash
$ sudo dpkg -i package.deb
```

Reconfigure a package
---------------------

```bash
$ sudo dpkg-reconfigure <package_name>
```
