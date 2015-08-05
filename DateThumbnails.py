import os
from glob import glob
import argparse

import exifread
import PIL
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser(description='Make a single jpg image with thumbnails and date information for all files in directory')
parser.add_argument('size', type=int, nargs=2, default='3 5', metavar="N",
                    help='x, y size of grid of thumbnails')
parser.add_argument('--outfile', nargs='?', type=str,
                     default='thumb.jpg', help='filename of output file')
args = parser.parse_args()

try:
    os.remove('args.outfile')
except OSError:
    pass

filelist = glob('*')
n_pictures = len(filelist)

if n_pictures > (args.size[0] * args.size[1]):
    raise Exception("{0} images don't fit on a {1} grid.".format(n_pictures, args.size))

fig = plt.figure(figsize=(6,8))
for i,f in enumerate(filelist):
    with open(f, 'rb') as imf:
        tags = exifread.process_file(imf)
        date = tags['EXIF DateTimeOriginal'].values
        im = PIL.Image.open(imf)
        im.thumbnail((128, 128))
        im = np.array(im)
        ax = fig.add_subplot(args.size[0], args.size[1], i+1)
        ax.imshow(im)
        ax.set_frame_on(False)
        ax.axes.get_yaxis().set_visible(False)
        ax.axes.get_xaxis().set_visible(False)
        ax.set_title(date.split()[0])

fig.savefig(args.outfile)
