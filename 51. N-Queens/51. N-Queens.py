from typing import List


def solveNQueens(self, n: int) -> List[List[str]]:
    """
    Solves the N-Queens puzzle by placing N queens on an NxN chessboard such that no two queens threaten each other.

    :param n: The number of queens to place on the board.
    :return: A list of lists containing strings representing the board configurations where queens are placed in valid positions.
    """
    col = set()
    positive_diagonal = set() # (r - c)
    negative_diagonal = set() # (r + c)
    board = [['.'] * n for i in range(n)]
    res = []
    def backtracking(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
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
