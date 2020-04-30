import pickle
import json
import numpy as np
import uuid



# coding=utf-8
from copy import copy

import xlrd
from xlutils.copy import copy
import numpy as np
# from com.rebalance.common.globaldata import *

filename = '/Users/jinglan.liang/Downloads/demo3.xlsx'
def getMhdatabal():
    # 打开文件
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_name('Sheet1')

    tmpExceldata = ''

    for row in np.arange(1, 12 , 1):
        for col in np.arange(1, 12, 1):
            tmp = table.cell(row, col).value
            if tmp != '':
                if tmpExceldata == '':
                    tmpExceldata = json.dumps(dataforpath('mh' + str(row), 'mh' + str(col), tmp), default=lambda obj: obj.__dict__)
                else:
                    tmpExceldata = tmpExceldata + ";" + json.dumps(dataforpath('mh' + str(row), 'mh' + str(col), tmp), default=lambda obj: obj.__dict__)

    print(tmpExceldata)

    tmpExceldataForBal = ''

    for colForbal in np.arange(1, 12, 1):
        tmpbal = table.cell(12, colForbal).value
        if tmpbal != '':
            if tmpExceldataForBal == '':
                tmpExceldataForBal = json.dumps(mhdata('mh'+ str(colForbal), table.cell(12, colForbal).value, table.cell(13, colForbal).value),
                                          default=lambda obj: obj.__dict__)
            else:
                tmpExceldataForBal = tmpExceldataForBal + ";" + json.dumps(mhdata('mh'+ str(colForbal), table.cell(12, colForbal).value, table.cell(13, colForbal).value),
                                          default=lambda obj: obj.__dict__)

    print(tmpExceldataForBal)

    # testmhdata = tmpExceldataForBal
    # testdata = tmpExceldata
    return tmpExceldataForBal

def getMhdata():
    # 打开文件
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_name('Sheet1')

    tmpExceldata = ''

    for row in np.arange(1, 12 , 1):
        for col in np.arange(1, 12, 1):
            tmp = table.cell(row, col).value
            if tmp != '':
                if tmpExceldata == '':
                    tmpExceldata = json.dumps(dataforpath('mh' + str(row), 'mh' + str(col), tmp), default=lambda obj: obj.__dict__)
                else:
                    tmpExceldata = tmpExceldata + ";" + json.dumps(dataforpath('mh' + str(row), 'mh' + str(col), tmp), default=lambda obj: obj.__dict__)

    print(tmpExceldata)

    tmpExceldataForBal = ''

    for colForbal in np.arange(1, 12, 1):
        tmpbal = table.cell(12, colForbal).value
        if tmpbal != '':
            if tmpExceldataForBal == '':
                tmpExceldataForBal = json.dumps(mhdata('mh'+ str(colForbal), table.cell(12, colForbal).value, table.cell(13, colForbal).value),
                                          default=lambda obj: obj.__dict__)
            else:
                tmpExceldataForBal = tmpExceldataForBal + ";" + json.dumps(mhdata('mh'+ str(colForbal), table.cell(12, colForbal).value, table.cell(13, colForbal).value),
                                          default=lambda obj: obj.__dict__)

    print(tmpExceldataForBal)

    # testmhdata = tmpExceldataForBal
    # testdata = tmpExceldata
    return tmpExceldata

def writefile(data11 = [[]]):
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_name('Sheet1')
    copy_workbook = copy(data)
    wb = copy_workbook.get_sheet(0)

    i = 0
    for row in np.arange(1, 12 , 1):
        for col in np.arange(1, 12, 1):
            tmp = table.cell(row, col).value
            if tmp != '':
                for da in data11:
                    if int(da[0]) == i:
                        wb.write(row + 17, col, da[1])
                        break
                i  = i + 1

    copy_workbook.save(filename)

    return

# analysis all mh details
# ANZ_OUT = [[x1], [x2], [x3]]
# ANZ_IN = [[x5], [x9, x8], [x4]]
# ANZ_BALANCE = 0
# ANZ_NEED = 20
#
# CC_OUT = [[], [], [x4]]
# CC_IN = [[], [x10], []]
# CC_BALANCE = 0
# CC_NEED = 20
#
# SCBHK_OUT = [[x5], [x6], []]
# SCBHK_IN = [[x7], [], [x3]]
# SCBHK_BALANCE = 0
# SCBHK_NEED = 20
#
# SCBSG_OUT = [[x7], [x8], []]
# SCBSG_IN = [[x1], [x6], []]
# SCBSG_BALANCE = 1000
# SCBSG_NEED = 0
#
# DBHK_OUT = [[], [x9, x10], []]
# DBHK_IN = [[], [], []]
# DBHK_BALANCE = 0
# DBHK_NEED = 50
#
# DBSHK_OUT = [[], [], []]
# DBSHK_IN = [[], [x2], []]
# DBSHK_BALANCE = 500
# DBSHK_NEED = 0


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

class dataforpath:
    def __init__(self, fromMh, toMh, level):
        self.fromMh = fromMh
        self.toMh = toMh
        self.level = level

