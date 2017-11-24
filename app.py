from flask import Flask, render_template, request, jsonify
from helpers import *
from datetime import datetime
import tweepy
import json


app = Flask(__name__)

consumer_key = 	"Bfc0WkrjRCxl0AGp3JI2m7QXk"
consumer_secret = "GyV4dJpLQJfOnELr04tv5vpYt6gGBLEM3sfF4M3imKF1bEj20w"
access_key = 	"1932838459-IQwTLSlwIcqqm1NPv7eW8S1bqyl2GoPprAAoZ3M"
access_secret = 	"ELm1Vhsw2zhhny5N3nDM7RVq2giDxm6BUAAFgGCW0DcKQ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)




@app.route('/')
def root():
    return render_template('landing.html')

@app.route('/today')
def today():
	date = datetime.now()
	tweets = api.user_timeline("realDonaldTrump", count=30)

	tweets = getTweets(date, tweets)
	worst = worstTweet(tweets)
	return render_template('tweets.html', worstTweet=worst)

@app.route('/tweets', methods=["GET", "POST"])
def handler():

	if request.method == "POST":
		
		date = request.form.get("day")
		year = int(date[0:4])
		month = int(date[5:7])
		day = int(date[8:])

		date = datetime(year, month, day)
		tweets = api.user_timeline("realDonaldTrump",count=30)
		
		tweets = getTweets(date, tweets)
		worst = worstTweet(tweets)
		return render_template('tweets.html', worstTweet=worst)

	
if __name__ == '__main__':
    app.debug = True
    app.run()
