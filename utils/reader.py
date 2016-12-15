import csv

def returnKey(apiName):
    with open('keys.csv', 'rb') as csvfile:
        keyreader = csv.reader(csvfile)

        for row in keyreader:
            if row[0] == apiName:
                return(row[1])

