
#928; 944 before fol; 954


# create visited array for each vertex
# for a v, if you hit a visited vertex w, then for v!=w, anything w is a part of, so is v 

# traverse each vertex until all are visited in dfs fashion
# for each dfs, maintain the path, when you visit a v new vertex for the first time, that path is placed in the vertex's answer[v].
# then add v to that path and call v 

# for each v you visit, you'll then visit its children in dfs fashion 

# at the end, sort each answer[i] in ascending order

from collections import defaultdict, deque

# def getAncestors(n, edges):

#     graph = defaultdict(list)
#     for (u,v) in edges: 
#         graph[u].append(v)


#     visited = [False] * n
#     answer = [set() for _ in range(n)]
#     ancestorUpdate = []
#     def dfs(graph, u, visited, answer, path, ancestorUpdate): 
#         visited[u] = True
#         for v in graph[u]: 
#             if not visited[v]:
#                 answer[v] = set(list(answer[v]) + path)
#                 dfs(graph, v, visited, answer, path + [v], ancestorUpdate)
#             else: 
#                 answer[v] = set(list(answer[v]) + path)
#                 ancestorUpdate.append((path, v))
#     i = 0
#     while i < n: 
#         if all(visited): 
#             break
#         if not visited[i]:
#             dfs(graph, i, visited, answer, [i], ancestorUpdate)
#         i +=1

#     #anywhere 
#     for (path, v) in ancestorUpdate: 
#         for i in range(len(answer)): 
#             if v in answer[i]: 
#                 answer[i] = set(list(answer[i]) + path)

#     for i in range(len(answer)): 
#         answer[i] = list(answer[i])
#         answer[i].sort()
#     return answer 


## you can build this with a topological sort



# class Solution:
#     def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
#         #Use Kahn's algorithm of toposort using a queue and bfs!
#         graph = [[] for _ in range(n)]
#         indegrees = [0] * n
        
#         #Time: O(n^2)
#         #Space: O(n^2 + n + n) -> O(n^2)
        
#         #1st step: build adjacency list grpah and update the initial indegrees of every node!
#         for edge in edges:
#             src, dest = edge[0], edge[1]
#             graph[src].append(dest)
#             indegrees[dest] += 1
        
        
#         queue = deque()
#         ans = [set() for _ in range(n)]
#         #2nd step: go through the indegrees array and add to queue for any node that has no ancestor!
#         for i in range(len(indegrees)):
#             if(indegrees[i] == 0):
#                 queue.append(i)
        
#         #Kahn's algorithm initiation!
#         #while loop will run for each and every node in graph!
#         #in worst case, adjacency list for one particular node may contain all other vertices!
#         while queue:
#             cur = queue.pop()
            
#             #for each neighbor
#             for neighbor in graph[cur]:
#                 #current node is ancestor to each and every neighboring node!
#                 ans[neighbor].add(cur)
#                 #every ancestor of current node is also an ancestor to the neighboring node!
#                 ans[neighbor].update(ans[cur])
#                 indegrees[neighbor] -= 1
#                 if(indegrees[neighbor] == 0):
#                     queue.append(neighbor)
        
#         #at the end, we should have set of ancestors for each and every node!
#         #in worst case, set s for ith node could have all other vertices be ancestor to node i !
#         ans = [(sorted(list(s))) for s in ans]
#         return ans



def getAncestors(n, edges):
    answer = [set() for _ in range(n)]
    graph = defaultdict(list)
    n_ancestors = [0] *n            # keeps track of how many paths that vertex has; 
    for (u,v) in edges:             # if that vertex has no ancestors, we must start with it; 
        graph[u].append(v)          # in the dfs loop, if it has no more ancestors, we stop applying its ancestors
        n_ancestors[v] +=1
    
    q = deque()

    for w in range(len(n_ancestors)):           # add allfathers here
        if n_ancestors[w] == 0: 
            q.append(w)

    while q: 
        u = q.popleft()
        for v in graph[u]:
            answer[v].update([u])
            answer[v].update(answer[u])
            n_ancestors[v] -=1
            if n_ancestors[v] == 0: 
                q.append(v)
    
    for i in range(len(answer)):
        answer[i] = sorted(list(answer[i]))

    return answer



                         
# n = 8
# edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]

n = 6
edges = [[0,3],[5,0],[2,3],[4,3],[5,3],[1,3],[2,5],[0,1],[4,5],[4,2],[4,0],[2,1],[5,1]]

print(getAncestors(n, edges))