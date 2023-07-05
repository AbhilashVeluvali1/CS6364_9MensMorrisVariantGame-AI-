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
def closeMill(loc, copyBoard):
    c = copyBoard[loc]
    
    if c == 'W' or c == 'B':
        if loc == 0:
            if (copyBoard[6] == c and copyBoard[18] == c):
                return True
            else:
                return False  # a0
        elif   loc == 1:
            if(copyBoard[11] == c and copyBoard[20]== c):
                return True
            else: 
                return False
        elif loc == 2:
            if (copyBoard[7] == c and copyBoard[15] == c):
                return True
            else:
                return False  # b1
        elif   loc == 3:
            if(copyBoard[10] == c and copyBoard[17]==c):
                return True
            else:
                return False
        elif loc == 4:
            if (copyBoard[8] == c and copyBoard[12] == c):
                return True
            else:
                return False  # c2
        elif loc == 5:
            if copyBoard[9] == c and copyBoard[14] == c:
                return True
            else:
                return False
        elif loc == 6:
            if (copyBoard[7] == c and copyBoard[8] == c) or (copyBoard[0] == c and copyBoard[18] == c):
                return True
            else:
                return False  # a3
        elif loc == 7:
            if (copyBoard[6] == c and copyBoard[8] == c) or (copyBoard[2] == c and copyBoard[15] == c):
                return True
            else:
                return False  # b3
        elif loc == 8:
            if (copyBoard[6] == c and copyBoard[7] == c) or (copyBoard[4] == c and copyBoard[12] == c):
                return True
            else:
                return False  # c3
        elif   loc == 9:
            if(copyBoard[5] == c and copyBoard[14]==c) or (copyBoard[10] == c and copyBoard[12] == c):
                return True
            else:
                return False
        elif   loc == 10:
            if(copyBoard[3] == c and copyBoard[17]==c) or (copyBoard[9] == c and copyBoard[11] == c):
                return True
            else:
                return False
        elif   loc == 11:
            if(copyBoard[1] == c and copyBoard[20]==c) or (copyBoard[9] == c and copyBoard[10] == c):
                return True
            else:
                return False
        elif loc == 12:
            if (copyBoard[4] == c and copyBoard[8] == c) or (copyBoard[13] == c and copyBoard[14] == c):
                return True
            else:
                return False  # c4
        elif loc == 13:
            if (copyBoard[12] == c and copyBoard[14] == c) or (copyBoard[16] == c and copyBoard[19] == c):
                return True
            else:
                return False  # d4
        elif   loc == 14:
            if(copyBoard[5] == c and copyBoard[9]==c) or (copyBoard[12] == c and copyBoard[13] == c):
                return True
            else:
                return False
        elif loc == 15:
            if (copyBoard[7] == c and copyBoard[2] == c) or (copyBoard[16] == c and copyBoard[17] == c):
                return True
            else:
                return False  # b5
        elif loc == 16:
            if (copyBoard[13] == c and copyBoard[19] == c) or (copyBoard[15] == c and copyBoard[17] == c):
                return True
            else:
                return False  # d5
        elif   loc == 17:
            if(copyBoard[3] == c and copyBoard[10]==c) or (copyBoard[15] == c and copyBoard[16] == c):
                return True
            else:
                return False
        elif loc == 18:
            if (copyBoard[0] == c and copyBoard[6] == c) or (copyBoard[19] == c and copyBoard[20] == c):
                return True
            else:
                return False  # a6
        elif loc == 19:
            if (copyBoard[13] == c and copyBoard[16] == c) or (copyBoard[18] == c and copyBoard[20] == c):
                return True
            else:
                return False  # d6
        elif   loc == 20:
            if(copyBoard[1] == c and copyBoard[11]==c) or (copyBoard[18] == c and copyBoard[19] == c):
                return True
            else:
                return False
        
#GenerateRemove Method
def generateRemove(b, lst):
    grList = lst.copy()
    for i in range(len(b)):
        cbo =b
        if b[i] == 'B':
            if not closeMill(i, b):
                cbo[i] = 'x'
                grList.append(cbo)
            else:
                grList.append(cbo)
    return grList

#GenerateMoves Method
def generateMove(x):
    gmList = []
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
                        #gmList.append(generateRemove(copyBoard, gmList))
                        generateRemove(copyBoard, gmList)
                    else:
                        gmList.append(copyBoard)
    return gmList

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
    ghList = []
    copyBoard = x.copy()
    for i in range(len(x)):
        if x[i] == 'W':
            for j in range(len(x)):
                if x[j] == 'x':
                    copyBoard = x.copy()
                    copyBoard[i] = 'x'
                    copyBoard[j] = 'W'
                    if closeMill(j, copyBoard):
                        #ghList.append(generateRemove(copyBoard, ghList))
                        generateRemove(copyBoard, ghList)
                    else:
                        ghList.append(copyBoard)
    return ghList

def generateMovesOpening(postions) :
    return generateAdd(postions)

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
    lboard = x.copy()
    for i in range(len(lboard)):
        if lboard[i] == 'W':
            lboard[i] = 'B'
        elif lboard[i] == 'B':
            lboard[i] = 'W'
    return lboard

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
    for i in range(0,len(positions)):
        for j in range(0, len(i)):
            if(positions[j] == "B"):
                if(closeMill(i,positions)== True):
                    cnt+=1
    return cnt


