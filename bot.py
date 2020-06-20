#Description:
#This bot will quote tweet itself once every 15 minutes until the end of time
#or until Twitter shuts down, whichever comes first. 

import tweepy
import time
import os
from os import environ

#-----------------------Twitter credentials-----------------------#
#Fill in on Heroku dashboard
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

#------------------------Connect to Twitter-----------------------#
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#------------------------Generate Tweets--------------------------#
num = 1
def createTweet():
    global num

    #Get most recent tweet ID
    for status in api.user_timeline('RecursionBot', count = 1):
        tweetID = status.id

    #Attach ID to template URL
    blankURL = 'https://twitter.com/RecursionBot/status/'
    prevTweet = "{}{}".format(blankURL, tweetID)

    #Generate new tweet
    tweet = "Level: {} \n {}".format(num, prevTweet)
    num += 1
   
    return tweet

#--------------------------Post Timer---------------------------#
interval = 60 * 15 #Post every 15 min
while True:
    print("Generating tweet...")
    api.update_status(createTweet())
    time.sleep(interval)
