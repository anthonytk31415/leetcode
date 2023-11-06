# DP: create up, left, right, down; 
# create running sum; run across i, j


def trapRainWater(heightMap):

    # create up, left, down , right matrices 
    dp_up = [[x for x in y] for y in heightMap]
    for j in range(len(dp_up[0])):
        for i in range(len(dp_up) - 2, -1, -1):
            dp_up[i][j] = max(dp_up[i][j], dp_up[i+1][j])
                
    dp_down = [[x for x in y] for y in heightMap]
    for j in range(len(dp_down[0])):
        for i in range(1, len(dp_down)):
            dp_down[i][j] = max(dp_down[i][j], dp_down[i-1][j])

    dp_left = [[x for x in y] for y in heightMap]
    for i in range(len(dp_left)):
        for j in range(1, len(dp_left[0])):
            dp_left[i][j] = max(dp_left[i][j], dp_left[i][j-1])

    dp_right = [[x for x in y] for y in heightMap]
    for i in range(len(dp_right)):
        for j in range(len(dp_right[0])-2, -1, -1):
            dp_right[i][j] = max(dp_right[i][j], dp_right[i][j+1])

    res = 0
    dp_res = [[0 for x in y] for y in heightMap]
    for i in range(len(heightMap)):
        for j in range(len(heightMap[0])):
            res += min(dp_up[i][j], dp_down[i][j], dp_left[i][j], dp_right[i][j]) - heightMap[i][j]
            dp_res[i][j] = min(dp_up[i][j], dp_down[i][j], dp_left[i][j], dp_right[i][j]) - heightMap[i][j]

    print('hm:', heightMap)
    print('up:', dp_up)
    print('dn:', dp_down)
    print('lt:', dp_left)
    print('rt:', dp_right)
    print(dp_res)
    return res

# heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]

heightMap = [[12,13,1,12],
             [13,4,13,12],
             [13,8,10,12],
             [12,13,12,12],
             [13,13,13,13]]


print(trapRainWater(heightMap))