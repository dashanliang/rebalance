from com.rebalance.common.main import *


def calculateMaxLevel2():
    for i in np.arange(0, np.sum(goalListLevelINLen2), 1):
        best = generalalldata(generalItemsForEachLevel(2, i + 1), 2)
        print(best)
        if best != None:
            tmpPaths = best
            break

    tmpcandiae2 = []
    for paths in tmpPaths:
        tmpcandiae2.append(paths[2:])

    tmpAllCandidate = []
    tmpAllCandidate.append(tmpcandiae2)

    print(tmpAllCandidate)

    for i in np.arange(0, np.sum(goalListLevelINLen1) + 1, 1):
        tmpdata = []
        tmpdata = generalItemsForEachLevel(1, i)
        tmpdata.extend(tmpAllCandidate)
        best = generalalldata(tmpdata, 2)
        print(best)
        if best != None:
            tmpPaths = best
            print("best is :", best)
            break

    tmpAllCandidateFor1 = []
    for paths in tmpPaths:
        ttmp1 = []
        ttmp1.append(paths[1])
        ttmp1.extend(paths[2])
        tmpAllCandidateFor1.append(ttmp1)

    print([tmpAllCandidateFor1])

    for i in np.arange(0, np.sum(goalListLevelINLen) + 1, 1):
        tmpdata = []
        tmpdata = generalItemsForEachLevel(0, i)
        tmpdata.extend([tmpAllCandidateFor1])
        best = generalalldata(tmpdata, 2)
        print(best)
        if best != None:
            tmpPaths = best
            print("best is :", best)
            break

    forTmp2 = []

    for paths in tmpPaths:
        f2 = []
        f2.append(paths[0])
        f2.extend(paths[1])
        forTmp2.append(f2)

    print(forTmp2)
    bestpath = calculateTheHighPrority(forTmp2)


    return bestpath

def calculateMaxLevel1():
    tmpPaths = []
    for i in np.arange(0, np.sum(goalListLevelINLen1), 1):
        best = generalalldata(generalItemsForEachLevel(1, i + 1), 1)
        print(best)
        if best != None:
            tmpPaths = best
            break
    tmpAllCandidate = []
    tmpcandiae = []
    for paths in tmpPaths:
        tmpcandiae.append(paths[1:])
    tmpAllCandidate.append(tmpcandiae)

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

    forTmp1 = []
    for paths in tmpPaths:
        f1 = []
        f1.append(paths[0])
        f1.extend(paths[1])
        forTmp1.append(f1)

    bestPath = calculateTheHighPrority(forTmp1)
    return bestPath

def calculateMaxLevel0(level = 0):
    best = []
    for i in np.arange(0, np.sum(goalListLevelINLen), 1):
        best = generalalldata(generalItemsForEachLevel(level, i + 1))
        print(best)
        if best != None:
            break
    bestPath = calculateTheHighPrority(best)
    return bestPath

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

