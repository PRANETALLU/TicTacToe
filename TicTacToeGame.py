import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsRegressor

c = 0; 

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Single Label
B = np.loadtxt("datasets-part1/tictac_single.txt")
X = B[:, :9]
Y = B[:, 9:]

mlpClassifier = MLPClassifier()
mlpClassifier.fit(X, Y); 

# Multi Label
C = np.loadtxt("datasets-part1/tictac_multi.txt")
X1 = C[:, :9]
Y1 = C[:, 9:]

kNeigh = KNeighborsRegressor(n_neighbors=3)
kNeigh.fit(X1, Y1)

def determineWinner(player: int):
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] == player:
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] == player:
        return True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] == player:
        return True
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] == player:
        return True
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] == player:
        return True
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] == player:
        return True
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] == player:
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] == player:
        return True
    else:
        return False

def printBoard():
    print(board[0])
    print(board[1])
    print(board[2])
    print('')
    

while True:
    row = input('Enter a row (0 to 2) : ')
    column = input('Enter a column (0 to 2) : ')
    if board[int(row)][int(column)] != 0:
        print('Not valid input')
        printBoard()
        continue 
    board[int(row)][int(column)] = 1
    c += 1
    if determineWinner(1):
        print('Human Player won')
        printBoard()
        break 
    if c == 9:
        print('Game is a tie')
        printBoard()
        break
    
    # Single Label
    """boardNumpy = np.array(board)
    boardNumpyFlatten = boardNumpy.flatten()
    boardNumpyFlattenRe = boardNumpyFlatten.reshape((1, -1))
    index = mlpClassifier.predict(boardNumpyFlattenRe)
    
    row1 = index[0] // 3
    col1 = index[0] % 3
    board[int(row1)][int(col1)] = -1
    c += 1"""
    
    # Multi Label
    boardNumpy1 = np.array(board)
    boardNumpyFlatten1 = boardNumpy1.flatten()
    boardNumpyFlattenRe1 = boardNumpyFlatten1.reshape((1, -1))
    availableInd = kNeigh.predict(boardNumpyFlattenRe1)
    availableInd = availableInd.flatten()
   
    newIndex = np.argsort(availableInd)
    reverseIndex = newIndex[::-1]
    
    for index in reverseIndex:
        if board[index // 3][index % 3] == 0:
            board[index // 3][index % 3] = -1
            c += 1
            break
    
    if determineWinner(-1):
        print('Computer Player won')
        printBoard()
        break 
    if c == 9:
        print('Game is a tie')
        printBoard()
        break
    
    printBoard()