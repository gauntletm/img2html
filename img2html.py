#!/usr/bin/env python
 
# img to html v0.2
# will convert a non-svg image to html
#
# Gauntlet O. Manatee
# spukspital@openmailbox.org
 
import os, sys
import Image
 
 
imgname = raw_input("Enter the path to the .png file you want to convert.\n(I recommend .png, though it is not mandatory.\n \
Other image files work, too. However, my best results have been .png pics in the RGB color space.)\n")
 
image = Image.open(imgname)
 
pix = image.load()
width, height = image.size
wbody = width*10
 
# creating the output file
outfile = open("i2h-out.html",'a+')
outfile.write(str('<!DOCTYPE html>\n \
<html>\n \
<head>\n \
<title>img2html</title>\n \
<style>.square {display: block; width: 10px; height: 10px; float: left;}\n \
       .clear {clear: both;}\n \
       p {margin-top: 0; margin-bottom: 0; padding-top: 0; padding-bottom: 0;}\n \
       div {width: ' + str(wbody) + 'px;} \n \
</style>\n \
</head>\n \
<body>\n \
<div><p>\n'))
 
# pixel coordinates
x = 0
y = 0
 
 
while y < height:
  while x < width:
    r, g, b = pix[x,y]
    outfile.write(str('<span class="square" style="background-color: rgb(' + str(r) + str(',') + str(g) + str(',') + str(b) + ')">&nbsp;</span>\n'))
    x = x+1
  outfile.write(str('</p>\n'))
  outfile.write(str('<p class="clear">\n\n'))
  y = y+1
  x = 0
 
# writing the rest of the html document and closing the file
outfile.write(str('</p></div>\n \
</body>\n \
</html>'))
outfile.close()
print("Done.")
quit()
