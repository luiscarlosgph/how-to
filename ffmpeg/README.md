#### Convert a folder with images into a video:

```bash
$ ffmpeg -r 25 -pattern_type glob -i '*.png' -c:v libx264 -vf "fps=25,format=yuv420p" out.mp4
```

Options:

  * `-r`: indicates how many images should be taken for each second of the video. For example, if you have 50 images and `-r 25`, the resulting video will have a duration of 2s.


#### Convert a video into a folder of images

```bash
$ ffmpeg -i video.mp4 -r 25 -f image2 -qscale:v 2 output_folder/%05d.png
```

#### Convert RTSP live stream to HLS:

```bash
$ ffmpeg -fflags nobuffer -rtsp_transport tcp -i <rtsp_url> -vsync 0 -copyts -vcodec copy -movflags frag_keyframe+empty_moov -an -hls_flags delete_segments+append_list -f segment -segment_list_flags live -segment_time 0.5 -segment_list_size 1 -segment_format mpegts -segment_list <output_directory>/index.m3u8 -segment_list_type m3u8 -segment_list_entry_prefix <output_directory>/ <output_directory>/%3d.ts
```

To display this video in a browoser, you need to include:

```html
<video id="video-player" controls preload="none">
    <source src="/output-directory/index.m3u8" type="application/x-mpegURL">
</video>
```
