from tweepy import Stream
import json
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
from GetTweets import listener

ckey="6yMsHkLwEtLldyk2MinN8N7Mb"
csecret="NzFmWgiSWwiF0fK4ic6mnqfaPuUNg471pb2Qcx6aS89z80ho72"
atoken="1709707117-JibK1EyA7TCS3Hhuzn5rfOBKPSpepkm0jPSFHfP"
asecret="zae8WJWSXoocsXiCYt8VQ0WJxBYQmP9sbvkXYUGbiYpB0"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

