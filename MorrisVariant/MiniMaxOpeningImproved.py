import sys
import Helper as hlpr
import StaticEstimations as sts
import InputOutputHelper as io

def maximize(board, depth, finalPosition):
    if depth == 0:
        hlpr.positionsEvaluated += 1
        return sts.staticEstimateOpeningImproved(board), board
    else:
        maxEval = float('-inf')
        for board_position in hlpr.generateMovesOpening(board):
            val = minimize(board_position, depth - 1, finalPosition)
            if val[0] > maxEval:
                maxEval = val[0]
                finalPosition = board_position
        return maxEval, finalPosition

def minimize(board, depth, finalPosition):
    if depth == 0:
        hlpr.positionsEvaluated += 1
        return sts.staticEstimateOpeningImproved(board), board
    else:
        minEval = float('inf')
        for position in hlpr.generateMovesOpeningBlack(board):
            val = maximize(position, depth - 1, finalPosition)
            if val[0] < minEval:
                minEval = val[0]
                finalPosition = val[1]
        return minEval, finalPosition
    
    
def miniMax(board, depth, finalPosition):
    
    return minimize(board, depth, finalPosition) or maximize(board, depth, finalPosition)



if __name__ == "__main__":
        inputBoardFile = io.readInputFile(sys.argv[1])
        outputBoardFile = sys.argv[2]
        depth = int(sys.argv[3])
        output = []
        resultantPosition = []
        output = miniMax(inputBoardFile, depth, resultantPosition)
        io.writeOutput(outputBoardFile, output[1] , hlpr.positionsEvaluated  , output[0])
            

