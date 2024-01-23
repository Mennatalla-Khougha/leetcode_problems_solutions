from typing import List


def is_overlap(a: List, b: List) -> bool:
    """
    The function `is_overlap` checks if two lists `a` and `b` overlap by comparing their first and last
    elements.
    
    :param a: List a is a list containing two elements. The first element represents the starting point
    of a range, and the second element represents the ending point of the range
    :type a: List
    :param b: The parameter `b` is a list
    :type b: List
    :return: a boolean value, indicating whether the two input lists, `a` and `b`, overlap or not.
    """
    return a[0] <= b[1] and b[0] <= a[1]


def merge_overlap(a: List[int], b: List[int]) -> List[int]:
    """
    The function `merge_overlap` takes two lists of integers as input and returns a new list that merges
    the overlapping range of the two input lists.
    
    :param a: a is a list of integers
    :type a: List[int]
    :param b: The parameter `b` is a list of integers
    :type b: List[int]
    :return: The function `merge_overlap` returns a list containing the minimum value of the first
    elements of the input lists `a` and `b` as the first element, and the maximum value of the second
    elements of the input lists `a` and `b` as the second element.
    """
    return [min(a[0], b[0]), max(a[1], b[1])]


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    The function takes a list of intervals and merges any overlapping intervals into a single interval.
    
    :param intervals: The parameter `intervals` is a list of lists, where each inner list represents an
    interval. Each inner list contains two integers, representing the start and end points of the
    interval
    :type intervals: List[List[int]]
    :return: The function `merge` returns a list of merged intervals.
    """
    intervals.sort(key = lambda i : i[0])
    merge = [intervals[0]]
    for i in intervals[1:]:
        if is_overlap(merge[-1], i):
           merge[-1] = (merge_overlap(merge[-1], i))
        else:
            merge.append(i)
    return merge