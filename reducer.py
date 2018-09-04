#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 15:46:12 2018

@author: root
"""

import sys
import re

pos = 0
neg = 0

data0 = ""
data1 = ""

for val in sys.stdin:
    val = val.strip()
    try:
        emotion,count=val.split(" ")
    except:
        emotion = ""
    if emotion=="Positive" :
        pos += int(count)
    elif emotion=="Negative" :
        neg += int(count)
    else:
        
        if(val.startswith("0neg")):
            data0+=val+"\n"
        if(val.startswith("1pos")):
            data1+=val+"\n"
print("Positive",pos)
print("Negative",neg)

data1 = data1.replace("1pos","")
data0 = data0.replace("0neg","")

data0 = re.sub(r"[0-9]",",",data0)
data1 = re.sub(r"[0-9]",",",data1)

data0 = re.sub(r'\['," ",data0)
data1 = re.sub(r'\['," ",data1)

data0 = re.sub(r'\]'," ",data0)
data1 = re.sub(r'\]'," ",data1)

data0 = re.sub(r'\s+'," ",data0)
data1 = re.sub(r'\s+'," ",data1)

print("Positive emotions:")
print(data1)

print("Negative emotions:")
print(data0)


