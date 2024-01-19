from typing import List


def letterCombinations(digits: str) -> List[str]:
    """
    The `letterCombinations` function generates all possible combinations of characters from a given set
    of digits using backtracking.
    
    :param digits: The `digits` parameter is a string that represents a sequence of digits. Each digit
    corresponds to a set of characters. For example, the digit "2" corresponds to the characters "a",
    "b", and "c". The function `letterCombinations` generates all possible combinations of characters
    from
    :type digits: str
    :return: The function `letterCombinations` returns a list of strings, which represents all possible
    combinations of characters that can be formed from the given `digits` string.
    """
    hashMap = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    result = []
    comb = []
    
    def backtrack(idx):
        """
        The function `backtrack` generates all possible combinations of characters from a given set of
        digits.
        
        :param idx: The parameter `idx` is the index of the current digit in the `digits` string. It is used
        to keep track of which digit we are currently considering while generating all possible combinations
        :return: The function `backtrack` does not explicitly return anything. However, it appends
        combinations to the `result` list.
        """
        if len(comb) == len(digits):
            result.append("".join(comb))
            return
        for i in range(len(hashMap[digits[idx]])):
            comb.append(hashMap[digits[idx]][i])
            backtrack(idx + 1)
            comb.pop()

    if digits:
        backtrack(0)
    return result
