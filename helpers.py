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

# gets all tweet indexes from a given date passed to it!
def getTweets(date, worksheet):
	tweetIndices = []

	i = 0
	while i < 3000:
		i += 1
		currentDate = worksheet.cell(i,1).value
		currentDate = xlrd.xldate.xldate_as_tuple(currentDate, 0)
		print date.month + ' ' + date.day + ' ' + date.year
		print str(currentDate[1]) + ' ' + str(currentDate[2]) + ' ' + str(currentDate[0])
		if sameDate(date, currentDate):
			tweetIndices.append(i+1)
			
	return tweetIndices


#fetches all tweets given the index in the list and returns index of most controversial tweet!
#most controversial defined by sum of retweets and favorites
def worstTweet(list, worksheet):
	
	if len(list) == 0:
		return 0

	worstIndex = list[0]
	worstIndexScore = 0
	for index in list:
		currentScore = getScore(index, worksheet)
		if currentScore > worstIndexScore:
			worstIndexScore = currentScore
			worstIndex = index
	return worstIndex

def getScore(index, worksheet):
	return worksheet.cell(index,3).value + worksheet.cell(index,4).value
	


