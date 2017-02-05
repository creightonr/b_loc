import json
import requests
import csv
import pprint
import time

city = 'lametro'

stinfo = 'https://gbfs.bcycle.com/bcycle_%s/station_information.json' % (city)
avinfo = 'https://gbfs.bcycle.com/bcycle_%s/station_status.json' % (city)
stdata = requests.get(stinfo)
stationdata = json.loads(stdata.text)
avdata = requests.get(avinfo)
availabilitydata = json.loads(avdata.text)

stations = stationdata["data"]["stations"]
av = availabilitydata["data"]["stations"]

numst = int(len(stations))
i = 0
tick = 0

outputFile = open('output.csv', 'w')
writer = csv.writer(outputFile, lineterminator = '\n')
writer.writerow(['address', 'latitude', 'longitude'])

while i < numst:
    writer.writerow([stations[i]["address"], stations[i]["lat"], stations[i]["lon"]])
    i = i + 1

outputFile.close()
inputFile = open('output.csv', 'r')
reader = csv.reader(inputFile)
redata = list(reader)
inputFile.close()
matrix = [('address', 'latitude', 'longitude')]

while tick < 10:
    i = 1
    outputFile = open('output.csv', 'w')
    writer = csv.writer(outputFile, lineterminator = '\n')
    
    while i < numst:
        row = redata[i]
        row.append(av[i]["num_bikes_available"])
        row.append(av[i]["num_docks_available"])
        matrix.append(row)
        i = i + 1
        
    time.sleep(60)
    tick = tick + 1
    writer.writerows(matrix)

outputFile.close()

#{"ttl":60,
# "data":    {"stations":[{"lon":-118.25905,
#                          "lat":34.04855,
#                          "address":"723 Flower Street",
#                          "name":"Flower & 7th",
#                          "station_id":"bcycle_lametro_3005"},
#
#                         {"lon":-118.25667,
#                          "lat":34.04554,
#                          "address":"729 S Olive Street",                          "name":"Olive & 
