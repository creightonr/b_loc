import csv
import time, datetime
import os

startTime = time.time()
datestamp = datetime.datetime.now()
os.chdir('ladot%s' % datestamp.strftime('%Y-%m-%d'))
outputFile = open('summary.csv', 'w')
writer = csv.writer(outputFile, lineterminator = '\n')

inputFile = open('minute.csv')
reader = csv.reader(inputFile)
redata = list(reader)

hour = 0
header = ['hour']
bikesin = ['total bikes in']
bikesout = ['total bikes out']

while hour < 24:
    incount = 0
    outcount = 0
    minute = 1
    header.append(hour)

    while minute < 60:
        incount = incount + int(redata[(hour*59 + minute)][2])
        outcount = outcount + int(redata[(hour*59 + minute)][3])
                
        minute = minute + 1

    bikesin.append(incount)
    hour = hour + 1

writer.writerow(header)
writer.writerow(bikesin)

hour = 0
inputFile = open('output%s.csv' % (hour))
reader = csv.reader(inputFile)
redata = list(reader)
numst = len(redata)
station = 1

while station < numst:    
    loc = [redata[station][0]]

    while hour < 24:
        inputFile = open('output%s.csv' % (hour))
        reader = csv.reader(inputFile)
        redata = list(reader)
        numst = len(redata)
        minute = 3
        incount = 0
    
        while minute < 121: 
            if int(redata[station][minute + 2]) > int(redata[station][minute]):
                incount = incount + int(redata[station][minute + 2]) - int(redata[station][minute])
            minute = minute + 2

        loc.append(incount)
        hour = hour + 1

    writer.writerow(loc)
    station = station + 1
    hour = 0

outputFile.close()
totalTime = round(time.time() - startTime, 2)
print totalTime
