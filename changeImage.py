#!/usr/bin/env python3
import os
import sys
from PIL import Image
# current_directory=os.getcwd()
imgpath='supplier-data/images/'
images_in_current_directory=os.listdir(imgpath)
for infile in images_in_current_directory:
    i=os.path.basename(infile)
    print(i)
    f, e = os.path.splitext(infile)
    if e =='.tiff':
        outfile = f + ".jpeg"
        print(outfile)
        img = Image.open(imgpath+i).resize((600,400))
        # img = Image.fromarray(img*255) # (x,y) pixels
        if not img.mode == 'RGB':
             img = img.convert('RGB')
        img.save(imgpath+outfile)
