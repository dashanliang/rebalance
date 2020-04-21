from itertools import combinations, permutations
import numpy as np
from scipy import optimize


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

goalList = ANZ_IN[0] + CC_IN[0] + SCBHK_IN[0] + SCBSG_IN[0] + DBHK_IN[0] + DBSHK_IN[0]

def getinequality(in_data = [x11], out_data = [x11]):
    inequalityData = np.zeros(len(goalList), dtype= np.int)
    for mh in in_data :
        for index, mh_node in enumerate(goalList):
            if mh.__name__ == mh_node.__name__ :
                inequalityData[index] = 1
                break

    for mh in out_data :
        for index, mh_node in enumerate(goalList):
            if mh.__name__ == mh_node.__name__ :
                inequalityData[index] = -1
                break

    return inequalityData


# 对于anz cc 等 生成对应的 不等式
anz = getinequality(ANZ_IN[0], ANZ_OUT[0])

cc = getinequality(CC_IN[0], CC_OUT[0])

scbhk = getinequality(SCBHK_IN[0], SCBHK_OUT[0])

scbsg = getinequality(SCBSG_IN[0], SCBSG_OUT[0])

dbhk = getinequality(DBHK_IN[0], DBHK_OUT[0])

dbshk = getinequality(DBSHK_IN[0], DBSHK_OUT[0])

a = np.array([anz, cc, scbhk, scbsg, dbhk, dbshk])
print(-a)
b = np.array([20, 20, 20, 0, 50, 0])

print(-b)
print(goalopt)
res = optimize.linprog(goalopt, A_ub=a, b_ub=b, bounds=((20, 1000), (20, 1500), (5, 1500), (50, 500), (50, 500)))

print(res)