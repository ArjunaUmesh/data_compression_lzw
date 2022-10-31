# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 14:28:28 2022

@author: 20pt04
"""

import socket
from PIL import Image

clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9999


clientSocket.connect((host,port))

operation=input('Enter the operation : COMPRESS,DECOMPRESS\n')

#s1
clientSocket.send(bytes(operation,'utf-8'))


if(operation=='COMPRESS'):

    filename=input('Enter the filename\n')
    #s2
    clientSocket.send(bytes(filename,'utf-8'))
    #r1
    size=clientSocket.recv(1024).decode()
    print(size)
    #r2
    file=clientSocket.recv(1024).decode()
    print(file)
    img=clientSocket.recv(1024).decode()
    print(img)
    clientSocket.close()
else :
    
    filename=input('Enter the filename')
    #s2
    clientSocket.send(bytes(filename,'utf-8'))
    #r1
    size=clientSocket.recv(1024).decode()
    print(size)