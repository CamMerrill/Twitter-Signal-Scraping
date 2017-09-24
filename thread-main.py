import auth
import tweepy
import csv
import sys

from urlparse import urlparse
from threading import Thread
import httplib, sys
from Queue import Queue

concurrent = 10

def doWork():
    while True:
		
        userName = q.get()
	#GetDataFromTL
	userData = getDataFromTimeline(user)
	#WriteData to CSV
        q.task_done()

def getDataFromTimeline(user):
	try:
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		api = tweepy.API(auth) 
		try:
			timeline = api.usertimeline(user, count=200)
		except tweepy:
			raise tweepy.TweepError(user, e)
		try:
			
			
	except tweepy.error.TweepError:
		print "Error for " + user
		
		
	

def writeToFile():
	#User, FollowerCount, FirstTweetDate, LastTweetDate
	#Avg Tweets/day, Tweet Total, RT Total, Fav Total
	#Avg Fav/tweet, Avg retweets/tweet, Avg inter/tweet
	#Avg Int Per Tweet Per Follower
	

inputFileName = str(sys.argv[1:])
inputFile = open(inputFileName[2:-2], "r")

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    for line in inputFile:
        q.put(line)
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
