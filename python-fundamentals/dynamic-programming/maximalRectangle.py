from math import inf 

# This is an application of a monotonic stack, similar to 84. Largest Rectangle in Historgram, with a twist.
# Where as previously, we had heights of a histogram where the starting point (say the "ground") is the same.
# Now we have a matrix and in each row, the heights are potentially different. So we calculate the height 
# per row and then run the same (84) O(n) algoritm for each row of varying heights. 

# Time: O(m*n)
# Space: O(m*n)


def maximalRectangle(matrix):
    matrix = [[int(x) for x in row] + [0] for row in matrix]
    heights = [[0 for _ in row] for row in matrix]

    # build the heights from bottom up
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                if i == 0: 
                    heights[i][j] = 1
                else: 
                    heights[i][j] = 1 + heights[i-1][j]
            else:
                heights[i][j] = 0
    
    maxRect = 0
    for i in range(len(matrix)):
        stack = [-1]
        for j in range(len(matrix[0])):
            while stack and heights[i][j] < heights[i][stack[-1]]:
                height = heights[i][stack.pop()]
                width = j - stack[-1] - 1
                maxRect = max(maxRect, height * width)
            stack.append(j)
    return maxRect     


## Test cases:

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

# matrix = [["1","0"],["1","0"]]

# matrix = [["0","0","1","0"],
#           ["0","0","1","0"],
#           ["0","0","1","0"],
#           ["0","0","1","1"],
#           ["0","1","1","1"],
#           ["0","1","1","1"],
#           ["1","1","1","1"]]
print(maximalRectangle(matrix))


# a = [1]
# b = [2, 3]
# print(a + b)