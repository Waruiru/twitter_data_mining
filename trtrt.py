from tweepy import Stream
import json
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from flask import Flask, render_template, request, flash, url_for, redirect

ckey="Z13ORV2NHFgknJsPOCMCNNXkG"
csecret="s7Ep9R6IbC9uPXhCehgNnDzyDM1lQcCMmnq0UQw06fQA0j9Hqs"
atoken="1709707117-JibK1EyA7TCS3Hhuzn5rfOBKPSpepkm0jPSFHfP"
asecret="zae8WJWSXoocsXiCYt8VQ0WJxBYQmP9sbvkXYUGbiYpB0"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
print "service started!"

for tweet in tweepy.Cursor(api.search,
                           q="safaricom",
                           count=100,
                           since="2018-01-14",
                           until="2018-01-15",
                           lang="en").items():
    print tweet.created_at, tweet.text
'''
query = 'Nivea'
max_tweets = 1000
searched_tweets = [json.loads(status.json) for status in tweepy.Cursor(api.search,
                                                                       q=query,
                                                                       count=100,
                                                                       # since_id="24012619984051000",
                                                                       since="2018-01-14",
                                                                       until="2018-01-15",
                                                                       result_type="mixed",
                                                                       lang="en"
                                                                       ).items()]
'''