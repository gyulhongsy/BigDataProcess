#!/usr/bin/python3

genre = ""
genreDict = {}
fileName = input('파일 이름을 입력하시오 ')
f = open(fileName, "rt")

for line in f:
    info = line.split("::")
    genre = info[2]
    genreList = genre.split("|")
    for name in genreList:
        name = name.strip()
        if name not in genreDict:
            genreDict[name] = 1
        else:
            genreDict[name] += 1
f.close()

for item in genreDict:
    print(item, genreDict.get(item))