# Video to ASCII Art

This Python script extracts each frame from a video, converts it to ASCII art, and saves each frame as a `.txt` file.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- Pillow (`PIL`)
- Numpy (`numpy`)

## Installation

```
pdm install
```

## Usage

```
pdm run python video_to_ascii.py path/to/video.mp4 --output_dir ascii_frames --width 100
```

- `path/to/video.mp4`: Path to your video file
- `--output_dir`: Directory to save ASCII art frames (default: `ascii_frames`)
- `--width`: Width of ASCII art (default: 100)
