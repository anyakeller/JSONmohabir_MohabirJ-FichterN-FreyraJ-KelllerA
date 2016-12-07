import urllib2, json, requests
from requests import auth
from requests.auth import HTTPBasicAuth

#
#    Input: Single word query
#  Returns: List of events relevant to the query in New York and information separated in a list of entries
#
#           [organization, event, performance, url, time, ticket type, price, seat]
#
#  Each entry is grouped by the most general shared information
#       - Tickets of similar organization are grouped together
#       - Tickets of similar events are grouped together
#       - Tickets of similar performances are grouped together and separated by ticket type
#
def ticketmaster(query):

    fullList = []

    link = "https://app.ticketmaster.com/discovery/v2/events.json?keyword="+query+"&dmaId=345&apikey=pH93aoYEABgaNXBfcWGS5fS9cid3QuAw"
    u = urllib2.urlopen(link)
    response = u.read()
    data = json.loads(response)
    events = data['_embedded']['events']

    for i in events:

        orgName = "Ticketmaster"
        eventName = i['name']
        perfName = i['name']
        url = i['url']
        
