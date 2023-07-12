import sys
import Helper as hlpr
import StaticEstimations as sts
import InputOutputHelper as io

def maxMin(board, depth, finalPosition):
    maxEval = float('-inf')
    for boardPositions in hlpr.generateMovesMidGameEndGame(board):
        val = miniMax(boardPositions, depth - 1, finalPosition, False)
        if val[0] > maxEval:
            maxEval = val[0]
            finalPosition = boardPositions
    return maxEval, finalPosition
   
def minMax(board, depth, finalPosition):
    minEval = float('inf')
    for position in hlpr.generateMovesMidGameEndGameBlack(board):
        val = miniMax(position, depth - 1, finalPosition, True)
        if val[0] < minEval:
            minEval = val[0]
            finalPosition = val[1]
    return minEval, finalPosition
   
   
def miniMax(board, depth, finalPosition, isMax):
    if depth == 0:
            hlpr.positionsEvaluated += 1
            return sts.staticEstimateMidGameEndGame(board), board
    if isMax:
        return maxMin(board, depth, finalPosition)
    else:
        return minMax(board, depth, finalPosition)
        
        
  
if __name__ == "__main__":
        inputBoardFile = io.readInputFile(sys.argv[1])
        outputBoardFile = sys.argv[2]
        depth = int(sys.argv[3])
        output = []
        resultantPosition = []
        output = miniMax(inputBoardFile, depth, resultantPosition, True)
        io.writeOutput(outputBoardFile, output[1] , hlpr.positionsEvaluated  , output[0] )