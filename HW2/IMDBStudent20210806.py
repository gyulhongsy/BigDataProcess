#!/usr/bin/python3

import sys

genre = ""
genreDict = {}
inFile = sys.argv[1]
outFile = sys.argv[2]

fr = open(inFile, "rt")

for line in fr:
    info = line.split("::")
    genre = info[2]
    genreList = genre.split("|")
    for name in genreList:
        name = name.strip()
        if name not in genreDict:
            genreDict[name] = 1
        else:
            genreDict[name] += 1
fr.close()

fw = open(outFile, "wt")
for item in genreDict:
    fw.write(str(item) +" "+ str(genreDict.get(item)))
    fw.write("\n")
fw.close()