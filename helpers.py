import xlrd


class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year


# checks if two dates are the same date. date1 is of type Date (we defined it)
# date2 is a tuple
def sameDate(date1, date2):
	# TODO:

	return False

# gets all tweet indexes from a given date passed to it!
def getTweets(date):
	tweetIndices = []
	return tweetIndices


#fetches all tweets given the index in the list and returns index of most controversial tweet!
#most controversial defined by sum of retweets and favorites
def worstTweet(list):
	worstIndex = 0
	return worstIndex
	


