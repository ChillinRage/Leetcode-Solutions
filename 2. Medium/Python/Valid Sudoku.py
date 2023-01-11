def isValidSudoku(board):
    for row in board: # check row
        check = []
        for each in row:
            if each == '.':
                continue
            if each in check:
                return False
            
            check.append(each)
            
    for i in range(9): # check col
        check = []
        col = [board[_][i] for _ in range(9)]
        for each in col:
            if each == '.':
                continue
            if each in check:
                return False
            
            check.append(each)
            
    for r in range(0,9,3): # check block (3x3 grid)
        for c in range(0,9,3):
            box = board[r][c:c+3] + board[r+1][c:c+3] + board[r+2][c:c+3]
            check = []
            for each in box:
                if each == '.':
                    continue
                if each in check:
                    return False
                
                check.append(each)

    return True
