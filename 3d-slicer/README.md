Install
-------

Open your terminal and run:

```
$ wget https://download.slicer.org/bitstream/637f7a7f517443dc5dc7326e -O 3dslicer.tar.gz
$ tar xf 3dslicer.tar.gz
$ mv Slicer-5.2.1-linux-amd64 3dslicer
$ cd 3dslicer
```

Run
---

Open your terminal and navigate to the directory where you have **3D Slicer** installed. If you are following this tutorial, you should be already there, then run:
```
$ ./Slicer
```


Troubleshooting
---------------

* **Problem:** if you try to click on `View` -> `Extensions Manager` and see that the progress bar at a `100%` and the `Extensions Manager` page is empty, 
you most likely will also see this message in your terminal:

   ```
   An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.
   ```
   
   * **Solution**: run **3D Slicer** with `$ QTWEBENGINE_DISABLE_SANDBOX=1 ./Slicer`
