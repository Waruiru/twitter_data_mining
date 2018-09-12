from tweepy import Stream
import json
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from flask import Flask, render_template, request, flash, url_for, redirect

app = Flask(__name__)
# consumer key, consumer secret, access token, access secret.
ckey = "6yMsHkLwEtLldyk2MinN8N7Mb"
csecret = "NzFmWgiSWwiF0fK4ic6mnqfaPuUNg471pb2Qcx6aS89z80ho72"
atoken = "1709707117-JibK1EyA7TCS3Hhuzn5rfOBKPSpepkm0jPSFHfP"
asecret = "zae8WJWSXoocsXiCYt8VQ0WJxBYQmP9sbvkXYUGbiYpB0"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

print "service started!"


class listener(StreamListener):
    def on_data(self, data):
        print "method for tweet retrieval started!"
        import sentiment_mod as s
        all_data = json.loads(data)
        print "data fetched, saving it to file!"
        outputfile = open('raw_data.txt', 'a')
        outputfile.write(data)
        outputfile.write('\n')
        outputfile.close()
        print "written to file!"
        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        display =(tweet, sentiment_value, confidence)
        print display
        if confidence * 100 >= 80:
            output = open("twitter-out.txt", "a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()
			
			savetweet = open("tweet.txt", "a")
            savetweet.write(tweet)
            savetweet.write('\n')
            savetweet.close()
            print "returning result to web!"
            return display
        return True

    def on_error(self, status):
        print "error ! ->"
        print(status)

@app.route('/', methods=['GET'])
def index():
    print "get request received! Processing request"
    return render_template("home.html")


@app.route('/post', methods=['post'])
def method():
    print "post request!"
    search_string = request.form.get('search_string')
    print search_string
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=[search_string])

    return
if __name__ == '__main__':
    app.run()
