def findNextCellToFill(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                return i, j
    return -1, -1


def isValid(board, i, j, e):
    rowOk = all([e != board[i][x] for x in range(9)])
    if rowOk:
        coloumnOk = all([e != board[x][j] for x in range(9)])
        if coloumnOk:
            # checking the box
            secTopX, secTopy = 3*(i//3), 3*(j//3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopy, secTopy+3):
                    if board[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(board, i=0, j=0):
    i, j = findNextCellToFill(board)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(board, i, j, e):
            board[i][j] = e
            if solveSudoku(board, i, j):
                return True
            # Backtracking
            board[i][j] = 0
    return False


board = [[5, 1, 7, 6, 0, 0, 0, 3, 4], [2, 8, 9, 0, 0, 4, 0, 0, 0], [3, 4, 6, 2, 0, 5, 0, 9, 0], [6, 0, 2, 0, 0, 0, 0, 1, 0], [
    0, 3, 8, 0, 0, 6, 0, 4, 7], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 9, 0, 0, 0, 0, 0, 7, 8], [7, 0, 3, 4, 0, 0, 5, 6, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
solveSudoku(board)
print(board)
