#!/usr/bin/python3

import sys
from datetime import datetime

inFile = sys.argv[1]
outFile = sys.argv[2]
dayDict = {0:"MON", 1:"TUE", 2:"WED", 3:"THU", 4:"FRI", 5:"SAT", 6:"SUN"}
region, date, day, vehicles, trips = "", "", "", "", ""
uberDict = {}

fr = open(inFile, "rt")
for line in fr:
    info = line.split(",")
    region, date, vehicles, trips = info
    date_obj = datetime.strptime(date, '%m/%d/%Y')
    day = dayDict[date_obj.weekday()]
    key = region +","+ day
    if key not in uberDict:
        uberDict[key] = [int(vehicles), int(trips)]
    else:
        uberDict[key][0] += int(vehicles)
        uberDict[key][1] += int(trips)
fr.close()

fw = open(outFile, "wt")
for item in uberDict:
    fw.write(str(item) +" "+ str(uberDict.get(item)[0]) +","+ str(uberDict.get(item)[1]))
    fw.write("\n")
fw.close()