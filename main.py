import auth
import tweepy

consumer_key = auth.key
consumer_secret = auth.secret
access_token = auth.token
access_token_secret = auth.tokenSecret



# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 




