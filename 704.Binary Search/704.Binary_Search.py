from typing import List


def search(nums: List[int], target: int) -> int:
    """
    The function `search` uses binary search to find the index of a target number in a sorted list of
    numbers.
    
    :param nums: The `nums` parameter is a list of integers
    :type nums: List[int]
    :param target: The target parameter is the value that we are searching for in the nums list
    :type target: int
    :return: the index of the target element in the given list of integers. If the target element is not
    found, it returns -1.
    """
    
    start = 0
    end = len(nums) - 1
    while start <= end:

        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if target > nums[mid]:
            start = mid + 1 
        else:
            end = mid - 1
    return -1
