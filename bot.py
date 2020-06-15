#Description:
#This bot will quote tweet itself once every 2 hours until the end of time
#or until Twitter shuts down, whichever comes first. 

import tweepy
import time
from keys import keys

#--------------------Twitter credentials---------------------#
consumer_key = keys['CONSUMER_KEY']
consumer_secret = keys['CONSUMER_SECRET']
access_key = keys['ACCESS_KEY']
access_secret = keys['ACCESS_SECRET']

#---------------------Connect to Twitter---------------------#
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
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
interval = 60 * 60 * 2
while True:
    print("Generating tweet...")
    newTweet = createTweet()
    api.update_status(newTweet)
    time.sleep(interval)
