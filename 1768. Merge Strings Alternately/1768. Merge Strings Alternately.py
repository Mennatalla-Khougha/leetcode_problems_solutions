def mergeAlternately(word1: str, word2: str) -> str:
    length = max(len(word1), len(word2))
    res = []
    
    for i in range(length):
        # check if the index is in bound
        if i < w1:
            res.append(word1[i])
            
        # check if the index is in bound
        if i < w2:
            res.append(word2[i])
    res = "".join(res)
    return res