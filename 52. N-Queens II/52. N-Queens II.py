def totalNQueens(n: int) -> int:
    """
    Counts the total number of distinct ways to place N queens on an NxN chessboard such that no two queens threaten each other.

    :param n: The number of queens to place on the board.
    :return: An integer representing the total number of valid configurations.
    """
    
    col = set()
    positive_diagonal = set() # (r - c)
    negative_diagonal = set() # (r + c)
    board = [['.'] * n for i in range(n)]
    res = 0
    def backtracking(r):
        nonlocal res
        if r == n:
            res += 1
        for c in range(n):
            if c in col or (c + r) in negative_diagonal or (r - c) in positive_diagonal:
                continue
            col.add(c)
            positive_diagonal.add(r - c)
            negative_diagonal.add(r + c)
            board[r][c] = 'Q'
    
            backtracking(r + 1)
            
            col.remove(c)
            positive_diagonal.remove(r - c)
            negative_diagonal.remove(r + c)
            board[r][c] = '.'

    backtracking(0)
    return res