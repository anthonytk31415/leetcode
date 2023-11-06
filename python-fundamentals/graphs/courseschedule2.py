# findOrder
# prereq = array
# numcourses

# topological sort with cycle detection

# - for topological sort, you will call the recursive fn on all nodes if it is not processed
# - you'll apply DFS using "colors" (0 = undiscovered, 1=discovered, 2=processed)
# - for the recursive function, you'll then call the fn on all of the current's node's children (i.e. the prerequisites)
# - normallly for DFS, you'll only run the function on non-visited nodes. But since you want to catch back edges, you'll run them and check for the BE's. 
# - you'll append the result in a list as the complete to signify the completed object as you progress the DFS 
# - key insight is you'll use DFS to go through the pre-requisites 
# 

# - if a cycle exists, then it is impossible to complete a class so return []
#     - to identify a cycle, if you visit a node and it has already been visited (but not processed) through a backtrack, you have a backedge
#     - for cycle detection, you'll mark a flag = true if cycle detected and you'll break the recursive loop 
# 
# time: O(V+E)
# complexity: O(V+E)

from collections import defaultdict, deque

def findOrder(numCourses, prerequisites):
    status= {'cycle': False, 'visited': [0]*numCourses, 'res':[]}
    graph = defaultdict(set)
    for p in prerequisites:
        (a,b) = p
        graph[a].add(b)

    #create the dfs function that will also check for cycles
    def dfs(u, graph, status):
        if status['cycle'] == True:
            return
        if status['visited'][u]==1:
            status['cycle'] = True
        if status['visited'][u]==0:
            status['visited'][u] = 1
            for v in graph[u]:
                dfs(v, graph, status)
            status['visited'][u] = 2
            status['res'].append(u)
    # cycle through all the courses with DFS; 
    # if you've identified a cycle, 
    for i in range(numCourses):
        if status['cycle']: break
        if status['visited'][i] != 2:
            dfs(i, graph, status)

    #check if status == True
    if status['cycle']:
        print('cycle found')
        return []
    else: 
        return status['res'] 



# def findOrder(numCourses, prerequisites):
#     status = {'res': deque()} # once a course is completely explored append it to the array

#     graph = defaultdict(list)
#     for edge in prerequisites:
#         u, v = edge[1], edge[0]
#         graph[u].append(v)

#     visited = set()

#     def dfs(node, graph, visited, status):
#         visited.add(node)
#         for v in graph[node]:
#             if v not in visited:
#                 dfs(v, graph, visited, status)
#         status['res'].appendleft(node)
    
#     for u in list(graph):
#         if u not in visited: 
#             dfs(u, graph, visited, status)

#     allcourses = set(range(numCourses))
#     for x in status['res']:
#         if x not in allcourses:
#             return []
#     single_classes = []
#     for y in allcourses:
#         if y not in status['res']:
#             single_classes.append(y)
#     status['res'] = single_classes + list(status['res'])
#     return status['res']

# p = [[1,0],[2,0],[3,1],[3,2]]
p = [[1,0],[0,1]]
# p = []
print(findOrder(2, p))