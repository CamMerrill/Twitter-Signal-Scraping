import auth
import tweepy
import top100
import top1000
import csv

consumer_key = auth.key
consumer_secret = auth.secret
access_token = auth.token
access_token_secret = auth.tokenSecret
userList = top1000.userList



with open ('top1000Scraped.csv', 'wb') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=' ')
	# Creating the authentication object
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	# Setting your access token and secret
	auth.set_access_token(access_token, access_token_secret)
	# Creating the API object while passing in auth information
	api = tweepy.API(auth) 
	csvwriter.writerow(['User', 'Follower Count', 'First Tweet Date', 'Last Tweet Date', 'Time Between T1 Tn',
				'Avg Tweets Per Day', 'Tweet Total', 'Retweet Total', 'Favorite Total', 
				'Avg Favorites', 'Average Retweets', 'Avg Inter Per Tweet', 'Avg Int Per Tweet Per Follower'])
	for user in userList:
		try:
			timeline = api.user_timeline(user,count=200)
			tweepyUser = api.get_user(user)
			#print user
			userTweetCount = 0
			userRetweetTotal = 0
			userFavoriteTotal = 0
			userRepliesTotal = 0

			try:
				firstTweet =  timeline[0]
			except IndexError:
				print ("FIX THIS: " + user)
				raise tweepy.error.TweepError
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
			if days == 0:
				days = 1
			avgFav = float(userFavoriteTotal)/days
			avgRet = float(userRetweetTotal)/days
			'''
			print "Follower Count: " + str(tweepyUser.followers_count)
			print "Most Recent Tweet: " + str(firstTweetDate)
			print "Last Crawled Tweet Date: " + str(lastTweetDate)
			print "Days between: " + str(delta.days) 
			print "Avg Tweets per day: " + str(float(userTweetCount)/days)
			print "Tweet Total: " + str(userTweetCount)
			print "Retweet Total: " + str(userRetweetTotal)
			print "Favorite Total: " + str(userFavoriteTotal)
			print "Average Favorites per Tweet: " + str(avgFav)
			print "Average Retweets per Tweet: " + str(avgRet)
			print "Total Avg Interactions: " + str(avgFav + avgRet)
			print "Avg Interactions Per Follower" + str(float(avgFav+avgRet)/tweepyUser.followers_count)
			'''
			
			csvwriter.writerow([user, tweepyUser.followers_count, firstTweetDate, lastTweetDate, days, 
				float(userTweetCount)/days, userTweetCount, userRetweetTotal, userFavoriteTotal, 
				float(userFavoriteTotal)/userTweetCount, float(userRetweetTotal)/userTweetCount, avgRet+avgFav, (avgFav+avgRet)/tweepyUser.followers_count])
			#print ("------")
			
		except tweepy.error.TweepError:
			print "Error for " + user
		




