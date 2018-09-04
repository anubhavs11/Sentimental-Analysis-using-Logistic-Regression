#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 17:34:57 2018

@author: root
"""
import re
import pickle
import sys
import nltk

dataset = sys.stdin
tweets = ""
for data in dataset:
    tweets+=str(data)

list_tweets = nltk.sent_tokenize(tweets)

### WORKING ON TWITTER DATA FOR SENTIMENTAL ANALYSIS
        
with open("preserved files/classifier.pickle","rb") as f:
    clf = pickle.load(f)
    
with open("preserved files/TfidfModel.pickle","rb") as f:
    tfidf = pickle.load(f)

# PREPROCESSING THE DATASET
total_pos = 0
total_neg = 0
data0 = ""
data1 = ""

for tweet in list_tweets:
    tweet = re.sub(r"^https://t.co/[A-Za-z0-9]*\s"," ",tweet)
    tweet = re.sub(r"\s+https://t.co/[A-Za-z0-9]*\s"," ",tweet)
    tweet = re.sub(r"\s+https://t.co/[A-Za-z0-9]*$"," ",tweet)
    tweet = tweet.lower()
    
    tweet = re.sub(r"that's","that is",tweet)
    tweet = re.sub(r"there's","there is",tweet)
    tweet = re.sub(r"what's","what is",tweet)
    tweet = re.sub(r"where's","where is",tweet)
    tweet = re.sub(r"it's","it is",tweet)
    tweet = re.sub(r"who's","who is",tweet)
    tweet = re.sub(r"i'm","i am",tweet)
    tweet = re.sub(r"she's","she is",tweet)
    tweet = re.sub(r"he's","he is",tweet)
    tweet = re.sub(r"they're","they are",tweet)
    tweet = re.sub(r"who're","who are",tweet)
    tweet = re.sub(r"ain't","am not",tweet)
    tweet = re.sub(r"wouldn't","would not",tweet)
    tweet = re.sub(r"shouldn't","should not",tweet)
    tweet = re.sub(r"can't","can not",tweet)
    tweet = re.sub(r"couldn't","could not",tweet)
    tweet = re.sub(r"won't","will not",tweet)
    
    tweet = re.sub(r"\W"," ",tweet)
    tweet = re.sub(r"\d"," ",tweet)
    tweet = re.sub(r"\s+[a-z]\s+"," ",tweet)
    tweet = re.sub(r"^[a-z]\s+"," ",tweet)    
    tweet = re.sub(r"\s+[a-z]$"," ",tweet)    
    tweet = re.sub(r"\s+"," ",tweet)    
    
    sent = clf.predict(tfidf.transform([tweet]).toarray())
        
    if(sent[0] == 1):
        total_pos += 1
        data0 += "1pos"+tweet+" "+str(sent)
    if(sent[0] == 0):
        total_neg += 1
        data1 += "0neg"+tweet+" "+str(sent)
        
print(data0)
print(data1)
print("Positive",total_pos)
print("Negative",total_neg)