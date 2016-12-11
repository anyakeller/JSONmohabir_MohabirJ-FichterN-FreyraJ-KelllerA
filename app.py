from flask import Flask, render_template, request, redirect, url_for, session, flash
import utils, sqlite3
#from utils import seatgeek, ticketleap, ticketmaster

app = Flask(__name__)

app.secret_key = 'key goes here'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/output", methods=["POST"])
def output():
    eventList = []
    if "searchTerm" in request.form:
        eventList = []
        #do stuff to eventList (waiting on utils)
    elif "quicksearchTerm" in request.form:
        eventList = []
        #do stuff to eventList (waiting on utils)
    else:
        eventList = []
    return render_template("output.html",events=eventList)

@app.route("/login", methods=["POST"])
def login():
    return None

if __name__ == "__main__":
    app.debug = True
    app.run()
 
