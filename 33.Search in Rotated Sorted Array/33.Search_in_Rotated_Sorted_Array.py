from typing import List


def search(nums: List[int], target: int) -> int:
    """
    The function `search` performs a binary search on a rotated sorted array to find the index of a
    target element, returning -1 if the target is not found.
    
    :param nums: The `nums` parameter is a list of integers
    :type nums: List[int]
    :param target: The target parameter is an integer that represents the value we are searching for in
    the given list of integers
    :type target: int
    :return: the index of the target element in the given list of integers. If the target element is not
    found, it returns -1.
    """
    
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # If the left half is sorted
        if nums[left] <= nums[mid]:
            # Check if the target is within the sorted left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # If the right half is sorted
        else:
            # Check if the target is within the sorted right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
         