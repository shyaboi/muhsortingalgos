from flask import Flask
app = Flask(__name__)
from app import bubblesort
list = [257,5673,667,19,2,31,45,6,113,121,5764,27,42,656,88,234,11,765,66,3,95,3452,55]
from flask import render_template, Response
import time


def sortLoopLoop():
    
    def sortLoop(list):
        if bubblesort(list)==None:
            donzo = 'donezo'
            return donzo
        else:
            # time.sleep(.02)
            loopArr = list
            return loopArr
            sortLoop(list)
    sortLoop(list)
    
    loopArrReturned = str(sortLoop(list))
    
    
    return loopArrReturned

@app.route('/')

def something():
    return sortLoopLoop()