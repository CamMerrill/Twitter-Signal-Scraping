
#Special acknowledgement: Kevin Rodewald
import auth
import tweepy
import csv
import sys

consumer_key = auth.key
consumer_secret = auth.secret
access_token = auth.token
access_token_secret = auth.tokenSecret
userList = []


inputFileName = str(sys.argv[1:])
inputFile = open(inputFileName[2:-2], "r")
for line in inputFile:
	userList.append(line)
	


with open ("Datasets/" + inputFileName[14:-2] + ".csv", 'wb') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=';')
	# Creating the authentication object
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	# Setting your access token and secret
	auth.set_access_token(access_token, access_token_secret)
	# Creating the API object while passing in auth information
	api = tweepy.API(auth, wait_on_rate_limit=True) 
	userCount = 0
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
			except IndexError as e:
				print ("Error for: " + user)
				raise tweepy.TweepError(user, e)
			firstTweetDate = firstTweet.created_at
			userCount += 1	
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
			user = user.strip()
			
			csvwriter.writerow([user, tweepyUser.followers_count, firstTweetDate, lastTweetDate, days, 
				float(userTweetCount)/days, userTweetCount, userRetweetTotal, userFavoriteTotal, 
				float(userFavoriteTotal)/userTweetCount, float(userRetweetTotal)/userTweetCount, avgRet+avgFav, (avgFav+avgRet)/tweepyUser.followers_count])
			#print ("------")
			print userCount
			
		except tweepy.error.TweepError as e:
			print "Error for " + user + str(e)
		
print userCount



