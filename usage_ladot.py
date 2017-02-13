import csv
import time, datetime
import os

datestamp = datetime.datetime.now()
os.chdir('ladot%s' % datestamp.strftime('%Y-%m-%d'))
outputFile = open('minute.csv', 'w')
writer = csv.writer(outputFile, lineterminator = '\n')
writer.writerow(['hour', 'minute', 'bikes in', 'bikes out'])
numst = 60
hour = 0
startTime = time.time()

# read all hourly files in a given day, each containing bike and dock counts on a minute-by-minute basis

while hour < 24:
    inputFile = open('output%s.csv' % (hour))
    reader = csv.reader(inputFile)
    redata = list(reader)
    minute = 3

    while minute < 121:
        nav = 0
        incount = 0
        outcount = 0

        station = 0
        while station < numst:
            if int(redata[station][minute + 2]) > int(redata[station][minute]):
                incount = incount + int(redata[station][minute + 2]) - int(redata[station][minute])
            if int(redata[station][minute + 2]) < int(redata[station][minute]):
                outcount = outcount + int(redata[station][minute]) - int(redata[station][int(minute) + 2])
            station = station + 1
                
        writer.writerow([hour, (minute - 3)/2, incount, outcount])
        minute = minute + 2

    hour = hour + 1

outputFile.close()
totalTime = round(time.time() - startTime, 2)
print totalTime
