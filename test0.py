from flask import Flask, render_template
import urllib2, json, requests
from requests import auth
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

@app.route("/")
def root():
    u = urllib2.urlopen("https://api.seatgeek.com/2/events?venue.state=NY")
    response = u.read()
    data = json.loads(response)
    print(data)
    #return render_template("index.html", pic = data['url'] )


if __name__ == "__main__":
   app.debug = True
   app.run()
