# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 14:22:28 2022

@author: 20pt04
"""

import socket
from os.path import exists,getsize 
import datacompression1
import datadecompression
from PIL import Image
import math

def compress_Image(img):
    #img=input('Provide image for compression : ')
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
    compressed.append(le)
    compressed.append(br)
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
    return compressed



def decompress_Image(compressed):
    
    
    le=compressed[-2]
    br=compressed[-1]
    compressed=compressed[0:-2]
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


serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=9999

serverSocket.bind((host,port))

serverSocket.listen(5)

print('Waiting for connections')

while True : 
    
    clientSocket,clientIP=serverSocket.accept()
    print('Got a connection from ',clientIP)
    print('Waiting for operation from client : ')
    #r1
    operation=clientSocket.recv(1024).decode()
    
    if(operation=='COMPRESS'):
        #r2
        filename=clientSocket.recv(1024).decode()
        print(filename)
        if(exists(filename)):
            #print('')
            size=getsize(filename)
            #s1
            clientSocket.send(bytes(str(size),'utf-8'))
            L=compress_Image(filename)
            # open file in write mode
            with open('textc.txt', 'w') as fp:
                for item in L:
                    # write each item on a new line
                    fp.write("%s\n" % item)
            #s2
            clientSocket.send(bytes('textc.txt','utf-8'))
            clientSocket.send(bytes('com.jpeg','utf-8'))
            
        else:
            clientSocket.send(bytes(-1))                                   
    else:
        #r2
        filename=clientSocket.recv(1024).decode()
        print(filename)
        if(exists(filename)):
            #print('')
            size=getsize(filename)
            #s1
            clientSocket.send(bytes(str(size),'utf-8'))
            L = []

            # open file and read the content in a list
            with open(filename, 'r') as fp:
                for line in fp:
                    # remove linebreak from a current name
                    # linebreak is the last character of each line
                    x = line[:-1]
            
                    # add current item to the list
                    L.append(int(x))
            decompress_Image(L)
            
    clientSocket.close()
    break;
    
    
        
    