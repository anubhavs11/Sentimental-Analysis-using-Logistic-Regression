#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 19:01:02 2018

@author: root
"""
import re
import time # to get the current timestamp

f = open("output/part-00000","r")
file = f.read()
pos_position = file.find("Positive emotions:")
neg_position = file.find("Negative emotions:")

positive_text = file[(pos_position+len("Positive emotions:")):neg_position]
negative_text = file[(neg_position+len("Negative emotions:")):]

positive_text = re.sub(r"\s+"," ",positive_text)
negative_text = re.sub(r"\s+"," ",negative_text)


positive_text = re.sub(r"^\s+","",positive_text)
negative_text = re.sub(r"^\s+","",negative_text)

positive_text = re.sub(r"$\s+","",positive_text)
negative_text = re.sub(r"$\s+","",negative_text)

filename = str(int(time.time()))

f = open("txt_sentoken/pos/"+filename+".txt","w")
f.write(positive_text)
f.close()

f = open("txt_sentoken/neg/"+filename+".txt","w")
f.write(negative_text)
f.close()