
# for each dfs "loop", visited = set() i.e. an empty set
# dfs through each node
# for each node, check whether all of the paths are 
# if the path is empty then mark that node as terminal; track safe: safe[i] = None
#   len(graph[node]) == 0
# now traverse each node
# if you go to a visited node, then it is not terminal and you can break the loop
# if that node you want to visit is not safe, then mark unsafe and then stop


def eventualSafeNodes(graph):
    safe = [None] * len(graph)      # None = we dont know; 0 = not safe; 1 = safe

    def dfs(node):
        visited.add(node)
        if safe[node] == 1 or len(graph[node]) == 0: # the current node is safe or terminal (which is safe) and returns true
            safe[node] = True
            return True

        # now check if all other nodes in graph are safe; 
        # if not, terminate and return False then mark the node is not safe
        for x in graph[node]:
            if (x in visited and not safe[x]) or not dfs(x): 
                safe[node] = False
                return False 
        safe[node] = True
        return True

    for i in range(len(graph)):
        if safe[i] == None: 
            visited = set()
            dfs(i)

    res = []
    for i in range(len(graph)):
        if safe[i] == True: res.append(i)

    return res


# graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]

graph = [[],[0,2,3,4],[3],[4],[]]
# graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(eventualSafeNodes(graph))