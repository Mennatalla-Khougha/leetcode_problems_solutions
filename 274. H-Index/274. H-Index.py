from typing import List


def hIndex(citations: List[int]) -> int:
    """
    The function `hIndex` takes in a list of citations and returns the h-index, which is the maximum
    value of h such that there are at least h papers with h or more citations.
    
    :param citations: The parameter "citations" is a list of integers representing the number of
    citations for each paper
    :type citations: List[int]
    :return: the h-index, which is a metric used to measure the impact and productivity of a researcher.
    """
    citations.sort()
    length = len(citations)
    h_index = 0
    
    for i in range(length):
        h_index = max(h_index, min(citations[i], length - i))
    
    return h_index
