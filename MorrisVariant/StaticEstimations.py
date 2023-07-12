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

#Improved static estimate 
def staticEstimateMidGameEndGameImproved(positions):
    cntW = hlpr.getCount(positions,'W')
    cntB = hlpr.getCount(positions,'B')
    
    blackPositions = hlpr.swapWB(positions)
    blackMillCnt = hlpr.countBMills(blackPositions)
    midgameEndGamePositionsBlack = hlpr.generateMovesMidGameEndGame(blackPositions)
    midgameEndGamePositionsWhite = hlpr.generateMovesMidGameEndGame(positions)
    noOfBlackMoves = len(midgameEndGamePositionsBlack)
    noOfWhiteMoves = len(midgameEndGamePositionsWhite)
    if(cntB<=2):
        return 10000
    elif(cntW<=2):
        return -10000
    elif(noOfBlackMoves == 0):
        return 10000
    else:
        return  100*(noOfWhiteMoves +  cntW)-cntB
    #(whiteMoves + whitePiceCount)-noOfBlackPices

#Improved static estimate for opening
def staticEstimateOpeningImproved(positions):
        return  10*(hlpr.getCount(positions,'W')-hlpr.getCount(positions,'B'))

    
    
    

        
    
    

    
    


    