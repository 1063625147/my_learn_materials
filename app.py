from flask import Flask, render_template
import random
from test import getdata


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/test')
def showdata():
    data=getdata()
    return data


if __name__ == '__main__':
    app.run(debug=True)