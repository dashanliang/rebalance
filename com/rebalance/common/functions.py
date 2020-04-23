from itertools import combinations, permutations
import numpy as np
from scipy import optimize
from itertools import product


def getCutParts(a, b):
    retParts = []
    cutParts = list(combinations(np.arange(1, a), b))
    for part in cutParts:
        retParts.append(changeToData(a, part))
    return retParts


def changeToData(org, part=()):
    datas = []
    cutPart = 0
    for index, data in enumerate(part):
        if index == 0:
            datas.append(data)
            cutPart = cutPart + int(data)
        else:
            cutData = data - part[index - 1]
            datas.append(cutData)
            cutPart = cutPart + int(cutData)
    datas.append(org - cutPart)
    return datas


# print(getCutParts(6, 3))
# simple filter the data


# got the best funcion
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

goalListLevel2 = ANZ_IN[0] + CC_IN[0] + SCBHK_IN[0] + SCBSG_IN[0] + DBHK_IN[0] + DBSHK_IN[0]

def getinequality(in_data = [x11], out_data = [x11], allNode = [x11]):
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


# 对于anz cc 等 生成对应的 不等式
anz = getinequality(ANZ_IN[0], ANZ_OUT[0], goalListLevel1)

cc = getinequality(CC_IN[0], CC_OUT[0], goalListLevel1)

scbhk = getinequality(SCBHK_IN[0], SCBHK_OUT[0], goalListLevel1)

scbsg = getinequality(SCBSG_IN[0], SCBSG_OUT[0], goalListLevel1)

dbhk = getinequality(DBHK_IN[0], DBHK_OUT[0], goalListLevel1)

dbshk = getinequality(DBSHK_IN[0], DBSHK_OUT[0], goalListLevel1)

a = np.array([anz, cc, scbhk, scbsg, dbhk, dbshk])
print(a)
b = np.array([-20, -20, -20, 1000, -50, 500])

print(b)
print(goalopt)
res = optimize.linprog(goalopt, A_ub=-a, b_ub=b, bounds=((0.1, None), (0.1, None), (0.1, None), (0.1, None), (0.1, None)))

print(res)

# 如果 level全集 加入可以 rebalance 从 1 1 1 1 1 1 开始 选取 最优
# level 1 路径生成器
# 每组要1个

def generateAllNeedAdd():
    # return np.arange(5, len(goalList), 1)
    return np.arange(1, len(goalListLevel1) + 1 -5, 1)
# get


def getMhs(mhindex = 0, level = 2):
    return [1, 2, 3]

def getMhAllValite(paths = [], needPart = 0):
    nodeLen = len(paths)
    alldata = list(combinations(np.arange(1, len(paths) + 1), needPart))
    allValite = []
    for node in alldata:
        tmpNode = np.zeros(nodeLen, dtype= int)
        for tmp in node:
            tmpNode[tmp-1] = 1
        allValite.append(tmpNode)
    return allValite



def descartes(firstdata = [], senddata = []):
    data = []
    for x in product(firstdata, senddata):
        data.append(list(x))
    return data

def filterAndCheck(data = [[[]]], mhs = []):
    dataRet = []
    for eachMhs in data:
        if len(data) == 1 :
            dataRet = eachMhs
            return dataRet
        if len(list(dataRet)) == 0:
            dataRet = eachMhs
            continue
        datatmp = []
        datatmp.extend(eachMhs)
        dataRet = descartes(dataRet, datatmp)

    realData = []
    for dataeach in dataRet:
        tmp = dataeach
        retData = []
        for i in np.arange(0, len(mhs) -1, 1):
            retData.append(tmp[1])
            tmp = tmp.pop(0)
            if type(tmp[0]).__name__ != 'list':
                retData.append(tmp)
        rightdata = []
        for empData in retData:
            rightdata.insert(0, empData)
        realData.append(rightdata)
    return realData

def getAllNeed(tmpNeedMhs = [[]], tmpPart = [], level = 2):
    goodPath = []
    for needMhs in tmpNeedMhs:
        i = 0
        candidateAllTmp = []
        goodones = []
        for mh in needMhs:
            candaditePaths = getMhs(mh, level)
            candidateAllTmp.append(getMhAllValite(candaditePaths, tmpPart[i]))
            if (len(candidateAllTmp) == len(needMhs)):
                goodones = filterAndCheck(candidateAllTmp, needMhs)
            i = i+1
        goodPath.extend(goodones)
    return goodPath

def getMhSize():
    return 6

# add level 2, get at least nodes
def add2isokGetLeastPaths(addNumber = 1, level1AllNodes = [x11]):
    if(addNumber <= 0 ):
        return []

    canCutNode = np.arange(0, addNumber, 1)
    tmpAll = []
    for i in canCutNode:
        tmpParts = getCutParts(addNumber, i)
        for tmpPart in tmpParts:
            needmhs = len(tmpPart)
            tmpNeedMhs = list(combinations(np.arange(0, 6), needmhs))
            tmp = getAllNeed(tmpNeedMhs, tmpPart)
            if len(tmp) > 0:
               tmpAll.extend(tmp)
        if len(tmpAll) >0 :
            break

    return tmpAll

print(add2isokGetLeastPaths(1))




