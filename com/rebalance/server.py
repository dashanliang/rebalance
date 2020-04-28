from com.rebalance.controller import *
from com.rebalance.common.excelExec import *

if __name__ == '__main__':
    getMhdata()
    getmhdata()
    getmhdatabalance()
    levelmax(3)
    getdataOut()
    bestpaths = controllerMaxLevel(3)
    if bestpaths != None:
        reeeeldate = getrealindex(bestpaths, markdata, mhoutdata)
        print(reeeeldate)
        writefile(reeeeldate)
    else:
        print("there is no path can rebalance")