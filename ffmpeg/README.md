* Convert a folder with images into a video:
```
$ ffmpeg -r 25 -pattern_type glob -i '*.png' -c:v libx264 -vf "fps=25,format=yuv420p" out.mp4
```
Options:

`-r`: indicates how many images should be taken for each second of the video. For example, if you have 50 images and `-r 25`, the resulting video will have a duration of 2s.
