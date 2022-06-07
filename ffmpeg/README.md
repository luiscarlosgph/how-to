* Convert a folder with images into a video:
```
$ ffmpeg -r 25 -pattern_type glob -i '*.png' -c:v libx264 -vf "fps=25,format=yuv420p" out.mp4
```
Options:

`-r`: indicates how many images should be taken for each second of the video, e.g. if you have 50 images the resulting video will have a duration 2s.
