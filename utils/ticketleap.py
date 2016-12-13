import urllib2, json, requests,dateutil.parser, sorts
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

    q = query.split(" ")[0]
    
    # Final List
    fullList = []

    # Events
    link = "http://public-api.ticketleap.com/events/by/search/"+q+"?key=2416970964522413&page_size=100"
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

            perfName = perfName.replace("_"," ")[:len(perfName)-4]
            
            # Ticket Types
            for ticket_type in data['ticket_types']:
                entry = [] #[organization, event, performance, url, time, ticket type, price, seat]

                entry.append(orgName)
                entry.append(eventName)
                entry.append(perfName)
                entry.append(data['url'])
                time = data['start_utc']
                entry.append(str(dateutil.parser.parse(time)))
                entry.append(ticket_type['name'])
                
                if(ticket_type['price'] == "BUYER_DEFINED_PRICE"):
                    entry.append("N/A: Price Defined by Buyer") 
                else:
                    entry.append(round(float(ticket_type['price']),2))
                entry.append("N/A")
                entry.append("Ticket Leap")
                fullList.append(entry)

    return fullList

## TESTING ##

# def main():
#     fullList = ticketleap("music and things")
#     orderedList = sorts.byDateAsc(fullList)
#     priceRange = sorts.priceRange(orderedList,10,140)
#     for i in priceRange:
#         print(i[1] + " | Price:" + str(i[6]) + " | Time:" + str(i[4]) )

# main()
