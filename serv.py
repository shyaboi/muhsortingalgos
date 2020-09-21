from flask import Flask
app = Flask(__name__)
from flask import abort, Flask, redirect, url_for, render_template, Response, jsonify, request
import time
from flask import Flask
from flask_cors import CORS
from bubs import benix

app = Flask(__name__)
CORS(app)


@app.route('/', methods = ['POST'])
def receive_data():
    return jsonify(benix(request.form['myData'], request.form['otherData']))
    # return 'thanks bruh'
@app.route('/', methods = ['GET'])
def index():
    return render_template("index.html")

@app.route('/bubbleSort', methods = ['GET'])
def bubSort():
    return render_template("bubsort.html")
# def something():
#     # lastMake()
#     txt = '432 5 5787 4 324 43 3 6 77 7 67 543 543'

if __name__ == "__main__":
    app.run(host='0.0.0.0')