# # coding=utf-8
# from copy import copy
#
# import xlrd
# from xlutils.copy import copy
# import numpy as np
# from com.rebalance.common.globaldata import *
#
# def getMhdata():
#     # 打开文件
#     data = xlrd.open_workbook('/Users/jinglan.liang/Downloads/demo1.xlsx')
#     table = data.sheet_by_name('Sheet1')
#
#     tmpExceldata = ''
#
#     for row in np.arange(1, 11 , 1):
#         for col in np.arange(1, 11, 1):
#             tmp = table.cell(row, col).value
#             if tmp != '':
#                 if tmpExceldata == '':
#                     tmpExceldata = json.dumps(dataforpath('mh' + str(row), 'mh' + str(col), tmp), default=lambda obj: obj.__dict__)
#                 else:
#                     tmpExceldata = tmpExceldata + ";" + json.dumps(dataforpath('mh' + str(row), 'mh' + str(col), tmp), default=lambda obj: obj.__dict__)
#
#     print(tmpExceldata)
#
#     tmpExceldataForBal = ''
#
#     for colForbal in np.arange(1, 11, 1):
#         tmpbal = table.cell(11, colForbal).value
#         if tmpbal != '':
#             if tmpExceldataForBal == '':
#                 tmpExceldataForBal = json.dumps(mhdata('mh'+ str(colForbal), table.cell(11, colForbal).value, table.cell(12, colForbal).value),
#                                           default=lambda obj: obj.__dict__)
#             else:
#                 tmpExceldataForBal = tmpExceldataForBal + ";" + json.dumps(mhdata('mh'+ str(colForbal), table.cell(11, colForbal).value, table.cell(12, colForbal).value),
#                                           default=lambda obj: obj.__dict__)
#
#     print(tmpExceldataForBal)
#
#     testmhdata = tmpExceldataForBal
#     testdata = tmpExceldata
#     return
#
#
# def writefile(data11 = [[]]):
#     data = xlrd.open_workbook('/Users/jinglan.liang/Downloads/demo1.xlsx')
#     table = data.sheet_by_name('Sheet1')
#     copy_workbook = copy(data)
#     wb = copy_workbook.get_sheet(0)
#
#     i = 0
#     for row in np.arange(1, 11 , 1):
#         for col in np.arange(1, 11, 1):
#             tmp = table.cell(row, col).value
#             if tmp != '':
#                 for da in data11:
#                     if int(da[0]) == i:
#                         wb.write(row + 16, col, da[1])
#                         break
#                 i  = i + 1
#
#     copy_workbook.save("/Users/jinglan.liang/Downloads/demo1.xlsx")
#
#     return