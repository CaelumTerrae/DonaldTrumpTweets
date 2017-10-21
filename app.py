from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return 'Hey shbeebee'

@app.route('/shmlavin')
def shmlavin():
    return 'shmlarah?'

@app.route('/shmlarah')
def shmlarah():
    return 'shmlavin?'

if __name__ = '__main__':
    app.debug = True
    app.run()
