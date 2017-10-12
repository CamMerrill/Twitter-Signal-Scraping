import auth
import tweepy
import csv
import sys


consumer_key = auth.key
consumer_secret = auth.secret
access_token = auth.token
access_token_secret = auth.tokenSecret
userList = []


user = "verified"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth, wait_on_rate_limit=True) 

for id in tweepy.Cursor(api.friends_ids, id="CamMerrill").items():
	print id


