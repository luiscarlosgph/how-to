* Convert a folder with images into a video:
```
$ ffmpeg -r 1/5 -pattern_type glob -i '*.png' -c:v libx264 -vf "fps=25,format=yuv420p" out.mp4
```
