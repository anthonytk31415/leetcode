

# https://leetcode.com/problems/minimum-falling-path-sum-ii/description/


# can you use a monotonic stack? 

# for the first row, and for trivial matrices with 1 row, just take the min of the current path

# each iteration (starting at i = row 1 onward): 
# build a monotonic (increasing) stack of the previous row
# iterate across each column j: 
# - evict the stack[0] element if the index == j
# - dp = min from the monotonic stack (stack[0]) + current entry 
# add the element back into the stack, maintaining the monotonic stack property


# return min of last row


from collections import deque

def minFallingPathSum(grid):

    for i in range(1, len(grid)):
        stack = deque()
        for j in range(len(grid[0])):
            while stack and grid[i - 1][j] < grid[i - 1][stack[-1]]:
                stack.pop()
            stack.append(j)

        for j in range(len(grid[0])):
            if stack[0] == j: 
                stack.popleft()
                        
            grid[i][j] = grid[i - 1][stack[0]] + grid[i][j]
            
            while stack and grid[i - 1][j] < grid[i - 1][stack[-1]]:
                stack.pop()
            stack.append(j)
    return min(grid[-1])

grid = [[7]]
# grid = [[1,2,3],[4,5,6],[7,8,9]]

print(minFallingPathSum(grid))