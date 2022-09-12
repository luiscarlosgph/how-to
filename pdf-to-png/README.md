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

Troubleshooting
---------------

1. If you see this error:
```
convert-im6.q16: attempt to perform an operation not allowed by the security policy `PDF' @ error/constitute.c/IsCoderAuthorized/408.
```

You can solve it with: `sudo sed -i '/disable ghostscript format types/,+6d' /etc/ImageMagick-6/policy.xml`
