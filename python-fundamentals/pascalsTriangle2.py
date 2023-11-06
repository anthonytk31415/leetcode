def getRow(rowIndex):
    memo = {0: [1], 1: [1,1]}
    if rowIndex <= 1: 
        return memo[rowIndex]
    
    for i in range(2, rowIndex + 1):
        innerRow = [] 
        prevRow = memo[i-1]
        for j in range(1, len(prevRow)):
            innerRow.append(prevRow[j-1] + prevRow[j])

        memo[i] = [1] + innerRow + [1]
    return memo[rowIndex]

print(getRow(4))