# requires 3x3 matrix
def isMagic(grid):
    # check horiz
    for i in range(len(grid)):
        cur_sum = 0
        for j in range(len(grid[0])):
            cur_sum += grid[i][j]
        if cur_sum != 15:
            return False

    # check vert
    for j in range(len(grid[0])):
        cur_sum = 0
        for i in range(len(grid)):
            cur_sum += grid[i][j]
        if cur_sum != 15:
            return False
    # check diag
    if grid[0][0] + grid[1][1] + grid[2][2] != 15: return False
    if grid[0][2] + grid[1][1] + grid[2][0] != 15: return False

    return True

grid = [[4,3,8], [9, 5, 1], [2,7,6]]

# print(isMagic(grid))

def numMagicSquaresInside(grid):
    counter = 0
    for i in range(len(grid) - 2):
        for j in range(len(grid[0]) - 2):
            subgrid = []
            for row in [0,1,2]:
                subgrid.append(grid[i + row][j:j+3])
            # print(subgrid)
            if isMagic(subgrid):
                counter +=1
    return counter

grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]

print(numMagicSquaresInside(grid))