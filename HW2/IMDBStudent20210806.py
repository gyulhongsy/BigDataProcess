#!/usr/bin/python3

genre = ""
genreDict = {}
fileName = input('파일 이름을 입력하시오 ')
fr = open(fileName, "rt")

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

fw = open("movieoutput.txt", "wt")
for item in genreDict:
    fw.write(str(item) +" "+ str(genreDict.get(item)))
    fw.write("\n")
fw.close()