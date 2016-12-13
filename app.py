from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import utils.master
import utils.ticketmaster
import utils.ticketleap
import utils.seatgeek

app = Flask(__name__)

app.secret_key = 'key goes here'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/output", methods=["POST"])
def output():
    eventList = []
    if "searchTerm" in request.form:
        eventList = utils.master.byPriceAsc(request.form["searchTerm"],int(request.form["minPrice"]),int(request.form["maxPrice"]))
        if not eventList:
            eventList = [['No events found. Please try again.','','','#','','','','']]
    elif "quicksearchTerm" in request.form:
        eventList = utils.master.byPriceAsc(request.form["quicksearchTerm"],0,1000)
    else:
        eventList = [['No events found. Please try again.','','','#','','','','']]
    return render_template("output.html",events=eventList)

@app.route("/login", methods=["POST"])
def login():
    return None

if __name__ == "__main__":
    app.debug = True
    app.run()
 
