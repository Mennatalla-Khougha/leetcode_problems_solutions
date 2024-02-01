from typing import List


def divideArray(nums: List[int], k: int) -> List[List[int]]:
    """
    Divides an array of integers into subarrays of three elements such
    that the difference between the maximum and minimum element in each
    subarray is less than or equal to a given value 'k'.

    Args:
        nums (List[int]): The input list of integers to be divided.
        k (int): The maximum allowed difference between the maximum and minimum element within each subarray.
    
    Returns:
        List[List[int]]: A list of subarrays, each containing exactly three elements. If it is not possible to create such subarrays, returns an empty list.
    """
    length = len(nums)
    nums.sort()
    res = []
    if length % 3 != 0:
        return []
    for i in range(0,length, 3):
        if nums[i + 2] - nums[i] > k:
            return []
        res.append([nums[i], nums[i + 1], nums[i + 2]])
    return res
