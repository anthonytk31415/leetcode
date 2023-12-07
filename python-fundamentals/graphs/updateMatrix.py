# start with all the zeroes and process them. Then process its neighbors if they haven't been processed as 1. 
# then process those neighbors if not processed as 2. Etc. 

from collections import deque

# optimized O(1) space 
# O(mn) Time (m rows, n cols)

# We find all 0's and we enqueue them. For others, encode as -1 as "not visited".
# Pop the queue. Relax its neighbors if it hasn't been visited and define mat(neighbor) = cur + 1

def updateMatrix(mat): 
    queue = deque()
    # gather all zeroes
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0: 
                queue.append((i, j))
            else: 
                mat[i][j] = -1

    while queue: 
        i, j = queue.popleft()
        for u, v in [(i + 1, j), (i - 1, j), (i, j+1), (i, j-1)]:
            if 0 <= u < len(mat) and 0 <= v < len(mat[0]) and mat[u][v] == -1: 
                queue.append((u, v))
                mat[u][v] = mat[i][j] + 1
    return mat

mat = [[0,0,0],
       [0,1,0],
       [1,1,1],
       [1,1,1]
       ]


print(updateMatrix(mat))
# [[0,0,0],
#  [0,1,0],
#  [1,1,1], 
#  [1,0,1]]