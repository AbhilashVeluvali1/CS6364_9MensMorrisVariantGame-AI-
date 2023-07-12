positionsEvaluated =0
#Add initial ppositions
def generateAdd(postions):
    allList = []
    copyBoard = []
    
    for i in range(len(postions)):
        if postions[i] == 'x':
            copyBoard = postions.copy()
            copyBoard[i] = 'W'
            if closeMill(i, copyBoard):
                generateRemove(copyBoard, allList)
            else:
                allList.append(copyBoard)
    
    return allList

#CloseMill method
def closeMill(loc, pos):
    c = pos[loc] 
    if c == 'W' or c == 'B':
        if loc == 0:
            if (pos[6] == c and pos[18] == c):
                return True
            else:
                return False  # a0
        elif loc == 1:
            if(pos[11] == c and pos[20]== c):
                return True
            else: 
                return False
        elif loc == 2:
            if (pos[7] == c and pos[15] == c):
                return True
            else:
                return False  # b1
        elif   loc == 3:
            if(pos[10] == c and pos[17]==c):
                return True
            else:
                return False
        elif loc == 4:
            if (pos[8] == c and pos[12] == c):
                return True
            else:
                return False  # c2
        elif loc == 5:
            if pos[9] == c and pos[14] == c:
                return True
            else:
                return False
        elif loc == 6:
            if (pos[7] == c and pos[8] == c) or (pos[0] == c and pos[18] == c):
                return True
            else:
                return False  # a3
        elif loc == 7:
            if (pos[6] == c and pos[8] == c) or (pos[2] == c and pos[15] == c):
                return True
            else:
                return False  # b3
        elif loc == 8:
            if (pos[6] == c and pos[7] == c) or (pos[4] == c and pos[12] == c):
                return True
            else:
                return False  # c3
        elif   loc == 9:
            if(pos[5] == c and pos[14]==c) or (pos[10] == c and pos[12] == c):
                return True
            else:
                return False
        elif   loc == 10:
            if(pos[3] == c and pos[17]==c) or (pos[9] == c and pos[11] == c):
                return True
            else:
                return False
        elif   loc == 11:
            if(pos[1] == c and pos[20]==c) or (pos[9] == c and pos[10] == c):
                return True
            else:
                return False
        elif loc == 12:
            if (pos[4] == c and pos[8] == c) or (pos[13] == c and pos[14] == c):
                return True
            else:
                return False  # c4
        elif loc == 13:
            if (pos[12] == c and pos[14] == c) or (pos[16] == c and pos[19] == c):
                return True
            else:
                return False  # d4
        elif   loc == 14:
            if(pos[5] == c and pos[9]==c) or (pos[12] == c and pos[13] == c):
                return True
            else:
                return False
        elif loc == 15:
            if (pos[7] == c and pos[2] == c) or (pos[16] == c and pos[17] == c):
                return True
            else:
                return False  # b5
        elif loc == 16:
            if (pos[13] == c and pos[19] == c) or (pos[15] == c and pos[17] == c):
                return True
            else:
                return False  # d5
        elif   loc == 17:
            if(pos[3] == c and pos[10]==c) or (pos[15] == c and pos[16] == c):
                return True
            else:
                return False
        elif loc == 18:
            if (pos[0] == c and pos[6] == c) or (pos[19] == c and pos[20] == c):
                return True
            else:
                return False  # a6
        elif loc == 19:
            if (pos[13] == c and pos[16] == c) or (pos[18] == c and pos[20] == c):
                return True
            else:
                return False  # d6
        elif   loc == 20:
            if(pos[1] == c and pos[11]==c) or (pos[18] == c and pos[19] == c):
                return True
            else:
                return False
        
#GenerateRemove Method
def generateRemove(b, lst):
    rmvList = lst.copy()
    for i in range(len(b)):
        cbo =b
        if b[i] == 'B':
            if not closeMill(i, b):
                cbo[i] = 'x'
                rmvList.append(cbo)
            else:
                rmvList.append(cbo)
    return rmvList

