
from collections import defaultdict
def validPath(n, edges, source, destination):

    ## build graph as a adjacency list
    graph = defaultdict(list)
    for (u,v) in edges: 
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False]*n
    status = [False]

    def dfs(graph, u, visited, status):
        if status[0] == True: 
            return 
        visited[u] = True

        if u == destination: 
            status[0]= True

        for v in graph[u]:
            if not visited[v]:
                dfs(graph, v, visited, status)

    ## do dfs until you visit destination; if you reach end, return false
    dfs(graph, source, visited, status)
    return status[0]

# n = 3
# edges = [[0,1],[1,2],[2,0]]
# source = 0
# destination = 2

# n = 6
# edges = [[0,1],[0,2],[3,5],[5,4],[4,3]] 
# source = 0
# destination = 5

n = 10
edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
source = 5
destination = 9

print(validPath(n, edges, source, destination))