import sys
import Helper as hlpr
#static estimate of midgameendgame
def staticEstimateMidGameEndGame(positions):
    cntW = hlpr.getCount(positions,'W')
    cntB = hlpr.getCount(positions,'B')
    blackPositions = hlpr.swapWB(positions)
    midgameEndGamePositions = hlpr.generateMovesMidGameEndGame(blackPositions)
    noOfBlackMoves = len(midgameEndGamePositions)
    if(cntB<=2):
        return 10000
    elif(cntW<=2):
        return -10000
    elif(noOfBlackMoves == 0):
        return 10000
    else:
        return (1000*(cntW-cntB))-noOfBlackMoves
    

#Static estimate of Opening
def staticEstimateOpening(positions):
    return  (hlpr.getCount(positions,'W')-hlpr.getCount(positions,'B'))


def staticEstimateMidGameEndGameImproved(positions):
    cntW = hlpr.getCount(positions,'W')
    cntB = hlpr.getCount(positions,'B')
    
    blackPositions = hlpr.swapWB(positions)
    blackMillCnt = hlpr.countBMills(blackPositions)
    print(blackMillCnt)
    midgameEndGamePositions = hlpr.generateMovesMidGameEndGame(blackPositions)
    noOfBlackMoves = len(midgameEndGamePositions)
    if(cntB<=2):
        return 10000
    elif(cntW<=2):
        return -10000
    elif(noOfBlackMoves == 0):
        return 10000
    else:
        return  noOfBlackMoves-blackMillCnt
    

    
    
    

        
    
    

    
    


    