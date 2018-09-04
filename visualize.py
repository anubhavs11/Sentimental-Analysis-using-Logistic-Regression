#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 20:33:38 2018

@author: root
"""

import pandas as pd

f = open("output/part-00000","r")
file = f.read()

index = file.find("Positive emotions:")

file = file[:index]

file = file.strip()
files = file.split("\n")

dict={}
for i in range(len(files)):
    files[i] = files[i].strip()
    values = files[i].split()
    dict[values[0]] = int(values[1])

ser = pd.Series(dict)

ser.plot(kind="barh",title = "Sentiment Analysis")
