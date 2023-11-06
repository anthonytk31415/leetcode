# course schedule

# does this graph have back edges? 

# this is checking for back edges of a graph 
# - assign the DFS "colors": 0=undiscovered, 1=discovered, 2=processed
# - run through all possible nodes (i.e. range of numCourses) that are not processed (color != 2)
# - build DFS that runs recursively for each node, then it's children, then when the children are processed, mark it completed
# - to encounter a backedge, you'll have to get to a node that is disovered (color=1)

# Time: O(V+E)
# Space: O(V+E)

from collections import defaultdict

def canFinish(numCourses, prerequisites):

    status = {'cycle': False, 'visited': [0]*numCourses}
    graph = defaultdict(list)
    for [u,v] in prerequisites: 
        graph[u].append(v)
    
    def dfs(u, graph, status):
        if status['cycle'] == True:
            return 
        if status['visited'][u] ==1:
            status['cycle'] = True
        if status['visited'][u] ==0:
            status['visited'][u] = 1
            for v in graph[u]:
                dfs(v, graph, status)
            status['visited'][u] = 2

    for i in range(numCourses):
        if status['cycle'] == True:
            break
        if status['visited'][i] !=2:
            dfs(i, graph, status)
            
    if status['cycle'] == True:
        return False
    else: 
        return True

p = [[1,0],[2,0],[3,1],[3,2]]
# p = [[1,0], [0,1]]
print(canFinish(4, p))

