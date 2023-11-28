# This is n^2 log n Time, but you can probalby do a n^2 using a monotonic stack

# using a sort
def largestSubmatrix1(matrix):

    heights = [[x for x in row] for row in matrix]
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
    for i in range(len(heights)):
        heights[i].sort()
        for j in range(len(heights[0])):
            height = heights[i][j]
            width = len(heights[0]) - j
            maxRect = max(maxRect, height * width)

    return maxRect


# using a monotonic stack; can't do it; you must use a sort to get the ordering shifts correct
def largestSubmatrix(matrix):

    heights = [[x for x in row] + [0] for row in matrix]
    for i in range(len(matrix)):
    
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1: 
                if i == 0: 
                    heights[i][j] = 1
                else: 
                    heights[i][j] = 1 + heights[i-1][j]
            else: 
                heights[i][j] = 0
    # print(heights)
    maxRect = 0

    for i in range(len(heights)):
        stack = [-1]
        for j, jHeight in enumerate(heights[i]):
            print("Stack", stack)
            while stack and jHeight < heights[i][stack[-1]]:
                
                height = heights[i][stack.pop()]
                width = j - stack[-1] - 1
                # print("i {}, height {}, width {}".format(i, height, width))
                maxRect = max(maxRect, height * width)

            stack.append(j)
    return maxRect

# matrix = [[1,0,1,0,1]]
matrix = [[1,1,0],[1,0,1]]
# matrix = [[0,0,1],[1,1,1],[1,0,1]]
# matrix[2].sort()
print("ans:", largestSubmatrix(matrix))