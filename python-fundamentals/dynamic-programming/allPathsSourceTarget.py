

def allPathsSourceTarget(graph):
    res = []

    def dfs(graph, path, res, src):
        # print(path, res)
        if src == len(graph)-1:
            res.append(path)
            return 
        for v in graph[src]:
            dfs(graph, path + [v], res, v)
    
    dfs(graph, [0], res, 0)
    return res

# graph = [[1,2],[3],[3],[]]
graph = [[4,3,1],[3,2,4],[3],[4],[]]

print(allPathsSourceTarget(graph))