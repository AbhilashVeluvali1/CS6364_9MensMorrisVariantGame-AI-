import sys
import Helper as hlpr
import StaticEstimations as sts
import InputOutputBlackHelper as io    

def maxMin(board, depth, finalPosition, isMax):
        maxEval = float('-inf')
        for board_position in hlpr.generateMovesOpening(board):
                val = minMaxBlack(board_position, depth - 1, finalPosition, False)
                if val[0] > maxEval:
                        maxEval = val[0]
                        finalPosition = board_position
        return maxEval, finalPosition
def minMax(board, depth, finalPosition, isMax):
        minEval = float('inf')
        for position in hlpr.generateMovesOpeningBlack(board):
                val = minMaxBlack(position, depth - 1, finalPosition, True)
                if val[0] < minEval:
                        minEval = val[0]
                        finalPosition = val[1]
        return minEval, finalPosition

def minMaxBlack(board, depth, finalPosition, isMax):
        if depth == 0:
                hlpr.positionsEvaluated += 1
                return sts.staticEstimateOpening(board), board
        if(isMax):
                return maxMin(board, depth, finalPosition, isMax)
        else:
                return minMax(board, depth, finalPosition, isMax)
    
if __name__ == '__main__':
        inputBoardFile = io.readInputFile(sys.argv[1])
        outputBoardFile = sys.argv[2]
        depth = int(sys.argv[3])
        output = []
        resultantPosition = []
        output = minMaxBlack(hlpr.swapWB(inputBoardFile), depth, resultantPosition, True)
        io.writeOutput(outputBoardFile, output[1] , hlpr.positionsEvaluated  , output[0])