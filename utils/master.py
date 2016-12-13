# Compilation of Master Sorted Lists Module

import utils.sorts,utils.ticketleap,utils.ticketmaster,utils.seatgeek

def byPriceAsc(query,minP,maxP):

    leapList = utils.ticketleap.ticketleap(query)
    masterList = utils.ticketmaster.ticketmaster(query)
    geekList = utils.seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = utils.sorts.byPriceAsc(fullList)

    return utils.sorts.priceRange(fullList,minP,maxP)


def byPriceDes(query,minP,maxP):

    leapList = utils.ticketleap.ticketleap(query)
    masterList = utils.ticketmaster.ticketmaster(query)
    geekList = utils.seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = utils.sorts.byPriceDes(fullList)

    return utils.sorts.priceRange(fullList,minP,maxP)


def byDateAsc(query,minP,maxP):

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = utils.leapList + masterList + geekList

    fullList = utils.sorts.byDateAsc(fullList)

    return utils.sorts.priceRange(fullList,minP,maxP)


def byDateDes(query,minP,maxP):

    leapList = utils.ticketleap.ticketleap(query)
    masterList = utils.ticketmaster.ticketmaster(query)
    geekList = utils.seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = utils.sorts.byDateDes(fullList)

    return utils.sorts.priceRange(fullList,minP,maxP)


def byAlphaEventAsc(query,minP,maxP):

    leapList = utils.ticketleap.ticketleap(query)
    masterList = utils.ticketmaster.ticketmaster(query)
    geekList = utils.seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = utils.sorts.byAlphaEventAsc(fullList)

    return utils.sorts.priceRange(fullList,minP,maxP)


def byAlphaEventDes(query,minP,maxP):

    leapList = utils.ticketleap.ticketleap(query)
    masterList = utils.ticketmaster.ticketmaster(query)
    geekList = utils.seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    fullList = utils.sorts.byAlphaEventDes(fullList)

    return utils.sorts.priceRange(fullList,minP,maxP)

## Testing ##

def main():
    listF = byPriceAsc("music",0,900)

    for i in listF:
        print(i[6])

main()
