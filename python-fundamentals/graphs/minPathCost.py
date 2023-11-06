# https://leetcode.com/problems/minimum-path-cost-in-a-grid/description/

# 1:45; finished 3:29pm

# did basically djikstras with some modifications; took a long ass time to coordinate the setup of the vertices with the costs

# mxn integer grid 

# 0 to m*n-1 distinct integers

# grid = list
# moveCost = 

# Time: O(m*n) - iterate over each node before factoring the min function; that makes it (m*n)^2 but maybe better if we apply a heap
# Space: O(m*n) for info on each node


from math import inf
from collections import defaultdict

class Graph:
    def __init__(self, grid, moveCost):
        self.m = len(grid)
        self.n = len(grid[0])
        self.g = grid
        self.mc = moveCost   

        self.mc_helper = {}
        ## adjacency list set up
        # set up mc: 
        for i in range(self.m):
            for j in range(self.n):
                self.mc_helper[self.g[i][j]] = (i,j)


    def minDist(self, dist, visited):
        min, minIndex = inf, None
        for v in range(len(dist)):
            if not visited[v] and dist[v] < min: 
                min = dist[v]
                minIndex = v
        return minIndex

    def minPathCost(self):
        visited = [False] * len(self.mc)
        dist = [inf] * len(self.mc)
        for x in self.g[0]:                     # instantiate the first row ;then relax vertices subsequently
            dist[x] = x
        
        for _ in range(len(self.mc)):
            u = self.minDist(dist, visited)
            visited[u] = True
            u_row, u_col = self.mc_helper[u]
            for v_col in range(len(self.g[0])):
                v_row = u_row + 1
                if v_row < self.m:
                    v = self.g[v_row][v_col]
                    if not visited[v] and dist[v] > dist[u]+self.mc[u][v_col] + v:
                        dist[v] = dist[u]+self.mc[u][v_col] + v
        
        # take min dist of the vertices in the last row
        resMin = inf
        for v in self.g[-1]:
            if dist[v] < resMin: 
                resMin = dist[v]
        return resMin


# grid = [[5,3],[4,0],[2,1]] 
# moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]


grid = [[5,1,2],[4,0,3]]
moveCost = [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]]

g = Graph(grid, moveCost)
print(g.mc_helper)
m = g.minPathCost()
print(m)

    # At teh end take the min dist of the last row of grid