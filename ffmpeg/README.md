* Convert a folder with images into a video:
```
$ ffmpeg -r 1/5 -i %03d.jpg -c:v libx264 -vf "fps=25,format=yuv420p" out.mp4
```
The `%03d.jpg` pattern indicates to ffmpeg that the filenames of the images contain integers of three digits. This is used by ffmpeg to discover the order of the images in the video. Change the pattern according to your filenames, e.g. if your images are `img007.png`, the pattern would be `img%03d.png`.
