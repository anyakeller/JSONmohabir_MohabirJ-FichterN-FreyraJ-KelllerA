import urllib2, json, requests
from requests import auth
from requests.auth import HTTPBasicAuth

#
#    Input: Single word query
#  Returns: List of events relevant to the query in New York and information separated in a list of entries
#
#           [organization, event, performance, url, time, ticket type, price, seat]
#
def seatgeek(query):

    fullList = []

    link = "https://api.seatgeek.com/2/events?q="+query.replace(" ","+")+"&venue.state=NY"
    u = urllib2.urlopen(link)
    response = u.read()
    data = json.loads(response)

    events = data['events']
    
    for i in events:
        
        orgName = "N/A"
        eventName = i['title']
        url = i['url']
        time = i['datetime_utc']
        ticket_type = "N/A"
            
        seat = "N/A"

        for j in i['performers']:

            
            price = "N/A"
        
            try:
                float(i['stats']['average_price'])
                price = i['stats']['average_price'] # seatgeek does not show ticket types nor specific prices or seats
            except:
                price = 999999

            
            entry = []
            perfName = j['name']

            entry.append(orgName)
            entry.append(eventName)
            entry.append(perfName)
            entry.append(url)
            entry.append(time)
            entry.append(ticket_type)
            entry.append(price)
            entry.append(seat)

            fullList.append(entry)

    return fullList


def byPrice(query):

    orderedList = []
    fullList = seatgeek(query)

    orderedList = sorted(fullList, key=lambda entry: float(entry[6]))
    
    for i in orderedList:
        if i[6] == 999999:
            i[6] = "N/A: Price not Defined"
    
    return orderedList


## TESTING ##

# def main():
#     listF = byPrice("music")
#     for i in listF:
#         print(i[6])

# main()
