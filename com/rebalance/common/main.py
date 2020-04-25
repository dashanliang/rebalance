from itertools import combinations, permutations
import numpy as np
from itertools import product
from com.rebalance.common.corefuntion import *
import numpy as np
from scipy import optimize
from itertools import product

MaxLevel = 3

def getlevelLen(i):
    return np.sum(goalListLevelINLen)

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
    return linearCalcute(0, allNodes)

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
ANZ_OUT = [[x4, x5], [x8, x10], []]
ANZ_BALANCE = 0

CC_IN = [[x4], [], []]
CC_OUT = [[], [], []]
CC_BALANCE = 0

SCBHK_IN = [[x5], [x6], []]
SCBHK_OUT = [[x7], [], [x3]]
SCBHK_BALANCE = 0

SCBSG_IN = [[x7], [x8], []]
SCBSG_OUT = [[x1], [x6], []]
SCBSG_BALANCE = 1000
SCBSG_NEED = 0

DBHK_IN = [[x9], [x10], []]
DBHK_OUT = [[], [], []]
DBHK_BALANCE = 0

DBSHK_IN = [[], [], []]
DBSHK_OUT = [[x9], [x2], []]
DBSHK_BALANCE = 500
DBSHK_NEED = 0

# check level one is ok or not
goal1 = len(ANZ_IN[0]) + len(CC_IN[0]) + len(SCBHK_IN[0]) + len(SCBSG_IN[0]) + len(DBHK_IN[0]) + len(DBSHK_IN[0])

goalopt = np.ones(goal1 ,dtype = np.int)

goalListLevel1 = ANZ_IN[0] + CC_IN[0] + SCBHK_IN[0] + SCBSG_IN[0] + DBHK_IN[0] + DBSHK_IN[0]
print(len(goalListLevel1))
goalListLevelIN = []
goalListLevelIN.append(ANZ_IN[0])
goalListLevelIN.append(CC_IN[0])
goalListLevelIN.append(SCBHK_IN[0])
goalListLevelIN.append(SCBSG_IN[0])
goalListLevelIN.append(DBHK_IN[0])
goalListLevelIN.append(DBSHK_IN[0])

goalListLevelINLen = []
goalListLevelINLen.append(len(ANZ_IN[0]))
goalListLevelINLen.append(len(CC_IN[0]))
goalListLevelINLen.append(len(SCBHK_IN[0]))
goalListLevelINLen.append(len(SCBSG_IN[0]))
goalListLevelINLen.append(len(DBHK_IN[0]))
goalListLevelINLen.append(len(DBSHK_IN[0]))

def linearCalcute(maxlevel = 0, goalalldata = []):
    anz = getinequality(ANZ_IN[0], ANZ_OUT[0], goalListLevel1)

    cc = getinequality(CC_IN[0], CC_OUT[0], goalListLevel1)

    scbhk = getinequality(SCBHK_IN[0], SCBHK_OUT[0], goalListLevel1)

    scbsg = getinequality(SCBSG_IN[0], SCBSG_OUT[0], goalListLevel1)

    dbhk = getinequality(DBHK_IN[0], DBHK_OUT[0], goalListLevel1)

    dbshk = getinequality(DBSHK_IN[0], DBSHK_OUT[0], goalListLevel1)

    a = np.array([np.multiply(anz, goalalldata), np.multiply(cc, goalalldata),
                  np.multiply(scbhk, goalalldata), np.multiply(scbsg, goalalldata),
                  np.multiply(dbhk, goalalldata), np.multiply(dbshk, goalalldata)])
    print(a)
    b = np.array([-20, -20, -20, 1000, -50, 500])

    print(b)
    print(goalopt)
    res = optimize.linprog(goalopt, A_ub=-a, b_ub=b,
                           bounds=((0.1, None), (0.1, None), (0.1, None), (0.1, None), (0.1, None)))

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
print(tmpAllCandidate)
for i in np.arange(0, len(goalListLevelIN), 1):
    best = generalalldata(generalItemsForEachLevel(1,0))
    print(best)
    if best != None:
        break



