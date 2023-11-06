from collections import defaultdict

def numOfMinutes(n, headID, manager, informTime):
    graph = defaultdict(list)
    for i, parent in enumerate(manager): 
        graph[parent].append(i)

    def dfs(node):
        res = informTime[node]
        
        if graph[node]:
            descendentsTimes = []
            for child in graph[node]:
                childTime = dfs(child)
                descendentsTimes.append(childTime)
            
            res += max(descendentsTimes)

        return res

    return dfs(headID) 

# n = 1
# headID = 0
# manager = [-1]
# informTime = [0]

n = 6
headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]

print(numOfMinutes(n, headID, manager, informTime))