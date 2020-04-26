from itertools import combinations, permutations
import numpy as np
from itertools import product
# from com.rebalance.common.corefuntion import *
import numpy as np
from scipy import optimize
from itertools import product

MaxLevel = 3

def getlevelLen(i):
    if i == 0:
        return np.sum(goalListLevelINLen)
    return np.sum(goalListLevelINLen1)

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

def checkoptimizeisok(level = 0, allNodes = []):
    return linearCalcute(level, allNodes)

def checkLeastLevel():
    sumLen = 0
    for i in np.arange(0, MaxLevel, 1):
        sumLen = sumLen + getlevelLen(i)
        tmpNodes = np.ones(sumLen, dtype=np.int)
        if checkoptimizeisok(i, tmpNodes) == True:
            return i
            break
    return

tmpAllCandidate = []

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

def getLevelPathLen(indexmh = 0):
    if indexmh == 0:
        return len(goalListLevel1)
    return len(goalListLevel2)

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

def generalItemsForEachLevel(level = 0, maxatleast = 0):
    leveldata = []
    allCandidata = []
    # if len(tmpAllCandidate) > 0:
    #     for candidate in tmpAllCandidate:
    #         allCandidata.insert(0, candidate)
    #
    # data = generalLevelMaxSequenceAtLeast(level, maxatleast, allCandidata)

    tmpAllCandidate = []
    data = generalLevelMaxSequenceAtLeast(level, maxatleast)
    # for eachdata in data:
    #     leveldata.append(eachdata)

    tmpAllCandidate.insert(0, data)
    return tmpAllCandidate

# check need level 2 / level 3 or not
class x1:
    value = 0.0

class x2:
    value = 0.0

class x3:
    value = 0.0

class x4:
    value = 0.0

class x5:
    value = 0.0

class x6:
    value = 0.0

class x7:
    value = 0.0

class x8:
    value = 0.0

class x9:
    value = 0.0

class x10:
    value = 0.0

class x11:
    value = 0.0

class x12:
    value = 0.0

# analysis all mh details
ANZ_IN = [[x1], [x2], [x3]]
ANZ_OUT = [[x5], [x4, x8, x10], []]
ANZ_BALANCE = 0
ANZ_NEED = 20

CC_IN = [[], [x4], []]
CC_OUT = [[], [], []]
CC_BALANCE = 0
CC_NEED = 20

SCBHK_IN = [[x5], [x6], []]
SCBHK_OUT = [[x7], [], [x3]]
SCBHK_BALANCE = 0
SCBHK_NEED = 20

SCBSG_IN = [[x7], [x8], []]
SCBSG_OUT = [[x1], [x6], []]
SCBSG_BALANCE = 1000
SCBSG_NEED = 0

DBHK_IN = [[x9], [x10], []]
DBHK_OUT = [[], [], []]
DBHK_BALANCE = 0
DBHK_NEED = 50

DBSHK_IN = [[], [], []]
DBSHK_OUT = [[x9], [x2], []]
DBSHK_BALANCE = 500
DBSHK_NEED = 0

# check level one is ok or not
goal1 = len(ANZ_IN[0]) + len(CC_IN[0]) + len(SCBHK_IN[0]) + len(SCBSG_IN[0]) + len(DBHK_IN[0]) + len(DBSHK_IN[0])

goalopt = np.ones(goal1 ,dtype = np.int)

goalListLevel1 = ANZ_IN[0] + CC_IN[0] + SCBHK_IN[0] + SCBSG_IN[0] + DBHK_IN[0] + DBSHK_IN[0]
goalListLevel2 = ANZ_IN[1] + CC_IN[1] + SCBHK_IN[1] + SCBSG_IN[1] + DBHK_IN[1] + DBSHK_IN[1]
print(len(goalListLevel1))
goalListLevelIN = []
goalListLevelIN.append(ANZ_IN[0])
goalListLevelIN.append(CC_IN[0])
goalListLevelIN.append(SCBHK_IN[0])
goalListLevelIN.append(SCBSG_IN[0])
goalListLevelIN.append(DBHK_IN[0])
goalListLevelIN.append(DBSHK_IN[0])
goalListLevelIN1 = []
goalListLevelIN1.append(ANZ_IN[1])
goalListLevelIN1.append(CC_IN[1])
goalListLevelIN1.append(SCBHK_IN[1])
goalListLevelIN1.append(SCBSG_IN[1])
goalListLevelIN1.append(DBHK_IN[1])
goalListLevelIN1.append(DBSHK_IN[1])

goalListLevelINLen = []
goalListLevelINLen.append(len(ANZ_IN[0]))
goalListLevelINLen.append(len(CC_IN[0]))
goalListLevelINLen.append(len(SCBHK_IN[0]))
goalListLevelINLen.append(len(SCBSG_IN[0]))
goalListLevelINLen.append(len(DBHK_IN[0]))
goalListLevelINLen.append(len(DBSHK_IN[0]))

