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
		userRetweetTotal = 0
		userFavoriteTotal = 0
		userRepliesTotal = 0

		firstTweet =  timeline[0]
		firstTweetDate = firstTweet.created_at
	
		for tweet in timeline:
			userRetweetTotal += tweet.retweet_count
			userFavoriteTotal += tweet.favorite_count
			#replies is tricky, do later
			userTweetCount += 1
		lastTweet = timeline[userTweetCount-1]
		lastTweetDate = lastTweet.created_at
		delta = firstTweetDate - lastTweetDate
		days = delta.days

		print "Most Recent Tweet: " + str(firstTweetDate)
		print "Last Crawled Tweet Date: " + str(lastTweetDate)
		print "Days between: " + str(delta.days) 
		print "Avg Tweets per day: " + str(float(userTweetCount)/delta.days)
		print "Tweet Total: " + str(userTweetCount)
		print "Retweet Total: " + str(userRetweetTotal)
		print "Favorite Total: " + str(userFavoriteTotal)
		print "Average Favorites per Tweet: " + str(float(userFavoriteTotal/userTweetCount)
		print "Average Retweets per Tweet: " + str(float(userRetweetTotal/userTweetCount)
		print ("------")
		
	except tweepy.error.TweepError:
		print "Error for" + user
	




