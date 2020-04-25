from itertools import combinations, permutations
import numpy as np
from itertools import product

def generalListSequence(lenAll = 0, lenNeed = 0):
    if lenAll >= 0:
        if lenNeed == 0:
            return [np.zeros(lenAll, dtype= np.int)]
    if lenAll < lenNeed or lenAll <= 0 or  lenNeed <= 0 :
        return
    indexNeed = list(combinations(np.arange(0, lenAll), lenNeed))
    retData = []
    for indexNodes in indexNeed:
        eachAllNode = np.zeros(lenAll, dtype= np.int)
        for indeNode in indexNodes:
            eachAllNode[indeNode] = 1
        retData.append(eachAllNode)
    return retData


def descartes(firstdata = [], seconddata = []):
    data = []
    for x in product(firstdata, seconddata):
        data.append(list(x))
    return data


def filterAndCheckForOnePiece(data = [[[]]]):
    dataRet = []
    lenData = len(data)
    for eachindex, eamhs in enumerate(data):
        if eachindex == 0:
            dataRet = eamhs
            continue
        dataRet = descartes(dataRet, eamhs)

    realData = []
    for dataeach in dataRet:
        tmp = dataeach
        retData = []
        if lenData == 1:
            retData.append(dataeach)
        if lenData == 2 :
            retData.extend(dataeach[0])
            retData.append(dataeach[1])
        for i in np.arange(0, lenData - 2, 1):
            retData.append(tmp[1])
            tmp = tmp.pop(0)
            if i == (lenData - 3):
                retData.append(tmp[1])
                retData.append(tmp[0])
        rightdata = []
        if lenData > 2:
            for empData in retData:
                rightdata.insert(0, empData)
        else:
            rightdata = retData
        realData.append(rightdata)
    return realData

# print(filterAndCheckForOnePiece([generalListSequence(5, 1)]))

def generalProrityLevel(levelSum = 4):
    prorityLevels = []
    for i in np.arange(0, levelSum, 1):
        prorityLevels.append(np.arange(0, i+1, 1))
    return prorityLevels

def getLevelPathLen(indexmh = 0):
    return 5

def generalLevelMaxSequenceAtLeast(levelData = 0, atleastMaxLen = 1, otherData = []):
    maxIndexLevel = levelData
#     get static data
    lowleveldata = []
    if maxIndexLevel > 0 :
        statisData = []
        for i in np.arange(0, maxIndexLevel, 1):
            statisData.append(np.ones(getLevelPathLen(i), dtype=np.int))
        lowleveldata.append(statisData)
    highleveldata = generalListSequence(getLevelPathLen(maxIndexLevel), atleastMaxLen)

    needGeneralData = []
    if len(lowleveldata) > 0:
       needGeneralData.append(lowleveldata)
    needGeneralData.append(highleveldata)
    needGeneralData.extend(otherData)
    return filterAndCheckForOnePiece(needGeneralData)

print(generalLevelMaxSequenceAtLeast(0, 1))



