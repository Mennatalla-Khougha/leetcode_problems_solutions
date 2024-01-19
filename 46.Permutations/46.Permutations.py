from typing import List


def permute(self, nums: List[int]) -> List[List[int]]:
    """
    The `permute` function uses a depth-first search algorithm to generate all permutations of a given
    list of numbers.
    
    :param nums: The `nums` parameter is a list of integers. It represents the numbers for which we want
    to generate all possible permutations
    :type nums: List[int]
    :return: The function `permute` returns a list of lists, where each inner list represents a
    permutation of the input `nums` list.
    """
    result = []
    def dfs(perm, flags):
        """
        The above function implements a depth-first search algorithm to generate all permutations of a given
        list of numbers.
        
        :param perm: The `perm` parameter is a list that represents the current permutation being
        constructed. It starts as an empty list and elements are added to it as the algorithm explores
        different paths in the search tree. Once a complete permutation is found, it is added to the
        `result` list
        :param flags: The `flags` parameter is a list that keeps track of whether each element in the `nums`
        list has been used in the current permutation. It is used to avoid using the same element multiple
        times in a single permutation. Each element in the `flags` list corresponds to an element in the `
        :return: The function `dfs` does not explicitly return anything. However, it modifies the `result`
        list by appending permutations to it.
        """
        if len(perm) == len(nums):
            result.append(perm[:])
            return
        
        for i in range(len(nums)):
            if not flags[i]:
                perm.append(nums[i])
                flags[i] = True
                dfs(perm, flags)
                perm.pop()
                flags[i] = False
        
    flags = [False] * len(nums)
    dfs([], flags)
    return result