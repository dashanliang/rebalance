from com.rebalance.controller import *
from com.rebalance.common.excelExec import *

if __name__ == '__main__':
    getMhdata()
    getmhdata()
    getmhdatabalance()
    levelmax(3)
    getdataOut()
    bestpaths = controllerMaxLevel(3)
    reeeeldate = getrealindex(bestpaths, markdata, mhoutdata)
    writefile(reeeeldate)