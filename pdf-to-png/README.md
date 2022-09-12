Install dependencies
--------------------

```
$ sudo apt update
$ sudo apt install imagemagick
```

Convert PDF to high resolution PNG image
----------------------------------------

```
$ convert -density 300 <pdf_path> -flatten <png_path>
```
