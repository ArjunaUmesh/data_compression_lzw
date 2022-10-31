# -*- coding: utf-8 -*-
"""
Created on Sat May 28 01:18:38 2022

@author: arjun
"""

import io

def decompress_data(data):
    #To decompress the given data
    
    
    size=256;
    #create the dictionary to store the 256 characters indexed from 0-255
    dictionary={};
    for c in range(256):
        dictionary[c]=chr(c);
    
    #print(dictionary)
    
    result=""
    w=""
    w+=chr(data[0])
    result+=w
    data=data[1:]
    for c in data:
        if c in dictionary:
            s=dictionary[c]
            
        else:
            s=w+w[0]
            
        result+=s
        
        
        dictionary[size]=w+s[0]
        size=size+1
        w=s

    return(result)
    
    
value=[65, 32, 108, 111, 115, 115, 32, 111, 102, 32, 104, 97, 98, 105, 116, 97, 116, 32, 99, 97, 110, 265, 97, 112, 112, 101, 276, 110, 271, 117, 114, 97, 108, 108, 121]
decompress_data(value)


        
        
        