def findTheDifference(s: str, t: str) -> str:
    t = sorted(t)
    s = sorted(s)
    
    for i in range(len(s)):
        if s[i] != t[i]:
            return t[i]
    
    return t[-1]