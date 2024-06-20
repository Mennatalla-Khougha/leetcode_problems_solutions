def convert(s: str, numRows: int) -> str:
    """
    Converts the input string `s` into a zigzag pattern with `numRows` rows.

    Args:
        s (str): The input string to be converted.
        numRows (int): The number of rows in the zigzag pattern.

    Returns:
        str: The converted string in zigzag pattern.

    """
    if numRows == 1:
        return s
    result = [""] * numRows
    row = 0
    flag = 1
    
    for c in s:
        result[row] += c
        if row == 0:
            flag = 1
        elif row == numRows - 1 :
            flag = -1
        row += flag 
    
    return "".join(result)
