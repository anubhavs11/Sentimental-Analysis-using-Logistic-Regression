#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 01:38:52 2018

@author: root
"""

import tweepy
from tweepy import OAuthHandler

#Variables that contains the user credentials to access Twitter API 
access_token = "1000286369413873664-nAgh2tNaoBoxvBung3gqg0H4cF2GBe"
access_token_secret = "zTtq8xWSa7ZIEzy1pKtzmIF7Wx9TXIV7c3xHL6sZG67cG"
consumer_key = "e4omtXv9uLZnKWgMIKDcDOmPR"
consumer_secret = "M429qBFcSOaEiOINGAUi4B7PomzE3txAQzLIPTK3u7PyPKPYGU"


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

args = ["google"]
api = tweepy.API(auth,timeout = 10)

query = args[0]
f = open("input/twitter.txt","w")

# this will stream based on the filter
if len(args) == 1:
    for status in tweepy.Cursor(api.search, q = query+" -filter:retweets",lang="en",result_type = "recent").items(100):
        f.write(status.text)