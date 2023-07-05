import sys
import Helper as hlpr
import StaticEstimations as sts
import InputOutputBlackHelper as io

def miniMax(board, depth, final_position, isMax):
    if depth == 0:
            hlpr.positionsEvaluated += 1
            # estimate = sts.staticEstimateMidGameEndGame(board)
            # print("Estimate ", str(estimate))
            return sts.staticEstimateMidGameEndGame(board), board
    if isMax:
            max_eval = float('-inf')
            for board_position in hlpr.generateMovesMidGameEndGame(board):
                val = miniMax(board_position, depth - 1, final_position, False)
                if val[0] > max_eval:
                    max_eval = val[0]
                    final_position = board_position
                    # print(str(max_eval ), "max eval")
            return max_eval, final_position
    else:
            min_eval = float('inf')
            for position in hlpr.generateMovesMidGameEndGameBlack(board):
                val = miniMax(position, depth - 1, final_position, True)
                if val[0] < min_eval:
                    min_eval = val[0]
                    final_position = val[1]
                    # print(str(min_eval) , "min eval")
            return min_eval, final_position

        
        
if __name__ == '__main__':
        inputBoardFile = io.readInputFile(sys.argv[1])
        outputBoardFile = sys.argv[2]
        depth = int(sys.argv[3])
        output = []
        resultantPosition = []
        output = miniMax(hlpr.swapWB(inputBoardFile), depth, resultantPosition, True)
        io.writeOutput(outputBoardFile, output[1] , hlpr.positionsEvaluated  , output[0] )