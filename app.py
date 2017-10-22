from flask import Flask, render_template
from helpers import *
import xlrd
import tweepy
import json


app = Flask(__name__)
workbook = xlrd.open_workbook('realDonaldTrump_tweets.xls')
worksheet = workbook.sheet_by_index(0)

consumer_key = 	"Bfc0WkrjRCxl0AGp3JI2m7QXk"
consumer_secret = "GyV4dJpLQJfOnELr04tv5vpYt6gGBLEM3sfF4M3imKF1bEj20w"
access_key = 	"1932838459-IQwTLSlwIcqqm1NPv7eW8S1bqyl2GoPprAAoZ3M"
access_secret = 	"ELm1Vhsw2zhhny5N3nDM7RVq2giDxm6BUAAFgGCW0DcKQ"




@app.route('/')
def root():
    return render_template('landing.html')

@app.route('/<month>/<day>/<year>')
def handler(day, month, year):

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	dateToCheck = Date(day, month, year)

	tweetIndices = getTweets(dateToCheck, worksheet)

	worstTweetIndex = worstTweet(tweetIndices, worksheet)

	statusID = worksheet.cell(worstTweetIndex,0).value

	status = api.get_status(statusID)

	tweet = ''

	return render_template('index.html', year=dateToCheck.year,month=dateToCheck.month,day=dateToCheck.day, tweet=tweet);

if __name__ == '__main__':
    app.debug = True
    app.run()
