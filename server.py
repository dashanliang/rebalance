from controller import *

if __name__ == '__main__':
    sheetname = "AUD"
    getMhdata(sheetname)
    getalldatafromexcel(sheetname)
    getmhdata(sheetname)
    getmhdatabalance(sheetname)
    levelmax(3)
    getdataOut(sheetname)
    bestpaths = controllerMaxLevel(3)
    if bestpaths != None:
        reeeeldate = getrealindex(bestpaths, markdata, mhoutdata)
        print(reeeeldate)
        writefile(reeeeldate, sheetname)
    else:
        print("there is no path can rebalance")

    # sheetname = "EUR"
    # getMhdata()
    # getmhdata()
    # getmhdatabalance()
    # levelmax(3)
    # getdataOut()
    # bestpaths = controllerMaxLevel(3)
    # if bestpaths != None:
    #     reeeeldate = getrealindex(bestpaths, markdata, mhoutdata)
    #     print(reeeeldate)
    #     writefile(reeeeldate)
    # else:
    #     print("there is no path can rebalance")
    #
    # sheetname = "CAD"
    # getMhdata()
    # getmhdata()
    # getmhdatabalance()
    # levelmax(3)
    # getdataOut()
    # bestpaths = controllerMaxLevel(3)
    # if bestpaths != None:
    #     reeeeldate = getrealindex(bestpaths, markdata, mhoutdata)
    #     print(reeeeldate)
    #     writefile(reeeeldate)
    # else:
    #     print("there is no path can rebalance")
    #
    # sheetname = "GBP"
    # getMhdata()
    # getmhdata()
    # getmhdatabalance()
    # levelmax(3)
    # getdataOut()
    # bestpaths = controllerMaxLevel(3)
    # if bestpaths != None:
    #     reeeeldate = getrealindex(bestpaths, markdata, mhoutdata)
    #     print(reeeeldate)
    #     writefile(reeeeldate)
    # else:
    #     print("there is no path can rebalance")
    #
    # sheetname = "AUD"
    # getMhdata()
    # getmhdata()
    # getmhdatabalance()
    # levelmax(3)
    # getdataOut()
    # bestpaths = controllerMaxLevel(3)
    # if bestpaths != None:
    #     reeeeldate = getrealindex(bestpaths, markdata, mhoutdata)
    #     print(reeeeldate)
    #     writefile(reeeeldate)
    # else:
    #     print("there is no path can rebalance")

