# Count Unreachable Pairs of Nodes in an Undirected Graph

# 9:00


# n nodes : 0 -> n-1
# edges = [a_i, b_i] [ith edge]
#pairs of diff nodes that are unreachable 


# 1: get connnected compnoents length of each component
# 2: return # combinations of connected components length
# trick for speedy combination math: 
# - count # of nodes traversed in each connected DFS. Call it c.
# - That c will be paired with all the other current found nodes. so total pairs increments by totalNodes*c
# - do that step at every iteration to get totap pairs


# you can also do union find here. each connnected component is a set. Then
# count the number of members in each set. Then find the "pairs of each distinct set". 



## ok this is too long; how do I make it quicker? 
# def combo(arr):
#     if len(arr) == 1: 
#         return 0
#     else:
#         res = 0
#         for x in arr[1:]:
#             res = res + arr[0] * x
#         return res + combo(arr[1:])


from collections import defaultdict

def countPairs(n, edges):

    graph = defaultdict(list)
    for u in range(n):
        graph[u] = list()
    for e0, e1 in edges: 
        graph[e0].append(e1)
        graph[e1].append(e0)

    visited = {}
    processed = {}
    counter = {'counter': 0}
    def dfs_helper(visited, processed, u, counter):
        visited[u] = True
        counter['counter'] +=1
        for v in graph[u]: 
            if v not in visited:
                dfs_helper(visited, processed, v, counter)
        processed[u] = True

    count = 0
    totalNodes = 0
    for i in range(n):
        if i not in processed: 
            counter = {'counter': 0}
            dfs_helper(visited, processed, i, counter)

            count += totalNodes*counter['counter']
            totalNodes +=counter['counter']
    
    return count

n = 7
edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]

# n = 5
# edges = [[1,0],[3,1],[0,4],[2,1]]

print(countPairs(n, edges))


a = [4,1,2]



print(combo(a))