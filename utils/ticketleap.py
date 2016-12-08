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
def ticketleap(query):

    # Final List
    fullList = []

    # Events
    link = "http://public-api.ticketleap.com/events/by/search/"+query+"?key=2416970964522413&page_size=100"
    u = urllib2.urlopen(link)
    response = u.read()
    data = json.loads(response)
    search = data['events']
    events = []
    for e in search:
        if e['venue_region_name'] == "NY":
            events.append(e)
    for i in events:
        
        org = i['organization_slug']
        eve = i['slug']
        
        orgName = i['organization_name']
        eventName = i['name']
        
        link = "http://public-api.ticketleap.com/organizations/"+org+"/events/"+eve+"?key=2416970964522413&page_size=100"
        u = urllib2.urlopen(link)
        response = u.read()
        data = json.loads(response)
        perf = data['performances']

        # Performances
        for j in perf:
            perfName = j['slug']
            
            link = "http://public-api.ticketleap.com/organizations/"+org+"/events/"+eve+"/performances/"+perfName+"?key=2416970964522413&page_size=100"
            u = urllib2.urlopen(link)
            response = u.read()
            data = json.loads(response)

            # Ticket Types
            for ticket_type in data['ticket_types']:
                entry = [] #[organization, event, performance, url, time, ticket type, price, seat]

                entry.append(orgName)
                entry.append(eventName)
                entry.append(perfName)
                entry.append(data['url'])
                entry.append(data['start_utc'])
                entry.append(ticket_type['name'])
                
                if(ticket_type['price'] == "BUYER_DEFINED_PRICE"):
                    entry.append(0)
                else:
                    entry.append(ticket_type['price'])
                entry.append("N/A")

                fullList.append(entry)

    return fullList

def byPrice(query):

    orderedList = []
    fullList = ticketleap(query)

    orderedList = sorted(fullList, key=lambda entry: float(entry[6]))

    for i in orderedList:
        if i[6] == 0:
            i[6] = "N/A: Price Defined by Buyer"

    return orderedList

## TESTING ##

def main():
     print(byPrice("music"))

main()
