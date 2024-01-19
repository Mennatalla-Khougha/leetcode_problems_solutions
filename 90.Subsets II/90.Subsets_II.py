from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    """
    The function `subsetsWithDup` generates all possible subsets of a given list of integers, taking
    into account duplicate elements.
    
    :param nums: `nums` is a list of integers
    :type nums: List[int]
    :return: The function `subsetsWithDup` returns a list of lists, where each inner list represents a
    unique combination of elements from the input list `nums`.
    """
    nums.sort()
    result = []
    
    def backtracking(idx, comb):
        """
        The function `backtracking` generates all possible combinations of elements from a given list `nums`
        using backtracking.
        
        :param idx: The `idx` parameter represents the current index in the `nums` list that we are
        considering. It is used to keep track of our progress in the backtracking algorithm
        :param comb: The parameter `comb` is a list that represents the current combination of elements. It
        is initially empty and elements are added to it during the backtracking process
        :return: The function does not explicitly return anything. However, it modifies the global variable
        "result" by appending the combinations to it.
        """
        if idx == len(nums):
            result.append(comb.copy())
            return
        
        comb.append(nums[idx])
        backtracking(idx + 1, comb)
        comb.pop()
        
        while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
            idx += 1
            
        backtracking(idx + 1, comb)
        
    backtracking(0, [])
    return result
