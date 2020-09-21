from flask import Flask
app = Flask(__name__)
from flask import abort, Flask, redirect, url_for, render_template, Response, jsonify, request
import time
from flask import Flask
from flask_cors import CORS
import sys
sys.path.append('../')
from sortingAlgos.bubs import benix
from sortingAlgos.bLite import benixLite

app = Flask(__name__)
CORS(app)


@app.route('/bubbleSort', methods = ['POST'])
def receive_data():
    return jsonify(benix(request.form['arrToSort'],request.form['randomIndices']))

@app.route('/onlyFinalResult/bubbleSort', methods = ['POST'])
def onlyFinalResultbubbleSort():
    return jsonify(benixLite(request.form['arrToSort']))
    # return 'thanks bruh'
@app.route('/', methods = ['GET'])
def index():
    return render_template("index.html")

@app.route('/bubbleSort', methods = ['GET'])
def bubSort():
    return render_template("bubsort.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')