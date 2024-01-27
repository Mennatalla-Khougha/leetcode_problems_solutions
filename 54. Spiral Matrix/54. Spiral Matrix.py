def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result = []
    row, col = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, row, 0, col 
    while left < right and top < bottom:
        # loop through the top row then incremenate it 
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1
        
        # loop through the right column then decreminate it
        for i in range(top, bottom):
            result.append(matrix[i][right - 1])
        right -= 1
        
        # check all element haven't been visited 
        if not (left < right and top < bottom):
            break
        
        # loop through the bottom row then decreminate it
        for i in range(right - 1, left - 1, -1):
            result.append(matrix[bottom - 1][i])
        bottom -= 1
        
        # loop through the left column then increminate it
        for i in range(bottom - 1, top - 1, -1):
            result.append(matrix[i][left])
        left += 1     
        
    return result 