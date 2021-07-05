# gen_video
Python script to generate an mp4 video from a list of images


## Installation

This guide assumes you already have the following installed:

  *  Python 3
  *  pip (Python package installer)

From the project directory, run:
```
pip install -r requirements.txt
```

pip will install the necessary Python packages (numpy and OpenCV).


## Usage

```
usage: gen_video.py [-h] [-o OUTPUT] [--fps FPS] image_lists [image_lists ...]

Generate mp4 video from image lists

positional arguments:
  image_lists           file(s) containing list of images

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output file (default: output.mp4)
  --fps FPS             frames per sec (default: 5)
```
