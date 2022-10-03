Install dependencies
--------------------

```bash
$ sudo apt install ddrescue
```

Recover data
------------

1. Create image of the hard drive:

```bash
$ sudo ddrescue 
```

For example:
```bash
$ ddrescue -d -r 3 /dev/sdb failing_hd.img recovery.log
```

2. Recover files: for this purpose we are going to use [TestDisk](https://www.cgsecurity.org/wiki/TestDisk) and [PhotoRec](https://www.cgsecurity.org/wiki/PhotoRec).

TODO
