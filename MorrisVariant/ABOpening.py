
import sys
import Helper as hlpr
import StaticEstimations as sts 
import InputOutputHelper as io
    
def maxMin(board, depth, finalPosition,alpha,beta):
    max_eval = alpha
    for board_position in hlpr.generateMovesOpening(board):
        val = AlphaBetaMinMax(board_position, depth - 1, finalPosition, False, alpha, beta)
        if alpha>=beta:
            break
        else:
            alpha = max(max_eval,alpha)
        if val[0] > max_eval:
            max_eval = val[0]
            finalPosition = board_position
    return max_eval, finalPosition


def minMax(board, depth, finalPosition,alpha,beta):
    min_eval = beta
    for position in hlpr.generateMovesOpeningBlack(board):
        val = AlphaBetaMinMax(position, depth - 1, finalPosition, True, alpha, beta)
        if alpha>=beta:
            break
        else:
            beta = min(min_eval,beta)
        if val[0] < min_eval:
            min_eval = val[0]
            finalPosition = val[1]
    return min_eval, finalPosition 
     
def AlphaBetaMinMax(board, depth, finalPosition, isMax,alpha,beta):
    if depth == 0:
        hlpr.positionsEvaluated += 1
        return sts.staticEstimateOpening(board), board
    if(isMax):
        return maxMin(board, depth, finalPosition,alpha,beta)
    else :
        return minMax(board, depth, finalPosition,alpha,beta)
        
if __name__ == "__main__":
        inputBoardFile = io.readInputFile(sys.argv[1])
        outputBoardFile = sys.argv[2]
        depth = int(sys.argv[3])
        output = []
        resultantPosition = []
        output = AlphaBetaMinMax(inputBoardFile, depth, resultantPosition, True,float('-inf'),float('inf'))
        io.writeOutput(outputBoardFile, output[1] , hlpr.positionsEvaluated  , output[0] )
        
          

