import pickle
import json
import numpy as np
import uuid


class mhdata:
    def __init__(self, mhName, balance, need):
        self.mhName = mhName
        self.balance = balance
        self.need = need

class data:
    def __init__(self, fromMh, toMh, level):
        self.fromMh = fromMh
        self.toMh = toMh
        self.level = level


def datatoclassData(d):
    return data(d['fromMh'], d['toMh'], d['level'])

def datatoclassMhdata(d):
    return mhdata(d['mhName'], d['balance'], d['need'])


testdata = '{\"fromMh\": \"a\", \"toMh\": \"b\", \"level\":\"0\"};{\"fromMh\": \"c\", \"toMh\": \"a\", \"level\":\"0\"}'
testmhdata = '{\"mhName\": \"a\", \"balance\": 50, \"need\": 100};{\"mhName\": \"b\", \"balance\": 100, \"need\": 0};{\"mhName\": \"c\", \"balance\": 100, \"need\": 0}'

mhdatas = []
mhnames = []
mhrebalance = []
mhoutdata = []
mhindata = []
markdata = []

def getmhdata(data1 = testmhdata):
    for eachnode in data1.split(";"):
        nodeclass = json.loads(eachnode, object_hook = datatoclassMhdata)
        mhnames.append(nodeclass.mhName)

def getmhdatabalance(data1 = testmhdata):
    for eachnode in data1.split(";"):
        mhbalance = []
        nodeclass = json.loads(eachnode, object_hook = datatoclassMhdata)
        mhbalance.append(nodeclass.balance)
        mhbalance.append(nodeclass.need)
        mhrebalance.append(mhbalance)
    return mhrebalance


def levelmax(maxlevel = 0):
    mhlen = len(mhnames)
    for i in np.arange(0, maxlevel, 1):
        mmhs = []
        for j in np.arange(0, mhlen, 1):
            mmhs.append([])
        mhoutdata.append(mmhs)
        mhindata.append(mmhs)
    return None


getmhdata(testmhdata)
print(mhnames)
levelmax(2)
print(mhoutdata)

def setdata(level = 0, frommh = "", tomh = "", markdata = "",  allindata = [[[]]], alloutdata = [[[]]]):
    tpdata = []
    mhoutindex = 0
    for indexout, name in enumerate(mhnames):
        if name == frommh:
            mhoutindex = indexout

    mhinindex = 0
    for indexin, name in enumerate(mhnames):
        if name == tomh:
            mhinindex = indexin
    alloutdata[level][mhoutindex].append(markdata)
    allindata[level][mhinindex].append(markdata)
    return None

def getdataOut(data = testdata, allindata = [[[]]], alloutdata = [[[]]]):
    i = 0
    tmpin = allindata
    tmpout = alloutdata
    for eachnode in data.split(";"):
        nodeclass = json.loads(eachnode, object_hook =datatoclassData)
        level = nodeclass.level
        frommh = nodeclass.fromMh
        toMh = nodeclass.toMh
        iduu = i
        setdata(level, frommh, toMh, iduu, allindata, alloutdata)
        markdata.append(iduu)
        i = i + 1
    return None

getdataOut(allindata= mhindata, alloutdata= mhoutdata)
print(mhindata)



