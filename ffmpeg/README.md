* Convert a folder with images into a video:
```
$ ffmpeg -r 1/5 -i %03d.jpg -c:v libx264 -vf "fps=25,format=yuv420p" out.mp4
```
