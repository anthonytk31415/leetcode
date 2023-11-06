
from collections import defaultdict
from math import inf 


def ap_helper(u, graph, visited, enter, low, parent, ap, time, a_edge): 
    visited[u] = True
    children = 0                # used for articulation points for the root
    enter[u] = time[0]
    low[u] = time[0]
    time[0] +=1

    for v in graph[u]:
        if not visited[v]:
            parent[v] = u
            children +=1
            ap_helper(v, graph, visited, enter, low, parent, ap, time, a_edge)
            low[u] = min(low[u], low[v])
            if parent[u] == -1 and children > 1: 
                ap[u] = True
            if parent[u] != -1 and low[v] >= enter[u]:          
                ap[u] = True    
            if low[v] > enter[u]:                                          #for critical edges, you only need to be able to NOT access as a child anything above parent
                a_edge.append([u,v])                                       # roots can have critical edges too (bridge = critical edge)
        elif v != parent[u]:                                               # only consider back-edges; not the parent; if you do, it's nonsensical
            low[u] = min(low[u], enter[v])

def criticalConnections(edges, v):
    # if len(edges) == 1: 
    #     return edges
    visited = [False] * v       
    enter = [inf] * v           # enter times from dfs
    low = [inf] * v             # lowest enter time possible for a given u
    parent = [-1] * v
    ap  = [False] *v            # store articulation points
    a_edge = []
    time = [0]                  #array of time so that it is accessible in all recursive calls

    graph = defaultdict(list)
    for u,v in edges: 
        graph[u].append(v)
        graph[v].append(u)

    ap_helper(0, graph, visited, enter, low, parent, ap, time, a_edge) 
    print(ap)
    return a_edge


## indexed 1 through 6
# edges = [[0,1],[1,2],[2,0],[1,3]]
# criticalConnections(edges, 4)



edges = [[0,1]]
print(criticalConnections(edges, 2))

# edges = [[1,0],[2,0],[3,2],[4,2],[4,3],[3,0],[4,0]]
# print(criticalConnections(edges, 5))