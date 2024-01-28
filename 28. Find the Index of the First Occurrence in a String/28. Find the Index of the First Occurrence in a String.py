def strStr(self, hay: str, needle: str) -> int:
    length = len(needle)
    if length > len(hay):
        return -1
    i = 0
    while i <= len(hay):
        if hay[i:i+length] == needle:
            return i
        i += 1
    return -1