#GenerateMoves Method
def generateMove(x):
    mvList = []
    copyBoard = x.copy()
    for i in range(len(x)):
        if x[i] == 'W':
            nlist = neighbours(i)
            for j in nlist:
                if x[j] == 'x':
                    copyBoard = x.copy()
                    copyBoard[i] = 'x'
                    copyBoard[j] = 'W'
                    if closeMill(j, copyBoard):
                        generateRemove(copyBoard, mvList)
                    else:
                        mvList.append(copyBoard)
    return mvList

#Findout Neighbours
def neighbours(j):
    adj = []
    if j == 0:
        adj = [1, 6]
    elif j == 1:
        adj = [0, 11]
    elif j == 2:
        adj = [3, 7]
    elif j == 3:
        adj = [2, 10]
    elif j == 4:
        adj = [5, 8]
    elif j == 5:
        adj = [4, 9]
    elif j == 6:
        adj = [0, 7, 18]
    elif j == 7:
        adj = [2, 6, 8, 15]
    elif j == 8:
        adj = [4, 7, 12]
    elif j == 9:
        adj = [5, 10, 14]
    elif j == 10:
        adj = [3, 9, 11, 17]
    elif j == 11:
        adj = [1, 10, 20]
    elif j == 12:
        adj = [8, 13]
    elif j == 13:
        adj = [12, 14, 16]
    elif j == 14:
        adj = [9, 13]
    elif j == 15:
        adj = [7, 16]
    elif j == 16:
        adj = [13, 15, 17, 19]
    elif j == 17:
        adj = [10, 16]
    elif j == 18:
        adj = [6, 19]
    elif j == 19:
        adj = [16, 18, 20]
    elif j == 20:
        adj = [11, 19]
    return adj

#Generate Hopping
def generateHopping(x):
    hpgList = []
    copyBoard = x.copy()
    for i in range(len(x)):
        if x[i] == 'W':
            for j in range(len(x)):
                if x[j] == 'x':
                    copyBoard = x.copy()
                    copyBoard[i] = 'x'
                    copyBoard[j] = 'W'
                    if closeMill(j, copyBoard):
                        generateRemove(copyBoard, hpgList)
                    else:
                        hpgList.append(copyBoard)
    return hpgList

#Generate Moves opening method
def generateMovesOpening(postions) :
    return generateAdd(postions)

#Generate Moves midgame endgame method
def generateMovesMidGameEndGame(position):
    count= 0
    for i in range(len(position)):
        if(position[i] == 'W'):
            count +=1
    if(count == 3):
        return generateHopping(position)
    else:
       return generateMove(position)

#swap white to black or black to white
def swapWB(x):
    board = x.copy()
    for i in range(len(board)):
        if board[i] == 'W':
            board[i] = 'B'
        elif board[i] == 'B':
            board[i] = 'W'
    return board

#count the no of whites/ blacks 
def getCount(positions, color):
    cnt=0
    for i in range(len(positions)):
        if positions[i] == color:
            cnt=cnt+1
    return cnt

#Revet to Original 
def revetToOriginal(positoin):
    blackMovesList =[]
    for i in positoin:
        blackMovesList.append(swapWB(i))
    return blackMovesList

#Generating opening moves for black
def generateMovesOpeningBlack(positions):
    blackPos = swapWB(positions)
    blackPosList = generateMovesOpening(blackPos)
    return revetToOriginal(blackPosList)

#Generating moves for black
def generateMovesMidGameEndGameBlack(positions):
    blackPos = swapWB(positions)
    blackPosList = generateMovesMidGameEndGame(blackPos)
    return revetToOriginal(blackPosList)

#Count the no of black closed mills
def countBMills(positions):
    cnt = 0
    for i in range(len(positions)):
        if(positions[i] == "B"):
            if(closeMill(i,positions)== True):
                cnt+=1
    return cnt


