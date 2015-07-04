'''Make a jpg images with thumbnails and date information for all files in directory

To-Do: Currently it will always make 5 * 3 thumbnails - need to calc this number
       use argparse
       add docs
       add setup.py
'''

import os
from glob import glob

import exifread
import PIL
import matplotlib.pyplot as plt

try:
    os.remove('thumb.jpg')
except OSError:
    pass

filelist = glob('*')
n_pictures = len(filelist)

fig = plt.figure(figsize=(6,8))
for i,f in enumerate(filelist):
    with open(f, 'rb') as imf:
        tags = exifread.process_file(imf)
        date = tags['EXIF DateTimeOriginal'].values
        im = PIL.Image.open(imf)
        im.thumbnail((128, 128))
        im = np.array(im)
        ax = fig.add_subplot(5,3,i+1)
        ax.imshow(im)
        ax.set_frame_on(False)
        ax.axes.get_yaxis().set_visible(False)
        ax.axes.get_xaxis().set_visible(False)
        ax.set_title(date.split()[0])

fig.savefig('thumb.jpg')
