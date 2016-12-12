# Compilation of Master Sorted Lists Module

import sorts,ticketleap,ticketmaster,seatgeek

def byPriceAsc(query,minP,maxP):

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = sorts.byPriceAsc(fullList)

    return sorts.priceRange(fullList,minP,maxP)


def byPriceDes(query,minP,maxP):

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = sorts.byPriceDes(fullList)

    return sorts.priceRange(fullList,minP,maxP)


def byDateAsc(query,minP,maxP):

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = sorts.byDateAsc(fullList)

    return sorts.priceRange(fullList,minP,maxP)


def byDateDes(query,minP,maxP):

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = sorts.byDateDes(fullList)

    return sorts.priceRange(fullList,minP,maxP)


def byAlphaEventAsc(query,minP,maxP):

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = sorts.byAlphaEventAsc(fullList)

    return sorts.priceRange(fullList,minP,maxP)


def byAlphaEventDes(query,minP,maxP):

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = sorts.byAlphaEventDes(fullList)

    return sorts.priceRange(fullList,minP,maxP)

## Testing ##

def main():
    listF = byPriceAsc("music",0,900)

    for i in listF:
        print(i[6])

main()
