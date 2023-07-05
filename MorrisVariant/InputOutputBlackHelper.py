def readInputFile(inputFile):
    with open(inputFile, 'r') as f:
        boardPos = f.read()
    return list(boardPos)

def writeOutput(outputFileName, boardPosition, positionEvaluated, staticEstimate):
    print('Board Position :', boardPosition)
    print('Positions evaluated by Static Estimation :', positionEvaluated)
    print('MINIMAX estimate :', -1*staticEstimate)
    # with open(outputFileName, 'w') as f:
    #     f.write(list(boardPosition))