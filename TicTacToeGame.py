import numpy as np
from sklearn.neural_network import MLPClassifier

c = 0; 

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

B = np.loadtxt("datasets-part1/tictac_single.txt")
X = B[:, :9]
Y = B[:, 9:]

mlpClassifier = MLPClassifier()
mlpClassifier.fit(X, Y); 

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
    

while True:
    row = input('Enter a row (0 to 2) : ')
    column = input('Enter a column (0 to 2) : ')
    if board[int(row)][int(column)] != 0:
        print('Not valid input')
        print(board[0])
        print(board[1])
        print(board[2])
        print('')
        continue 
    board[int(row)][int(column)] = 1
    c += 1
    if determineWinner(1):
        print('Human Player won')
        break 
    if c == 9:
        print('Game is a tie')
        break
    
    boardNumpy = np.array(board)
    boardNumpyFlatten = boardNumpy.flatten()
    boardNumpyFlattenRe = boardNumpyFlatten.reshape((1, -1))
    #print('boardNumpyFlattenRe:\n', boardNumpyFlattenRe)
    index = mlpClassifier.predict(boardNumpyFlattenRe)
    
    #print('Computer Index: ', len(index))
    row1 = index[0] // 3
    col1 = index[0] % 3
    #print('Row ', int(row1))
    #print('Column ', int(col1))
    board[int(row1)][int(col1)] = -1
    c += 1
    if determineWinner(-1):
        print('Computer Player won')
        break 
    if c == 9:
        print('Game is a tie')
        break
    
    print(board[0])
    print(board[1])
    print(board[2])
    print('')
    