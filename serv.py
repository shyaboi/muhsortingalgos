from sortingAlgos.bLite import benixLite
from sortingAlgos.bubs import benix
from sortingAlgos.insertLite import insertLite
import sys
from flask_cors import CORS
import time
from flask import abort, Flask, redirect, url_for, render_template, Response, jsonify, request
from flask import Flask
app = Flask(__name__)
sys.path.append('../')

app = Flask(__name__)
CORS(app)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~bubble sort routes start
# buble 
@app.route('/api/py-sort/bubbleSort', methods=['POST'])
def receive_data():
    return jsonify(benix(request.form['arrToSort'], request.form['randomIndices']))

# final result api route
@app.route('/api/py-sort/bubbleSortResult', methods=['POST'])
def bubbleSortResult():
    return jsonify(benixLite(request.form['arrToSort']))
# bub sort get jinja page
@app.route('/api/py-sort/bubbleSort', methods=['GET'])
def bubSort():
    return render_template("bubsort.html")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~bubble sort routes end
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~insert sort routes start
@app.route('/api/py-sort/insertSort', methods=['GET'])
def insertSortGet():
    return render_template("insertSort.html")

@app.route('/api/py-sort/insertSortResult', methods=['POST'])
def insertSortResult():
    return jsonify(insertLite(request.form['arrToSort']))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~insert sort routes end



@app.route('/api/py-sort/docs', methods=['GET'])
def apiDocs():
    return render_template("docs.html")

@app.route('/api/py-sort/home', methods=['GET'])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
