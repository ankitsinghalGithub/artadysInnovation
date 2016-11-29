#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import csv
import requests
#Variables that contains the user credentials to access Twitter API
access_token = "957322597-gjJB25i4z6LeoaZAY15DJNJTTdM4IIhQcA2phIl9"
access_token_secret = "BuF16sTiciQbkHt3wIpTsANGsdFT6ngBjug3HFcZSbOhh"
consumer_key = "8vCwfYFBVdJx3kC154N2jbrR8"
consumer_secret = "T67HYNgEH1DHVlG9Nzdj1CcaDjkWPUc6bI7Q8ro1Zuwtn94lFh"

c=0
name =[]
loc =[]
tweet =[]
data1 = []
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        #Just write data to one line in the file
        global data1,c
        if (c<5):
            d = json.loads(data)
            #name.append(d['user']['name'])
            #loc.append(d['user']['location'])
            #tweet.append(d['text'])
            l=d['user']['location']
            #print (l, type(l))
            if l is None:
                l='None'
            #print ('ddd',l, type(l))
            data123 = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+l+'&key=AIzaSyBPniJUxYnftn0QCRA5nJuUA0gu2PXJLKM')
            t1 = json.loads(data123.text)
            cord= t1['results'][0]['geometry']['location']
            #print (cord)
            sent='NEU'
            #print ('\n\n\n',c,d['text'])
            sentscore1 = requests.get('http://www.sentiment140.com/api/classify?text=' + d['text'])
            #print (sentscore1)
            sn= json.loads(sentscore1.text)
            sentscore = sn['results']['polarity']
            #print (sentscore)
            if sentscore ==0:
                sent ='N'
            elif sentscore ==4:
                sent = 'P'
            else:
                sent = 'O'

            t= (d['user']['name'], cord, d['text'],l, sent)
            data1.append(t)
            #print (name, loc, tweet)
            #print ('\n\n\n', c)
            c=c+1
            #print (data1)
            return True
        else :
            return False

    def on_error(self, status):
        print (status)


def getInfo(searchword):
    try:
        #Create a file to store output. "a" means append (add on to previous file)

        #This handles Twitter authetification and the connection to Twitter Streaming API
        #name =[]
        #l = StdOutListener()
        #auth = OAuthHandler(consumer_key, consumer_secret)
        #auth.set_access_token(access_token, access_token_secret)
        #stream = Stream(auth, l)
        #This line filter Twitter Streams to capture data by the keywords: 'ISIS'
        #stream.filter(track=[searchword],languages=['en'])

        print ("inside getInfo")
        global data1

        data =[]
        with open('tweets.csv') as f:
            data=[tuple(line) for line in csv.reader(f)]

        print (data)
        for d in data:

            l=d[2]
            print (l)
            data123 = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+l+'&key=AIzaSyBPniJUxYnftn0QCRA5nJuUA0gu2PXJLKM')
            t1 = json.loads(data123.text)
            cord= t1['results'][0]['geometry']['location']
            print (cord)
            sent ='P'
            t= (d[0],cord,d[1],l, sent)
            print (t)
            data1.append(t)
            print (data1)

        print (data1)


    except KeyboardInterrupt:
        #User pressed ctrl+c -- get ready to exit the program
        pass

    #Close the file
    t =  data1
    return t
