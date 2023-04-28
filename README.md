# Python Thumbnail VTT Generator

Simple script to generate thumbnail WebVTT file.

## Usage

### 1. Create directory to store thumbnail images

`mkdir thumbnails`

`cd thumbnails`

### 2. Generate thumbnails using `ffmpeg`:

`ffmpeg -i [video_filepath] -vf "fps=1,scale=178:100" out%d.jpg`

### 3. Generate VTT file with `generate_vtt.py`

`python3 generate_vtt.py [thumbnails_dir] [output_vtt_file.vtt]`

For example:

`python3 generate_vtt.py thumbnails thumbnails/thumbnails.vtt`

### Example Output (thumbnails.vtt):

```
WEBVTT

1
00:00:00.000 --> 00:00:01.000
out1.jpg#xywh=0,0,178,100

2
00:00:01.000 --> 00:00:02.000
out10.jpg#xywh=0,0,178,100

3
00:00:02.000 --> 00:00:03.000
out100.jpg#xywh=0,0,178,100
```


## Features

- Will detect size of thumbnails (default 178x100)
- One thumbnail per second of video




