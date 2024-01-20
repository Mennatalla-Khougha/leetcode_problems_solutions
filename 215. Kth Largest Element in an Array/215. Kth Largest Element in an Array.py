from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    """
    The function `findKthLargest` takes a list of integers `nums` and an integer `k`, sorts the list in
    ascending order, and returns the kth largest element.
    
    :param nums: The parameter "nums" is a list of integers
    :type nums: List[int]
    :param k: The parameter `k` represents the position of the largest element we want to find in the
    list `nums`
    :type k: int
    :return: the kth largest element in the given list of integers.
    """
    nums.sort()
    i = len(nums) - k
    return nums[i]
