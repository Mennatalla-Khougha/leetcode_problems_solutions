from typing import List
def combine(self, n: int, k: int) -> List[List[int]]:
    """
    The function `combine` generates all possible combinations of `k` numbers from the range 1 to `n`.
    
    :param n: The parameter `n` represents the range of numbers from 1 to `n` from which we can choose
    elements to form combinations
    :type n: int
    :param k: The parameter `k` represents the number of elements in each combination
    :type k: int
    :return: a list of lists, where each inner list represents a combination of numbers from 1 to n,
    with length k.
    """
    result = []
    def backtrack(start, comb):
        """
        The function `backtrack` generates all combinations of length `k` from the numbers `start` to `n`
        and stores them in the `result` list.
        
        :param start: The `start` parameter represents the starting index for the backtracking algorithm. It
        determines the range of values that can be added to the combination `comb`
        :param comb: The parameter "comb" is a list that represents the current combination of numbers. It
        starts as an empty list and elements are added to it as the function backtracks through the numbers
        :return: The function does not explicitly return anything. However, it appends combinations to the
        "result" list.
        """
        if len(comb) == k:
            result.append(comb.copy())
            return
        for i in range(start, n + 1):
            comb.append(i)
            backtrack(i + 1, comb)
            comb.pop()
    backtrack(1, [])
    return result
