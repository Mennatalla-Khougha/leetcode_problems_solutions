from typing import List
def subsets(self, nums: List[int]) -> List[List[int]]:
    """
    The function `subsets` takes a list of integers as input and returns all
    possible subsets of the input list.
    
    :param nums: The parameter `nums` is a list of integers
    :type nums: List[int]
    :return: a list of all possible subsets of the input list `nums`. Each subset
    is represented as a list of integers.
    """
    result = []
    comb = []
    
    def backtrack(idx):
        """
        The function `backtrack` generates all possible combinations of elements in the `nums` list using
        backtracking.
        
        :param idx: The parameter `idx` represents the current index of the `nums` list that we are
        considering. It is used to keep track of the progress of the backtracking algorithm
        :return: Nothing is being returned explicitly in this code. The function `backtrack` is being used
        to populate the `result` list with combinations of elements from the `nums` list.
        """
        if idx >= len(nums):
            result.append(comb.copy())
            return
        
        comb.append(nums[idx])
        backtrack(idx + 1)
        
        comb.pop()
        backtrack(idx + 1)
        
    backtrack(0)
    return result