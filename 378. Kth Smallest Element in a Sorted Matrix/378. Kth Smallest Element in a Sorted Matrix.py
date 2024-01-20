from typing import List


def kthSmallest(matrix: List[List[int]], k: int) -> int:
    """
    The function `kthSmallest` takes a matrix of integers and an integer `k` as input, and returns the
    kth smallest element in the matrix.
    
    :param matrix: The parameter `matrix` is a 2D list of integers. It represents a matrix where each
    row is a list of integers
    :type matrix: List[List[int]]
    :param k: The parameter `k` represents the position of the element we want to find in the sorted
    matrix. It is an integer value
    :type k: int
    :return: the kth smallest element in the given matrix.
    """
    res = [i for row in matrix for i in row]
    res.sort()
    return res[k - 1]
    