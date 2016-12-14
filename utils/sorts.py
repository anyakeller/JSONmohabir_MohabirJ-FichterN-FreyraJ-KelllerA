# Sorting Query module
#
# Sorts for a given list of lists with entries of format:
#       [organization, event, performance, url, time, ticket type, price, seat]
#


# Sorts list by price in ascending order
# Will replace placeholder text with numerical values to allow entries to float to top or sink to bottom
def byPriceAsc(fullList):

    for i in fullList:
        if i[6] == "N/A: Price Defined by Buyer":
            i[6] = 0.00 # let prices the buyer can define float to the top                                                    
        if i[6] == "N/A: Price not Defined": 
            i[6] = 999999 # let undefined prices sink to bottom
            
    orderedList = sorted(fullList, key=lambda entry:round(float(entry[6]),2))

    for i in orderedList:
        if i[6] == 0.00:
            i[6] = "N/A: Price Defined by Buyer" # switch back for proper display                                            
        if i[6] == 999999:
            i[6] = "N/A: Price not Defined" 

    return orderedList

# Sorts list by price in descending order
# Will replace placeholder text with numerical values to allow entries to float to top or sink to bottom
def byPriceDes(fullList):
    for i in fullList:
        if i[6] == "N/A: Price Defined by Buyer":
            i[6] = 0.00 # let prices the buyer can define float to the top                                                    
        if i[6] == "N/A: Price not Defined": 
            i[6] = 999999 # let undefined prices sink to bottom
            
    orderedList = sorted(fullList, key=lambda entry: round(float(entry[6]),2), reverse=True)

    for i in orderedList:
        if i[6] == 0.00:
            i[6] = "N/A: Price Defined by Buyer" # switch back for proper display                                           
        if i[6] == 999999:
            i[6] = "N/A: Price not Defined"

    return orderedList

# Sorts list by date in ascending order
def byDateAsc(fullList):

    datedList = fullList
    undatedList = []
    
    for i in datedList:
        if "TBA" in str(i[4]) or "N/A" in str(i[4]):
            undatedList.append(i)

    for i in undatedList:
        datedList.remove(i)
    
    orderedList = sorted(datedList, key=lambda entry: entry[4])

    for i in undatedList:
        orderedList.append(i)
    
    return orderedList

# Sorts list by date in descending order
def byDateDes(fullList):
   orderedList = sorted(fullList, key=lambda entry: entry[4],reverse=True)
   return orderedList

# Sorts list alphabetically in ascending order
def byAlphaEventAsc(fullList):
    orderedList = sorted(fullList, key=lambda entry: entry[1])
    return orderedList

# Sorts list alphabetically in descending order
def byAlphaEventDes(fullList):
    orderedList = sorted(fullList, key=lambda entry: entry[1],reverse=True)
    return orderedList

# Returns a new list based on entries within fullList that have prices within the priceRange
def priceRange(fullList,minP,maxP):
    orderedList = []

    for i in fullList:
        if i[6] != "N/A: Price Defined by Buyer" and i[6] != "N/A: Price not Defined":
            if i[6] >= minP and i[6] <= maxP:
                orderedList.append(i)
        else:
            orderedList.append(i)

    return orderedList

