Install dependencies
--------------------
```bash
$ sudo apt install wget ghostscript exiftool
```

Download the code
-----------------
```bash
$ wget https://raw.githubusercontent.com/luiscarlosgph/how-to/main/compress-pdf/compresspdf.sh
$ chmod +x compresspdf.sh
```

Compress PDF
------------
```bash
$ ./compresspdf.sh whatever.pdf
```
The resulting file will have a `-compressed.pdf` suffix, i.e. `whatever-compressed.pdf` following the example above.
