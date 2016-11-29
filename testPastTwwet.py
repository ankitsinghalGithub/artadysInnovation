#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import csv
import sys
import requests

access_token = "957322597-gjJB25i4z6LeoaZAY15DJNJTTdM4IIhQcA2phIl9"
access_token_secret = "BuF16sTiciQbkHt3wIpTsANGsdFT6ngBjug3HFcZSbOhh"
consumer_key = "8vCwfYFBVdJx3kC154N2jbrR8"
consumer_secret = "T67HYNgEH1DHVlG9Nzdj1CcaDjkWPUc6bI7Q8ro1Zuwtn94lFh"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# Open/Create a file to append data
csvFile = open('tweetsHistory1.csv', 'a')
#tweet_RSS_file = open('tweets_RSS.json', 'a')
	#Use csv Writer
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,q='EUROVIA',since='2016-11-01',lang='en').items():
	#csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
	csvWriter.writerow([tweet])


csvFile.close()
