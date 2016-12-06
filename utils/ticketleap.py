from flask import Flask, render_template
import urllib2, json, requests
from requests import auth
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

@app.route("/")
def ticketleap():
    link = "http://public-api.ticketleap.com/events/by/search/"+"music"+"?key=2416970964522413&page_size=100"
    u = urllib2.urlopen(link)
    response = u.read()
    data = json.loads(response)
    events = data['events']
    for e in events:
        print(e['name'])
        
# def main():
#     ticketleap("music")

if __name__ == "__main__":
   app.debug = True
   app.run()
