# coding=utf-8
from copy import copy

import xlrd
from xlutils.copy import copy
import numpy as np
from com.rebalance.common.globaldata import *

def getMhdata():
    # 打开文件
    data = xlrd.open_workbook('/Users/jinglan.liang/Downloads/demo.xlsx')
    table = data.sheet_by_name('Sheet1')
    print("整行值：" + str(table.row_values(0)))
    print("整列值：" + str(table.col_values(0)))

    tmpExceldata = ''

    for row in np.arange(1, 11 , 1):
        for col in np.arange(1, 11, 1):
            tmp = table.cell(row, col).value
            if tmp != '':
                if tmpExceldata == '':
                    tmpExceldata = json.dumps(dataforpath('mh' + str(row), 'mh' + str(col), tmp), default=lambda obj: obj.__dict__)
                else:
                    tmpExceldata = tmpExceldata + ";" + json.dumps(dataforpath('mh' + str(row), 'mh' + str(col), tmp), default=lambda obj: obj.__dict__)

    print(tmpExceldata)

    tmpExceldataForBal = ''

    for colForbal in np.arange(1, 11, 1):
        tmpbal = table.cell(11, colForbal).value
        if tmpbal != '':
            if tmpExceldataForBal == '':
                tmpExceldataForBal = json.dumps(mhdata('mh'+ str(colForbal), table.cell(11, colForbal).value, table.cell(12, colForbal).value),
                                          default=lambda obj: obj.__dict__)
            else:
                tmpExceldataForBal = tmpExceldataForBal + ";" + json.dumps(mhdata('mh'+ str(colForbal), table.cell(11, colForbal).value, table.cell(12, colForbal).value),
                                          default=lambda obj: obj.__dict__)

    print(tmpExceldataForBal)
    copy_workbook = copy(data)
    wb = copy_workbook.get_sheet(0)
    wb.write(2, 4, "0")
    wb.write(5, 3, "1")
    wb.write(11, 3, "1")
    copy_workbook.save("/Users/jinglan.liang/Downloads/demo.xlsx")


getMhdata()