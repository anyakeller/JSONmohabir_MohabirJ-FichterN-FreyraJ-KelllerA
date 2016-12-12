# Compilation of Master Sorted Lists Module

import sorts,ticketleap,ticketmaster,seatgeek

def byPriceAsc(query):

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = sorts.byPriceAsc(fullList)

    return fullList


def byPriceDes(query):

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = sorts.byPriceDes(fullList)

    return fullList


def byDateAsc(query):

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = sorts.byDateAsc(fullList)

    return fullList


def byDateDes(query):

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = sorts.byDateDes(fullList)

    return fullList


def byAlphaEventAsc(query):

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = sorts.byAlphaEventAsc(fullList)

    return fullList


def byAlphaEventDes(query):

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = sorts.byAlphaEventDes(fullList)

    return fullList


def byPriceRange(query,minP,maxP):

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = sorts.priceRange(fullList,minP,maxP)

    return fullList

## Testing ##

# def main():
#     listF = byPriceRange("music",100,300)

#     for i in listF:
#         print(i[6])

# main()
