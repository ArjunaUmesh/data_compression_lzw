# -*- coding: utf-8 -*-
"""
Created on Sat May 28 15:06:47 2022

@author: arjun
"""

import datacompression1
import datadecompression
from PIL import Image
import math

img=input('Provide image for compression : ')
image=Image.open(img)
pixels=list(image.getdata())
#print(pixels)
image.show()

le,br=image.size

pixelstr=""
for i in pixels:
    for j in i:
        pixelstr+=str(j).zfill(3)

#print(pixelstr)
compressed=datacompression1.compress_data(pixelstr)
#print(compressed)

text=""
for i in compressed:
    text+=str(i)

f=open("adidas.txt",'w')
f.write(text)


pixels2=[]
l=len(text)
i=0
for j in range(int(l/3)):
    pixels2.append(int(text[i:i+3]))
    i+=3

l=len(pixels2)
l1=[0,0,0]
i=0
pixels3=[]
for j in range(int(l/3)):
    l1[0]=pixels2[i]
    l1[1]=pixels2[i+1]
    l1[2]=pixels2[i+2]
    i=i+3
    pixels3.append(tuple(l1))
#print(pixels3)

l=len(pixels3)
l=math.sqrt(l)
l=math.ceil(l)

img2=Image.new('RGB',(l,l),"pink")
img2.show()
img2.putdata(pixels3)
img2.show()
img2.save("com.jpeg")


#image1=Image.open('33.png')
#le,br=image1.size

image=Image.open('com.jpeg')
pixels=list(image.getdata())
#print(pixels)
#image.show()
pixelstr=""
for i in pixels:
    for j in i:
        pixelstr+=str(j).zfill(3)
#print(compressed)
#print(pixelstr)
#decompressed=datacompression1.compress_data(pixelstr)

decompressed=datadecompression.decompress_data(compressed)
#print(decompressed)


pixels2=[]
l=len(decompressed)
i=0
for j in range(int(l/3)):
    pixels2.append(int(decompressed[i:i+3]))
    i+=3

l=len(pixels2)
l1=[0,0,0]
i=0
pixels3=[]
for j in range(int(l/3)):
    l1[0]=pixels2[i]
    l1[1]=pixels2[i+1]
    l1[2]=pixels2[i+2]
    i=i+3
    pixels3.append(tuple(l1))
#print(pixels3)


img2=Image.new('RGB',(le,br),"pink")
img2.show()
img2.putdata(pixels3)
img2.show()
