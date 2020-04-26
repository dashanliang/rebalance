from com.rebalance.common.main import *


def calculateMaxLevel2():
    return []

def calculateMaxLevel1():
    tmpPaths = []
    for i in np.arange(0, np.sum(goalListLevelINLen1), 1):
        best = generalalldata(generalItemsForEachLevel(1, i + 1), 1)
        print(best)
        if best != None:
            tmpPaths = best
            break
    tmpAllCandidate = []
    for paths in tmpPaths:
        tmpAllCandidate.append([paths[1:]])

    print(tmpAllCandidate)

    for i in np.arange(0, np.sum(goalListLevelINLen) + 1, 1):
        tmpdata = []
        tmpdata = generalItemsForEachLevel(0, i)
        tmpdata.extend(tmpAllCandidate)
        best = generalalldata(tmpdata, 1)
        print(best)
        if best != None:
            tmpPaths = best
            print("best is :", best)
            break
    return []

def calculateMaxLevel0(level = 0):
    best = [[]]
    for i in np.arange(0, np.sum(goalListLevelINLen), 1):
        best = generalalldata(generalItemsForEachLevel(level, i + 1))
        print(best)
        if best != None:
            break
    return best[0]

def controllerMaxLevel(maxLevel = 0):
    atleastLevel = checkLeastLevel(maxLevel)
    if atleastLevel == None:
        return
    if atleastLevel == 0:
        return calculateMaxLevel0()

    if atleastLevel == 1:
        return calculateMaxLevel1()

    if atleastLevel >= 2:
        return calculateMaxLevel2()