goalListLevelINLen1 = []
goalListLevelINLen1.append(len(ANZ_IN[1]))
goalListLevelINLen1.append(len(CC_IN[1]))
goalListLevelINLen1.append(len(SCBHK_IN[1]))
goalListLevelINLen1.append(len(SCBSG_IN[1]))
goalListLevelINLen1.append(len(DBHK_IN[1]))
goalListLevelINLen1.append(len(DBSHK_IN[1]))

def linearCalcute(maxlevel = 0, goalalldata = []):
    anz = getinequality(ANZ_IN[0], ANZ_OUT[0], goalListLevel1)

    cc = getinequality(CC_IN[0], CC_OUT[0], goalListLevel1)

    scbhk = getinequality(SCBHK_IN[0], SCBHK_OUT[0], goalListLevel1)

    scbsg = getinequality(SCBSG_IN[0], SCBSG_OUT[0], goalListLevel1)

    dbhk = getinequality(DBHK_IN[0], DBHK_OUT[0], goalListLevel1)

    dbshk = getinequality(DBSHK_IN[0], DBSHK_OUT[0], goalListLevel1)

    if maxlevel == 1:
        anz = getinequality(ANZ_IN[0] + ANZ_IN[1], ANZ_OUT[0] + ANZ_OUT[1], goalListLevel1 + goalListLevel2)

        cc = getinequality(CC_IN[0] + CC_IN[1], CC_OUT[0] + CC_OUT[1], goalListLevel1 + goalListLevel2)

        scbhk = getinequality(SCBHK_IN[0]+ SCBHK_IN[1], SCBHK_OUT[0] + SCBHK_OUT[1], goalListLevel1 + goalListLevel2)

        scbsg = getinequality(SCBSG_IN[0] + SCBSG_IN[1], SCBSG_OUT[0] + SCBSG_OUT[1], goalListLevel1 + goalListLevel2)

        dbhk = getinequality(DBHK_IN[0] + DBHK_IN[1], DBHK_OUT[0] + DBHK_OUT[1], goalListLevel1 + goalListLevel2)

        dbshk = getinequality(DBSHK_IN[0] + DBSHK_IN[1], DBSHK_OUT[0] + DBSHK_OUT[1], goalListLevel1 + goalListLevel2)

    a = np.array([np.multiply(anz, goalalldata), np.multiply(cc, goalalldata),
                  np.multiply(scbhk, goalalldata), np.multiply(scbsg, goalalldata),
                  np.multiply(dbhk, goalalldata), np.multiply(dbshk, goalalldata)])
    print(a)
    b = np.array([ANZ_BALANCE-ANZ_NEED,
                  CC_BALANCE-CC_NEED,
                 SCBHK_BALANCE-SCBHK_NEED,
                 SCBSG_BALANCE-SCBSG_NEED,
                 DBHK_BALANCE-DBHK_NEED,
                  DBSHK_BALANCE-DBSHK_NEED])

    print(b)
    boundsList = []
    for i in goalalldata:
        boundsList.append((0.1, None))

    res = optimize.linprog(goalalldata, A_ub=-a, b_ub=b,
                           bounds=tuple(boundsList))

    print(res)
    print(goalalldata)
    return res.get("success")

def canRebalanceOrNot(datas = [[]]):
    checkdate = []
    i = 0
    for data in datas:
        # if type(data).__name__ != "int":
        #     checkdate.extend(data)
        # else:
        checkdate.extend(data)
        i = i + 1
    # need add funtion to linear
    if i > 0:
        return linearCalcute(i-1, checkdate)
    return False

def filterCanRebalance(candidates= [[[]]]):
    realResult = []
    for cadidate in candidates:
        if canRebalanceOrNot(cadidate) == True:
            realResult.append(cadidate)
    return realResult

def getmhlen(level = 1):
    datamh = goalListLevelINLen
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

# print(calculateTheHighPrority([[[1,1,1,1,1,1]]]))
def generalalldata(tmpAllCandidate = [[[]]]):
    allCandidata = []
    if len(tmpAllCandidate) > 0:
        for candidate in tmpAllCandidate:
            allCandidata.insert(0, candidate)
    if len(allCandidata) == 1:
        canBeSuccessdata = allCandidata[0]
    else:
        canBeSuccessdata = filterAndCheckForOnePiece(allCandidata)
#     filter one by one cal  and the 倾向性
    realCandidate = filterCanRebalance(canBeSuccessdata)
    calBias = []
    if len(realCandidate)>0:
        calBias = calculateTheHighPrority(realCandidate)

#     choice the best is well
    if calBias == []:
        return
    print(realCandidate)
    print(" best is : " , calBias)
    return np.argmax(calBias)

print(checkLeastLevel())
# print(tmpAllCandidate)
# for i in np.arange(0, len(goalListLevelIN), 1):
#     best = generalalldata(generalItemsForEachLevel(0,i+1))
#     print(best)
#     if best != None:
#         break

# needMaxLevel = checkLeastLevel()


