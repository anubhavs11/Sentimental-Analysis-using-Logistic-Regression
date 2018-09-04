#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 21:23:47 2018

@author: root
"""
import nltk
import pickle
import re

from nltk.corpus import stopwords
from sklearn.datasets import load_files

nltk.download("stopwords")

reviews = load_files("txt_sentoken")
X,y = reviews.data,reviews.target

# storing the data as pickle file ---AS pickle files are faster to load because they store data
# in the form fo stream of bytes
with open("preserved files/X.pickle","wb") as f:
    pickle.dump(X,f)

with open("preserved files/y.pickle","wb") as f:
    pickle.dump(y,f)
    
# loading data from pickle file
with open("preserved files/X.pickle","rb") as f:
    X = pickle.load(f)
    
with open("preserved files/y.pickle","rb") as f:
    y = pickle.load(f)
    
# cretaing corpus
corpus = []

#PREPROCESSING
for i in range(len(X)):
    review = re.sub(r"\W"," ",str(X[i]))
    review = review.lower()
    review = re.sub(r"\s+"," ",review)
    review = re.sub(r"\s+[a-z]\s+"," ",review)
    review = re.sub(r"^[a-z]\s+","",review)
    corpus.append(review)


# Creating BOW
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=2000,min_df =3 ,max_df = 0.6, stop_words = stopwords.words("english"))    
X = vectorizer.fit_transform(corpus).toarray()

#Cretaing TF-IDF from BOW
from sklearn.feature_extraction.text import TfidfTransformer

transformer = TfidfTransformer()
X = transformer.fit_transform(X).toarray()

#Spliting for testing and training

from sklearn.model_selection import train_test_split

text_train,text_test,sent_train,sent_test = train_test_split(X,y,test_size=0,random_state=0)
# here text size = 0 , so that all the data will be used for the training purpose only

# Training our classifier
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(text_train,sent_train)

# Pickling the classifier
with open("preserved files/classifier.pickle","wb") as f:
    pickle.dump(classifier,f)

with open("preserved files/TfidfModel.pickle","wb") as f:
    pickle.dump(vectorizer,f)
# this pickle file is saved so that it can be used with the mapper 