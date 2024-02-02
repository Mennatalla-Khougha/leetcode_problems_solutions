from typing import List


def sequentialDigits(low: int, high: int) -> List[int]:
    """
    Find all numbers between 'low' and 'high' that contain digits in sequential order without any gaps.

    Args:
        low (int): The lower bound of the range to search within.
        high (int): The upper bound of the range to search within.

    Returns:
        List[int]: A sorted list of integers that are within the specified range and have digits in sequential order.

    Example:
        sequentialDigits(10, 100) would return [12, 23, 34, 45, 56, 67, 78, 89].
    """
    res = []
    for i in range(1, 10):
        num = i
        j = i + 1
        while num <= high and j < 10:
            num = num * 10 + j
            if low <= num <= high:
                res.append(num)
            j += 1
    res.sort()
    return res
