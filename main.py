from tweepy import Stream
import json
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
ckey="Z13ORV2NHFgknJsPOCMCNNXkG"
csecret="s7Ep9R6IbC9uPXhCehgNnDzyDM1lQcCMmnq0UQw06fQA0j9Hqs"
atoken="1709707117-JibK1EyA7TCS3Hhuzn5rfOBKPSpepkm0jPSFHfP"
asecret="zae8WJWSXoocsXiCYt8VQ0WJxBYQmP9sbvkXYUGbiYpB0"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)


class listener(StreamListener):
    print "method for tweet retreival started"
    def on_data(self, data):
        import sentiment_mod as s
        all_data = json.loads(data)

        outputfile = open('raw_data.txt', 'a')
        outputfile.write(data)
        outputfile.write('\n')
        outputfile.close()

        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print "classification"
        print(tweet, sentiment_value, confidence)
        if confidence*100 >= 80:
            output = open("twitter-out.txt", "a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()

        return True

    def on_error(self, status):
        print(status)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['fanta'])
