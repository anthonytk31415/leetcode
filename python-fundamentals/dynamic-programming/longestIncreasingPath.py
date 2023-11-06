from functools import lru_cache

# time: O(n), 
# space: O(n) for the cache
# traverse the matrix at each step, you'll find the longest increasing path. 
# dfs when you can travel to a larger neighbor
# when you hit a cell that you visited, that cell's longest path is in memory so add it to yours 
# note that by traveling in "longest increasing", your path is a dag 

def longestIncreasingPath(matrix):
    m, n = len(matrix), len(matrix[0])
    # visited = set()

    @lru_cache(None)
    def helper(i,j):
        print(i,j)
        # visited.add((i,j))
        max_candidates = [1]
        for u, v in [(i + 1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= u < m and 0 <= v < n and matrix[u][v] > matrix[i][j]:
                # print('i,j:', (i, j), 'u,v:', (u,v))
                cur_candidate = 1 + helper(u,v)
                max_candidates.append(cur_candidate)
        print((i,j), max_candidates)
        return max(max_candidates)

    overall_max = 1
    for i in range(m):
        for j in range(n):
            # if (i,j) not in visited: 
            cur_max = helper(i,j)
            overall_max = max(overall_max, cur_max)
    
    return overall_max

# matrix = [[9,9,4],[6,6,8],[2,1,1]]
# matrix = [[3,4,5],[3,2,6],[2,2,1]]
matrix = [[1]]
print(longestIncreasingPath(matrix))