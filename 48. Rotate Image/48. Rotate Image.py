def rotate(matrix: List[List[int]]) -> None:
    # transpose the matrix in place replacing it's rows with it's column
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # reverse each row in the matrix
    for i in range(len(matrix)):
        matrix[i].reverse()
    