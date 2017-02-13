import csv
import time, datetime
import os

startTime = time.time()
datestamp = datetime.datetime.now()
os.chdir('ladot%s' % datestamp.strftime('%Y-%m-%d'))
outputFile = open('hour.csv', 'w')
writer = csv.writer(outputFile, lineterminator = '\n')

writer.writerow(['hour', 'bikes in', 'bikes out'])
inputFile = open('minute.csv')
reader = csv.reader(inputFile)
redata = list(reader)

hour = 0

while hour < 24:
    incount = 0
    outcount = 0
    minute = 1

    while minute < 60:
        incount = incount + int(redata[(hour*59 + minute)][2])
        outcount = outcount + int(redata[(hour*59 + minute)][3])
                
        minute = minute + 1

    writer.writerow([hour, incount, outcount])    
    hour = hour + 1

outputFile.close()
totalTime = round(time.time() - startTime, 2)
print totalTime
