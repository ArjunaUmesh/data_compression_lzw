# -*- coding: utf-8 -*-
"""
Created on Sat May 28 00:45:45 2022

@author: arjun
"""

import io

def compress_data(data):
    #To compress given data
    
    size=256;
    #create the dictionary to store the 256 characters indexed from 0-255
    dictionary={};
    for c in range(256):
        dictionary[chr(c)]=c;
    
    #print(dictionary)
    
    output=[]
    s=""
    for c in data:
        charset=s+c
        
        #if the current character(s) is in the dictionary then add the next character and check again in the 
        #dictionary for presence of this new set of characters        
        if charset in dictionary:
            s=charset
        #if the current character set isnt in the dictionary then
        #assign the code for the characte set excluding the last char in the result
        else:
            output.append(dictionary[s])
            #and add the whole character set as a new entry in the dictionary 
            dictionary[charset]=size
            size=size+1
            s=c
    
    if s:
        output.append(dictionary[s])

    #additional items added to the dictionary
    
    #for d in range(256,size):
    #    print(d,"\t",dictionary[d])

    return output
    
    
    



