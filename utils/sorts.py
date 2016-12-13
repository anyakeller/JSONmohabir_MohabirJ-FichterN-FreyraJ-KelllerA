# Sorting Query module

def byPriceAsc(fullList):

    for i in fullList:
        if i[6] == "N/A: Price Defined by Buyer":
            i[6] = 0.00 # let prices the buyer can define float to the top                                                    
        if i[6] == "N/A: Price not Defined": 
            i[6] = 999999
            
    orderedList = sorted(fullList, key=lambda entry:round(float(entry[6]),2))

    for i in orderedList:
        if i[6] == 0.00:
            i[6] = "N/A: Price Defined by Buyer" # switch back for proper display                                            
        if i[6] == 999999:
            i[6] = "N/A: Price not Defined" 

    return orderedList

def byPriceDes(fullList):
    for i in fullList:
        if i[6] == "N/A: Price Defined by Buyer":
            i[6] = 0.00 # let prices the buyer can define float to the top                                                    
        if i[6] == "N/A: Price not Defined": 
            i[6] = 999999
            
    orderedList = sorted(fullList, key=lambda entry: round(float(entry[6]),2), reverse=True)

    for i in orderedList:
        if i[6] == 0.00:
            i[6] = "N/A: Price Defined by Buyer" # switch back for proper display                                           
        if i[6] == 999999:
            i[6] = "N/A: Price not Defined"

    return orderedList

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

def byDateDes(fullList):
   orderedList = sorted(fullList, key=lambda entry: entry[4],reverse=True)
   return orderedList

def byAlphaEventAsc(fullList):
    orderedList = sorted(fullList, key=lambda entry: entry[1])
    return orderedList

def byAlphaEventDes(fullList):
    orderedList = sorted(fullList, key=lambda entry: entry[1],reverse=True)
    return orderedList

def priceRange(fullList,minP,maxP):
    orderedList = []

    for i in fullList:
        if i[6] != "N/A: Price Defined by Buyer":
            if i[6] >= minP and i[6] <= maxP:
                orderedList.append(i)
        else:
            orderedList.append(i)

    return orderedList

