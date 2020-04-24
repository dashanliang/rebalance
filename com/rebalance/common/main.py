from itertools import combinations, permutations
import numpy as np
from itertools import product
from com.rebalance.common.corefuntion import *

MaxLevel = 3

def getlevelLen(i):
    return 2

def getinequality(in_data = [], out_data = [], allNode = []):
    inequalityData = np.zeros(len(allNode), dtype= np.int)
    for mh in in_data :
        for index, mh_node in enumerate(allNode):
            if mh.__name__ == mh_node.__name__ :
                inequalityData[index] = 1
                break

    for mh in out_data :
        for index, mh_node in enumerate(allNode):
            if mh.__name__ == mh_node.__name__ :
                inequalityData[index] = -1
                break

    return inequalityData

def checkoptimizeisok(allNodes = []):
    return True

def checkLeastLevel():
    sumLen = 0
    for i in np.arange(0, MaxLevel, 1):
        sumLen = sumLen + getlevelLen(i)
        tmpNodes = np.ones(sumLen, dtype=np.int)
        if checkoptimizeisok(tmpNodes) == True:
            return i
            break
    return

tmpAllCandidate = []

def generalItemsForEachLevel(level = 0, maxatleast = 0):
    leveldata = []
    allCandidata = []
    if len(tmpAllCandidate) > 0:
        for candidate in tmpAllCandidate:
            allCandidata.insert(0, candidate)

    data = generalLevelMaxSequenceAtLeast(level, maxatleast, allCandidata)
    for eachdata in data:
        leveldata.append(eachdata[level])

    tmpAllCandidate.insert(0, leveldata)
    return leveldata

def canRebalanceOrNot(datas = [[]]):
    checkdate = []
    for data in datas:
        checkdate.extend(data)
    # need add funtion to linear
    return True

def filterCanRebalance(candidates= [[[]]]):
    realResult = []
    for cadidate in candidates:
        if canRebalanceOrNot(cadidate) == True:
            realResult.append(cadidate)
    return realResult

def getmhlen(level = 1):
    datamh = [1,1,0,2,2]
    return datamh

def calnodedata(level = 0, node = []):
    datatmp = []
    tmplens = getmhlen(level)
    alllen = []
    lens = 0
    for tmplen in tmplens:
        if tmplen == 0:
            datatmp.append([])
            continue
        datatmp.append(node[lens:lens + tmplen])
        lens = lens + tmplen

    for data in datatmp:
        alllen.append(np.sum(data, axis=0, dtype= int))

    return alllen


def calculateTheHighPrority(datas = [[[]]]):
    biasData = []

    for data in datas:
        tmpdata = []
        for level, node in enumerate(data):
            if tmpdata == [] :
                tmpdata = calnodedata(level, node)
                continue
            tmpdata = np.add(tmpdata, calnodedata(level, node))

        biasData.append(np.dot(tmpdata, tmpdata))

    return biasData

print(calculateTheHighPrority([[[1,1,1,1,1,1]]]))
def generalalldata():
    allCandidata = []
    if len(tmpAllCandidate) > 0:
        for candidate in tmpAllCandidate:
            allCandidata.insert(0, candidate)
    canBeSuccessdata = filterAndCheckForOnePiece(allCandidata)
#     filter one by one cal  and the 倾向性
    realCandidate = filterCanRebalance(canBeSuccessdata)
    calBias = calculateTheHighPrority(realCandidate)

#     choice the best is well


data = []
date1 = [1,2,3]
data = np.add(date1, date1)
print(np.dot(date1, date1))
print(date1[0:1])





