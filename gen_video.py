#!/usr/bin/env python3

import argparse
import cv2
import numpy as np

_output = None  # Video writer

def getVideoWriter(filename, fps, size):
    # This factory method uses size of first image to instantiate the video
    # writer
    global _output
    if _output:
        return _output

    _output = cv2.VideoWriter(filename,
            cv2.VideoWriter_fourcc(*'mp4v'),
            fps,
            size,
            )

    return _output

def release():
    # Cleanup video writer
    global _output
    if _output:
        _output.release()

    _output = None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate mp4 video from image lists')

    parser.add_argument('image_lists', type=str, nargs='+',
            help='file(s) containing list of images')

    parser.add_argument('-o', '--output', type=str, default='output.mp4',
            help='output file (default: %(default)s)')

    parser.add_argument('--fps', type=int, default=5,
            help='frames per sec (default: %(default)s)')

    args = parser.parse_args()
    print(args)

    for img_list in args.image_lists:
        with open(img_list, 'r') as f:
            for line in f:
                img_name = line.strip()

                # Read image
                img = cv2.imread(img_name)
                height, width, layers = img.shape
                size = (width, height)

                # Write image to video
                vw = getVideoWriter(args.output, args.fps, size)
                vw.write(img)

    release()
