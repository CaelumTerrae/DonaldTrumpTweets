from flask import Flask, render_template
from helpers import *
import xlrd


app = Flask(__name__)
workbook = xlrd.open_workbook('realDonaldTrump_tweets.xls')
worksheet = workbook.sheet_by_index(0)


@app.route('/')
def root():
    return 'Hello World'

@app.route('/<month>/<day>/<year>')
def handler(day, month, year):

	dateToCheck = Date(day, month, year)

	tweetIndices = getTweets(dateToCheck, worksheet)

	worstTweetIndex = worstTweet(tweetIndices, worksheet)

	tweet = worksheet.cell(worstTweetIndex,2).value


	return render_template('index.html', year=dateToCheck.year,month=dateToCheck.month,day=dateToCheck.day, tweet=tweet);

if __name__ == '__main__':
    app.debug = True
    app.run()
