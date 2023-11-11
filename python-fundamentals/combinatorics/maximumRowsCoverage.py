from itertools import combinations


arr = [x for x  in range(5)]

# 5 choose 3 -> 10 combinations
res = list(combinations(arr, 3))
print(len(res))


a = set([1,2,3])
b = set([2])
c = set([4])

print(a - b)
print(b | c) # union 

def maximumRows(matrix, numSelect):
    cols = len(matrix[0])
    allCols = set([x for x in range(len(matrix[0]))])
    allRows = set([x for x in range(len(matrix))])      # set of all rows in matrix
    colCombos = list(combinations(allCols, numSelect))
    rowsInCol = {}                                      # given a col, what row has a 1

    # all rows minus  col from rowInCol for each remaining col will give you total number of rows that have coverage

    maxCoverage = 0
    print(colCombos)
    for combo in colCombos: 
        colsLeft = allCols - set(combo)
        print(colsLeft)
        allRows = set([x for x in range(len(matrix))])  
        for col in colsLeft: 
            if col not in rowsInCol: 
                rows = set([])
                for i in range(len(matrix)):
                    if matrix[i][col] == 1: 
                        rows.add(i)
                rowsInCol[col] = rows
            # take the 
            allRows -= rowsInCol[col]
        maxCoverage = max(maxCoverage, len(allRows))
    return maxCoverage


# matrix = [[0,1,1], [0,1,0], [0,0,1]]
# numSelect = 2


matrix = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]]
numSelect = 2
print(maximumRows(matrix, numSelect))


