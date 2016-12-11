import urllib2, json, requests
from requests import auth
from requests.auth import HTTPBasicAuth

#28 Oct 2012 23:00:00
def dateConversion(date):
    m = {}
    
    year = date[7:11]

    return year
    

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
                entry.append(dateConversion(data['start_utc']))
                entry.append(ticket_type['name'])
                
                if(ticket_type['price'] == "BUYER_DEFINED_PRICE"):
                    entry.append("N/A: Price Defined by Buyer") 
                else:
                    entry.append(round(float(ticket_type['price']),2))
                entry.append("N/A")

                fullList.append(entry)

    return fullList

def byPriceAsc(query):

    fullList = ticketleap(query)
 
    for i in fullList:
        if i[6] == "N/A: Price Defined by Buyer":
            i[6] = 0.00 # let prices the buyer can define float to the top
    
    orderedList = sorted(fullList, key=lambda entry: round(float(entry[6]),2))

    for i in orderedList:
        if i[6] == 0.00:
            i[6] = "N/A: Price Defined by Buyer" # switch back for proper display

    return orderedList

def byPriceDesc(query):

    orderedList = byPriceAsc(query)
    orderedList.reverse()

    return orderedList

def byDate(query):

    fullList = ticketleap(query)
    

def byAlphaEvent(query):

    fullList = ticketleap(query)
    orderedList = sorted(fullList, key=lambda entry: entry[1])

    return orderedList

def byAlphaPerf(query):

    fullList = ticketleap(query)
    orderedList = sorted(fullList, key=lambda entry: entry[2])


def priceRange(olist,minP,maxP):

    flist = olist
    orderedList = []
    
    for i in flist:
        if i[6] != "N/A: Price Defined by Buyer":
            if i[6] >= minP and i[6] <= maxP:
                orderedList.append(i)
        else:
            orderedList.append(i)

    return orderedList
    
## TESTING ##

def main():
    l = priceRange(byPriceAsc("music and things"),10,140)

    for i in l:
        print(i[6])

main()
