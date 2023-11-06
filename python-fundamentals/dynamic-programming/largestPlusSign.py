# <!-- https://leetcode.com/problems/largest-plus-sign/ -->

# first create the matrix
# create left, right, up, down
# 
def orderOfLargestPlusSign(n, mines):
    grid = [[1 for _ in range(n) ] for _ in range(n)]
    for (x,y) in mines: 
        grid[x][y] = 0
    
    up = [[0 for _ in range(n)] for _ in range(n)]
    # create up; start at lastrow -> first row; 
    for i in range(n-1, -1, -1):
        for j in range(n):
            if i == n-1:
                if grid[i][j] == 1: up[i][j] = 1
            else:  
                if grid[i][j] == 1: up[i][j] = 1 + up[i+1][j]

    down = [[0 for _ in range(n)] for _ in range(n)]
    # create down; start from first row to last row; 
    for i in range(n):
        for j in range(n):
            if i == 0:
                if grid[i][j] == 1: down[i][j] = 1
            else:  
                if grid[i][j] == 1: down[i][j] = 1 + down[i-1][j]

    left = [[0 for _ in range(n)] for _ in range(n)]
    # create down; start from first row to last row; 
    for i in range(n):
        for j in range(n): # range(n-1, -1, -1)
            if j == 0:
                if grid[i][j] == 1: left[i][j] = 1
            else:  
                if grid[i][j] == 1: left[i][j] = 1 + left[i][j-1]

    right = [[0 for _ in range(n)] for _ in range(n)]
    # create down; start from first row to last row; 
    for i in range(n):
        for j in range(n-1, -1, -1):
            if j == n-1:
                if grid[i][j] == 1: right[i][j] = 1
            else:  
                if grid[i][j] == 1: right[i][j] = 1 + right[i][j+1]

    res = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1: 
                cur = 1
                valid_sides = True
                sides = []
                for x, y, dir in [(i-1, j, down), (i+1, j, up), (i, j+1, right), (i, j-1, left)]:
                    if 0 <= x < n and 0 <= y < n: 
                        sides.append(dir[x][y])
                    else: 
                        valid_sides = False
                        break 
                if valid_sides == True and len(sides) == 4: 
                    cur += min(sides)
                print(i, j, sides, cur)
                res = max(res, cur)

    return res

n = 5
mines = [[4,2]]
print(orderOfLargestPlusSign(n, mines))