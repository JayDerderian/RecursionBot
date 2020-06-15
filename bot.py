import tweepy
import time
import sys
import os

#--------------------Twitter credentials---------------------#
#Update these values on the Heroku dashboard.
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

#---------------------Connect to Twitter---------------------#
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#----------------------Generate Tweets-----------------------#
lastTweet = None
num = 1
def createTweet():
    global lastTweet
    global num
    #Get most recent tweet ID
    for status in api.user_timeline('RecursionBot', count = 1):
        tweetID = status.id
    #Attach ID to template URL
    blankURL = 'https://twitter.com/RecursionBot/status/'
    mostRecentTweet = "{}{}".format(blankURL, tweetID)
    #Generate new tweet
    if mostRecentTweet != lastTweet:
        tweet = "Level: {} \n {}".format(num, mostRecentTweet)
        num += 1
    lastTweet = mostRecentTweet
    return tweet

#------------------------Post Timer-------------------------#
interval = 60 * 60
while True:
    print("Generating tweet...")
    newTweet = createTweet()
    api.update_status(newTweet)
    time.sleep(interval)
