# findball

## 

def findBall(grid):
    def findBallIndiv(grid, i):
        if not grid:
            return i
        curRow = grid[0]
        if curRow[i] == 1 and i+1 < len(curRow) and curRow[i] == curRow[i+1]:
                return findBallIndiv(grid[1:], i+1)
        if curRow[i] == -1 and i-1 >= 0 and curRow[i] == curRow[i-1]:
                return findBallIndiv(grid[1:], i-1)
        else: 
            return -1


    entry = set(range(len(grid[0])))
    return [findBallIndiv(grid, i) for i in entry]
    

# grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
print(findBall(grid))