from com.rebalance.common.main import *


def calculateMaxLevel2():
    return []

def calculateMaxLevel1():
    return []

def calculateMaxLevel0():
    return []

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

