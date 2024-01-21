from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    """
    The function `findMedianSortedArrays` takes two sorted lists of integers as input and returns the
    median of the combined sorted list.
    
    :param nums1: nums1 is a list of integers representing a sorted array
    :type nums1: List[int]
    :param nums2: The parameter `nums2` is a list of integers
    :type nums2: List[int]
    :return: the median of the two sorted arrays as a float.
    """
    res = nums1 + nums2
    res.sort()
    length = len(res)
    mid = (length - 1) // 2

    if length % 2 == 0 :
        m = (res[mid] + res[mid + 1]) / 2
    else:
        m = res[mid]

    return m
