from typing import List


def findMin(nums: List[int]) -> int:
    """
    The function `findMin` takes a list of integers as input, sorts the list in ascending order, and
    returns the minimum value.
    
    :param nums: A list of integers
    :type nums: List[int]
    :return: the minimum value from the given list of integers.
    """
    
    nums.sort()
    return nums[0]
