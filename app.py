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
    #start with empty list
    eventList = []
    if "searchTerm" in request.form: #check if user searched by main search function
        if request.form["searchTerm"] == "": #if no search term, tell them to enter one
            flash("Please enter a search term!")
            return redirect(url_for("index"))
        else: #get the list from master.py (default: price ascending)
            eventList = utils.master.byPriceAsc(request.form["searchTerm"],int(request.form["minPrice"]),int(request.form["maxPrice"]))
            if not eventList: #if no results, tell them to try again
                flash("No results were found. Please try again!")
                return redirect(url_for("index"))
            #add the search terms to the session so that the user can modify the way their output is sorted
            session['searchTerm'] = request.form['searchTerm']
            session['minPrice'] = request.form['minPrice']
            session['maxPrice'] = request.form['maxPrice']
    elif "quicksearchTerm" in request.form: #check if user quicksearched
        if request.form["quicksearchTerm"] == "": #if no search term, tell them to enter one
            flash("Please enter a search term!")
            return redirect(url_for("index"))
        else: #get the list from master.py (default: price ascending,minP = 0, maxP = 1000)
            eventList = utils.master.byPriceAsc(request.form["quicksearchTerm"],0,1000)
            if not eventList: #if no results, tell them to try again
                flash("No results were found. Please try again!")
                return redirect(url_for("index"))
            #add the search terms to the session so that the user can modify the way their output is sorted
            session['searchTerm'] = request.form['quicksearchTerm']
            session['minPrice'] = 0
            session['maxPrice'] = 1000
    elif "searchTerm" in session: #check if they have already searched when they try to sort
        if request.form["filterbuttons"] == "filterPA":
            eventList = utils.master.byPriceAsc(session['searchTerm'],int(session['minPrice']),int(session['maxPrice']))
        if request.form["filterbuttons"] == "filterPD":
            eventList = utils.master.byPriceDes(session['searchTerm'],int(session['minPrice']),int(session['maxPrice']))
        if request.form["filterbuttons"] == "filterDA":
            eventList = utils.master.byDateAsc(session['searchTerm'],int(session['minPrice']),int(session['maxPrice']))
        if request.form["filterbuttons"] == "filterDD":
            eventList = utils.master.byDateDes(session['searchTerm'],int(session['minPrice']),int(session['maxPrice']))
        if request.form["filterbuttons"] == "filterAA":
            eventList = utils.master.byPriceAsc(session['searchTerm'],int(session['minPrice']),int(session['maxPrice']))
        if request.form["filterbuttons"] == "filterAD":
            eventList = utils.master.byPriceAsc(session['searchTerm'],int(session['minPrice']),int(session['maxPrice']))
    else: #if none of the above, there was an error --> try again
        flash("There was an error. Please try again!")
        return redirect(url_for("index"))
    
    return render_template("output.html",events=eventList)

if __name__ == "__main__":
    app.debug = True
    app.run()
 
