from collections import Counter
# https://leetcode.com/problems/equal-row-and-column-pairs/solutions/2324688/cubic-432-vs-three-map-95-vs-trie-137/?envType=daily-question&envId=2023-10-21
# can rewrite with a trie and a three-map

def equalPairs(grid):


    # transform the rows into tuples and then count them

    grid_tuples = [tuple(row) for row in grid]
    countRows = Counter(grid_tuples)
    res = 0
    for j in range(len(grid[0])):
        column = [] 
        for i in range(len(grid)):
            column.append(grid[i][j])
        
        column = tuple(column)
        res += countRows[column]
    return res

# grid = [[3,2,1],[1,7,6],[2,7,7]]
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(equalPairs(grid))