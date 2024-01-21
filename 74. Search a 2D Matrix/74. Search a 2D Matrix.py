from typing  import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    """
    The function `searchMatrix` takes a matrix and a target integer as input, and returns True if the
    target is found in the matrix, and False otherwise.
    
    :param matrix: The matrix parameter is a 2D list of integers. It represents a matrix where each row
    is a list of integers
    :type matrix: List[List[int]]
    :param target: The target parameter is the integer value that we are searching for in the matrix
    :type target: int
    :return: a boolean value indicating whether the target integer is found in the matrix.
    """
    res = [ele for row in matrix for ele in row]
    left = 0
    right = len(res) - 1
    while left <= right:
        mid = (left + right) // 2
        if res[mid] == target:
            return True
        
        if res[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False
