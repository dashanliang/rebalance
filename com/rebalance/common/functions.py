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


print(getCutParts(6, 3))
# simple filter the data


# got the best funcion
# check need level 2 / level 3 or not
class x11:
    value = 0.0

class x21:
    value = 0.0

class x31:
    value = 0.0

class y11:
    value = 0.0

class z11:
    value = 0.0

class z21:
    value = 0.0

class k11:
    value = 0.0

class k21:
    value = 0.0

class p11:
    value = 0.0

class p21:
    value = 0.0

# x11 = x21 = x31 = y11 = z11 = z21 = k11 = k21 = p11 = p21 = 0.00
allVariableComeIn = [[[x11], [x21], [x31]], [[y11]], [[z11], [z21]], [[k11], [k21]], [[p11], [p21]]]
allVariableGoOut = [[[x11], [x21], [x31]], [[y11]], [[z11], [z21]], [[k11], [k21]], [[p11], [p21]]]


print(x11.value)

# objective function



# x11+ y11 + z11 + k11 + p11
# x11, y11, z11, k11, p11 >0
# x11 =< scbsg
# k11 + p11 =< scbhk
# y11 + z11 =< x11
# x11 -y11 - z11 >= anzbalance
# y11 = cc balance
# z11 - k11 -p11 >= scb balance
# k11 - x11 >= scbsg balance
# p11 >= dbhk balance
# 根据条件判断 对应的系数

