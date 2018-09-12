#!/usr/bin/python
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from flask import Flask
from flask import Flask, render_template, request, flash, url_for, redirect

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''

    def __init__(self):
        '''
        Class constructor or initialization method.
        '''

        # keys and tokens from the Twitter Dev Console

        consumer_key="Z13ORV2NHFgknJsPOCMCNNXkG"
        consumer_secret="s7Ep9R6IbC9uPXhCehgNnDzyDM1lQcCMmnq0UQw06fQA0j9Hqs"
        access_token="1709707117-JibK1EyA7TCS3Hhuzn5rfOBKPSpepkm0jPSFHfP"
        access_token_secret="zae8WJWSXoocsXiCYt8VQ0WJxBYQmP9sbvkXYUGbiYpB0"

        # attempt authentication

        try:

            # create OAuthHandler object

            self.auth = OAuthHandler(consumer_key, consumer_secret)

            # set access token and secret

            self.auth.set_access_token(access_token,
                    access_token_secret)

            # create tweepy API object to fetch tweets

            self.api = tweepy.API(self.auth)
        except:
            print 'Error: Authentication Failed'

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''

        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"
                        , ' ', tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''

        # create TextBlob object of passed tweet text

        analysis = TextBlob(self.clean_tweet(tweet))

        # set sentiment

        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count=10):
        '''
        Main function to fetch tweets and parse them.
        '''

        # empty list to store parsed tweets

        tweets = []

        try:

            # call twitter api to fetch tweets

            fetched_tweets = self.api.search(q=query, count=count)

            # parsing tweets one by one

            for tweet in fetched_tweets:

                # empty dictionary to store required params of a tweet

                parsed_tweet = {}

                # saving text of tweet

                parsed_tweet['text'] = tweet.text

                # saving sentiment of tweet

                parsed_tweet['sentiment'] = \
                    self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list

                if tweet.retweet_count > 0:

                    # if tweet has retweets, ensure that it is appended only once

                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets

            return tweets
        except tweepy.TweepError, e:

            # print error (if any)

            print 'Error : ' + str(e)

dict1 = {}

def main(search_string, count_data):

    data = {}
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query=search_string, count=count_data)
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment']
               == 'positive']
    # percentage of positive tweets
    print 'Positive tweets percentage: {} %'.format(100 * len(ptweets)
            / len(tweets))

    data['positive_tweets'] = ptweets

    posd  = open("posd.txt", "a")
    posd.write(ptweets)
    posd.write('\n')
    posd.close()

    percantage_positive_tweets = 100 * len(ptweets) / len(tweets)

    pos = open("pos.txt", "w")
    pos.write(percantage_positive_tweets)
    pos.write('\n')
    pos.close()


    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment']
               == 'negative']
    # percentage of negative tweets
    # print 'Negative tweets percentage: {} %'.format(100 * len(ntweets)
    #         / len(tweets))
    print ntweets
    negd = open("negd.txt", "a")
    negd.write(ntweets)
    negd.write('\n')
    negd.close()
    # percentage of neutral tweets
    # print "Neutral tweets percentage: {} % \".format(100* len(tweets - ntweets - ptweets) / len(tweets))
    # printing first 5 positive tweets

    data['negative_tweets'] = ntweets

    percantage_negative_tweets = 100 * len(ntweets) / len(tweets)

    neg = open("neg.txt", "w")
    neg.write(percantage_negative_tweets)
    neg.write('\n')
    neg.close()

    print '''
Positive tweets:'''
    for tweet in ptweets[:10]:
        print tweet['text']

    # printing first 5 negative tweets
    print '''
Negative tweets:'''
    for tweet in ntweets[:10]:
        print tweet['text']





    dict1 = {'percantage_positive_tweets':percantage_positive_tweets,'negative_positive_tweets'  : percantage_negative_tweets,
    "negative_tweets":ntweets,"positive_tweets":ptweets}

    return  dict1



app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    print "get request received! Processing request"
    return render_template("analysis.html")

@app.route('/post', methods=['post'])
def method():
    data = {}
    print "post request!"
    search_string = request.form.get('search_string')
    print search_string

    data = {}
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query=search_string, count=count_data)
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment']
               == 'positive']
    # percentage of positive tweets
    print 'Positive tweets percentage: {} %'.format(100 * len(ptweets)
            / len(tweets))

    data['positive_tweets'] = ptweets

    posd  = open("posd.txt", "a")
    posd.write(ptweets)
    posd.write('\n')
    posd.close()

    percantage_positive_tweets = 100 * len(ptweets) / len(tweets)

    pos = open("pos.txt", "w")
    pos.write(percantage_positive_tweets)
    pos.write('\n')
    pos.close()


    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment']
               == 'negative']
    # percentage of negative tweets
    # print 'Negative tweets percentage: {} %'.format(100 * len(ntweets)
    #         / len(tweets))
    print ntweets
    negd = open("negd.txt", "a")
    negd.write(ntweets)
    negd.write('\n')
    negd.close()
    # percentage of neutral tweets
    # print "Neutral tweets percentage: {} % \".format(100* len(tweets - ntweets - ptweets) / len(tweets))
    # printing first 5 positive tweets

    data['negative_tweets'] = ntweets

    percantage_negative_tweets = 100 * len(ntweets) / len(tweets)

    neg = open("neg.txt", "w")
    neg.write(percantage_negative_tweets)
    neg.write('\n')
    neg.close()

    print '''
Positive tweets:'''
    for tweet in ptweets[:10]:
        print tweet['text']

    # printing first 5 negative tweets
    print '''
Negative tweets:'''
    for tweet in ntweets[:10]:
        print tweet['text']

    dict1 = {'percantage_positive_tweets':percantage_positive_tweets,'negative_positive_tweets':negative_positive_tweets}


#    dict1 = main(search_string, 200)
    return render_template("home.html",name = dict1, tweets=ptweets)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '127.0.0.1',port=59563)
