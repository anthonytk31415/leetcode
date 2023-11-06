class Graph: 
    def __init__(self, vertices):
        self.v = vertices
        self.g = [[0 for col in range(vertices)] for row in range(vertices)]
        self.time = 0

    def dfs(self, src):
        visited = [False]*self.v
        processed = [False]*self.v
        exit = [None]*self.v
        enter = [None]*self.v

        self.time = 0

        def dfs_helper(self, u, visited, processed, enter, exit):
            visited[u] = True
            self.time +=1
            enter[u] = self.time
            for v in range(len(self.g[u])):
                if self.g[u][v] > 0 and not visited[v]: 
                    dfs_helper(self, v, visited, processed, enter, exit)
            processed[u] = True
            self.time +=1
            exit[u] = self.time

        dfs_helper(self, src, visited, processed, enter, exit)
        return enter, exit


g = Graph(5)
g.g = [[0,1,1,0,0], 
       [1,0,0,1,0],
       [1,0,0,1,0],
       [0,1,1,0,1],
       [0,0,0,1,0], ]


print(g.dfs(0))



## strongly connected components: 
# (1) do dfs once
# (2) then take the transpose of the edges
# (3) then do dfs with ordering of the finish times from (1)
# the componets from (3) are the strongly connected components 