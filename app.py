from flask import Flask, render_template, request, redirect, url_for, session, flash
import utils, sqlite3, re
#import utils., utils.story_manager

app = Flask(__name__)

app.secret_key = 'key goes here'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/output", methods=["POST"])
def output():
    eventList = []
    if (request.form["searchTerm"]):
        return render_template("output.html",events=eventList)
    else:
        return render_template("output.html",events=[])

if __name__ == "__main__":
    app.debug = True
    app.run()
 
