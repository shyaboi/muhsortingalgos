from flask import Flask
app = Flask(__name__)
from app import bubblesort
from flask import abort, Flask, redirect, url_for, render_template, Response, jsonify, request
import time
from flask import Flask
from flask_cors import CORS
from bubs import benix

app = Flask(__name__)
CORS(app)


@app.route('/', methods = [ 'GET','POST'])
def receive_data():
    return jsonify(benix(request.form['myData']))
    # return 'thanks bruh'
def something():
    # lastMake()
    txt = '432 5 5787 4 324 43 3 6 77 7 67 543 543'