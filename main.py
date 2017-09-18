import auth
import tweepy
import top100

consumer_key = auth.key
consumer_secret = auth.secret
access_token = auth.token
access_token_secret = auth.tokenSecret
userlist = top100.userlist




# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 
for user in userlist:
	try:
		timeline = api.user_timeline(user,count=200)
		print user
		userTweetCount = 0
		for tweet in timeline:
			print tweet.retweet_count 
		print ( "---" )
	except tweepy.error.TweepError:
		print "Error for" + user
	




