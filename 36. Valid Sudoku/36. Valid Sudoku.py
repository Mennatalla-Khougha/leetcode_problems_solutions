def isValidSudoku(self, board: List[List[str]]) -> bool:
    # initialize the rows, cols, square dict
    row = {i: set() for i in range(9)}
    cols = {j: set() for j in range(9)}
    square = {(i // 3, j // 3): set() for i in range(9) for j in range(9)}
    
    # loop through each cell in the board
    for i in range(9):
        for j in range(9):
            # skip empty cells
            if board[i][j] == ".":
                continue
            # check for dupicate in row, cols, square
            if (board[i][j] in row[i] or board[i][j] in cols[j] or board[i][j] in square[(i // 3, j // 3)]):
                return False
            
            # add the value of the cell to the row, cols, square
            row[i].add(board[i][j])
            cols[j].add(board[i][j])
            square[(i // 3, j // 3)].add(board[i][j])
    return True
