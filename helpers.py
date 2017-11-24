import xlrd


class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year


# checks if two dates are the same date. date1 is of type Date (we defined it)
# date2 is a tuple
def sameDate(date1, date2):
	return date1.day == str(date2[2]) and date1.month == str(date2[1]) and date1.year == str(date2[0])

# gets all tweet objects from tweet list and date passed to it
def getTweets(date, tweets):
	matchedTweets = []

	for tweet in tweets:
		if tweet.created_at.day == date.day and tweet.created_at.month == date.month and tweet.created_at.year == date.year:
			matchedTweets.append(tweet)
			print(tweet)
	return matchedTweets


#fetches all tweets given the index in the list and returns index of most controversial tweet!
#most controversial defined by sum of retweets and favorites
def worstTweet(tweets):
	
	if len(tweets) == 0:
		return 0

	worstTweet = tweets[0]
	worstTweetScore = getScore(tweets[0])
	for tweet in tweets:
		currentScore = getScore(tweet)
		if currentScore > worstTweetScore:
			worstTweetScore = currentScore
			worstTweet = tweet
	return worstTweet


def getScore(tweet):
	return tweet.retweet_count + tweet.favorite_count
