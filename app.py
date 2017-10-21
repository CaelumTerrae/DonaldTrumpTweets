from flask import Flask, render_template
import xlrd

app = Flask(__name__)
workbook = xlrd.open_workbook('realDonaldTrump_tweets.xls')
worksheet = workbook.sheet_by_index(0)


@app.route('/')
def root():
    return 'Hello World'

@app.route('/<month>/<day>/<year>')
def handler(day, month, year):

	



	date = worksheet.cell(1,1).value
	date = xlrd.xldate.xldate_as_tuple(date, 0)
	tweet = worksheet.cell(1,2).value









	return render_template('index.html', year=year,month=month,day=day, tweet=tweet);

if __name__ == '__main__':
    app.debug = True
    app.run()
