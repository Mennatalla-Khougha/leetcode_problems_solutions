from typing import List 


def setZeroes(matrix: List[List[int]]) -> None:
    """
    The function `setZeroes` takes a matrix as input and sets all the rows and columns containing a zero
    to zero.
    
    :param matrix: The parameter `matrix` is a 2D list of integers. It represents a matrix where each
    element is an integer
    :type matrix: List[List[int]]
    """
    col, row = len(matrix[0]), len(matrix)
    row_zero, col_zero = [], []
    
    for j in range(row):
        for i in range(col):
            if matrix[j][i] == 0:
                row_zero.append(j)
                col_zero.append(i)

    # Generate the row of zeros
    for i in row_zero:
        matrix[i] = [0] * col
        
    # Generate the column of zeros
    for i in col_zero:
        for j in range(row):
            matrix[j][i] = 0
