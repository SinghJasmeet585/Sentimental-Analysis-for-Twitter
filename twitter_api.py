# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 00:04:58 2019

@author: jasjag
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
#import sentiment_mod as s


#consumer key, consumer secret, access token, access secret.
ckey="awEhBjkdwTpaoNKnrfUrK6R99p "
csecret="5pOluFfLPUqsj3aNghkVPSxwv4zl4QzCaodiziVdFICBXRA7Jk"
atoken="742455567315173376-iS7VRRZf2thsyzjcKlnoA4ZlWZ3TLR7 "
asecret="z3GzT9gpOtnvwTrmR49VGdybLLfZMPcbYKevwbps9TQB3"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
#        sentiment_value, confidence=s.sentiment(tweet)
#        print(tweet, sentiment_value, confidence)
        print(tweet)
        
 #       if confidence*100 >= 80:
 #           output = open("twitter-out.txt","a")
 #           output.write(sentiment_value)
 #           output.write('\n')
 #           output.close()
        
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["obama"])