x1 = data("anz", "scbhk", 0)
x2 = data("anz", "dbhk", 1)
x3 = data("anz", "scbsg", 1)
x4 = data("anz", "cc", 2)
x5 = data("cc", "dbhk", 2)
x6 = data("scbhk","scbsg",0)
x7 = data("scbhk", "anz", 2)
x8 = data("scbsg", "anz", 0)
x9 = data("scbsg", "scbhk", 1)
x10 = data("dbshk", "anz", 1)

x11 = mhdata("anz", 0, 20)
x21 = mhdata("cc", 0, 20)
x31 = mhdata("scbhk", 0, 20)
x41 = mhdata("scbsg", 1000, 0)
x51 = mhdata("dbhk", 0, 50)
x61 = mhdata("dbshk",500,0)

# print(json.dumps(x1, default=lambda obj: obj.__dict__), ";",
#       json.dumps(x2, default=lambda obj: obj.__dict__), ";",
#       json.dumps(x3, default=lambda obj: obj.__dict__), ";",
#     json.dumps(x4, default=lambda obj: obj.__dict__), ";",
#     json.dumps(x5, default=lambda obj: obj.__dict__), ";",
#     json.dumps(x6, default=lambda obj: obj.__dict__), ";",
#     json.dumps(x7, default=lambda obj: obj.__dict__), ";",
#     json.dumps(x8, default=lambda obj: obj.__dict__), ";",
#     json.dumps(x9, default=lambda obj: obj.__dict__), ";",
#     json.dumps(x10, default=lambda obj: obj.__dict__)
#       )
#
# print(json.dumps(x11, default=lambda obj: obj.__dict__), ";",
#       json.dumps(x21, default=lambda obj: obj.__dict__), ";",
#       json.dumps(x31, default=lambda obj: obj.__dict__), ";",
#     json.dumps(x41, default=lambda obj: obj.__dict__), ";",
#     json.dumps(x51, default=lambda obj: obj.__dict__), ";",
#     json.dumps(x61, default=lambda obj: obj.__dict__)
#       )

def datatoclassData(d):
    return data(d['fromMh'], d['toMh'], d['level'])

def datatoclassMhdata(d):
    return mhdata(d['mhName'], d['balance'], d['need'])


testdata = getMhdata()
testmhdata = getMhdatabal()
# = '{"fromMh": "anz", "toMh": "scbhk", "level": 0} ; {"fromMh": "anz", "toMh": "dbhk", "level": 1} ; {"fromMh": "anz", "toMh": "scbsg", "level": 1} ; {"fromMh": "anz", "toMh": "cc", "level": 2} ; {"fromMh": "cc", "toMh": "dbhk", "level": 1} ; {"fromMh": "scbhk", "toMh": "scbsg", "level": 0} ; {"fromMh": "scbhk", "toMh": "anz", "level": 2} ; {"fromMh": "scbsg", "toMh": "anz", "level": 0} ; {"fromMh": "scbsg", "toMh": "scbhk", "level": 1} ; {"fromMh": "dbshk", "toMh": "anz", "level": 1}'
# testmhdata = '{"mhName": "anz", "balance": 0, "need": 20} ; {"mhName": "cc", "balance": 0, "need": 20} ; {"mhName": "scbhk", "balance": 0, "need": 20} ; {"mhName": "scbsg", "balance": 1000, "need": 0} ; {"mhName": "dbhk", "balance": 0, "need": 50} ; {"mhName": "dbshk", "balance": 500, "need": 0}'

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
        mhbalance.append(int(nodeclass.balance))
        mhbalance.append(int(nodeclass.need))
        mhrebalance.append(mhbalance)
    return mhrebalance


def levelmax(maxlevel = 0):
    mhlen = len(mhnames)
    for i in np.arange(0, maxlevel, 1):
        mmhs = []
        mmhs1 = []
        for j in np.arange(0, mhlen, 1):
            mmhs.append([])
            mmhs1.append([])
        mhoutdata.append(mmhs)
        mhindata.append(mmhs1)
    return None



def setdata(level , frommh = "", tomh = "", markdata = "",  allindata = [[[]]], alloutdata = [[[]]]):
    mhoutindex = 0
    for indexout, name in enumerate(mhnames):
        if name == frommh:
            mhoutindex = indexout
            break

    mhinindex = 0
    for indexin, name in enumerate(mhnames):
        if name == tomh:
            mhinindex = indexin
            break

    tmmp = alloutdata[int(level)][mhoutindex]
    tmmp.append(markdata)

    tmmp1 = allindata[int(level)][mhinindex]
    tmmp1.append(markdata)
    # allindata[int(level)][mhinindex].append(markdata)
    return None

def getdataOut(data = testdata, allindata = mhindata, alloutdata = mhoutdata):
    i = 0
    tmpin = allindata
    tmpout = alloutdata
    for eachnode in data.split(";"):
        nodeclass = json.loads(eachnode, object_hook =datatoclassData)
        level = nodeclass.level
        frommh = nodeclass.fromMh
        toMh = nodeclass.toMh
        iduu = str(uuid.uuid1())
        setdata(level, frommh, toMh, iduu, allindata, alloutdata)
        markdata.append(iduu)
        i = i + 1
    return None

# getmhdata()
# levelmax(3)
# getdataOut()

