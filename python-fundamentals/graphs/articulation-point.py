# An Articulation Point is a vertex in a graph that, when removed, makes other vertices unreachable. 
# A Bridge is an edge that, when removed, makes other vertices unreachable. 
# assumes the initial graph is connected and this implementation uses a adjacency list

# The Strategy: 
# - keep track of parent, enter time, time, visited, low, articulation point, and Bridge  
#   - for low, this is the lowest enter time possible from vertex u 
# - do DFS on any starting node
#   - keep track of number of children
#   - for v each child of u: 
#       - recursively call helper; 
#       - update low[u] = min(low[u], low[v])                           (note recursively, low[v] will have been assigned)
#       - if v not visited: conditions for (1) root AP, (2) non-root AP, (3) Bridge 
#           (1) if parent = -1 and children > 1 --> AP
#           (2) if not parent == -1 and low[v] >= enter[u] --> AP       (logic: the child can't get to anywhere before the parent)
#           (3) if low[v] > enter[u] --> Bridge                         
#       - if v visited and v is not the parent of u: 
#           - low[u] = min(low[v], enter[v])


from collections import defaultdict
from math import inf 



## let's reindex them for the algo from 0-5 in an adjacency list


def ap_helper(u, graph, visited, enter, low, parent, ap, time, bridges): 
    visited[u] = True
    children = 0                # used for articulation points for the root
    enter[u] = time[0]
    low[u] = time[0]
    time[0] +=1

    for v in graph[u]:
        if not visited[v]:
            parent[v] = u
            children +=1
            ap_helper(v, graph, visited, enter, low, parent, ap, time, bridges)
            low[u] = min(low[u], low[v])
            if parent[u] == -1 and children > 1:                           # is root and > 1 child? 
                ap[u] = True
            if parent[u] != -1 and low[v] >= enter[u]:                     # Can child reach a lower or equal entry than parent? --> AP
                ap[u] = True    
            if low[v] > enter[u]:                                          # Bridge Cond: can child reach strictly lower entry than parent?
                bridges.append([u,v])
        elif v != parent[u]:                                               # only consider back-edges; not the parent; if you do, it's nonsensical
            low[u] = min(low[u], enter[v])                                 

def articulation_point(graph, v):
    visited = [False] * v       
    print('visited', visited)
    enter = [inf] * v           # enter times from dfs
    low = [inf] * v             # lowest enter time possible for a given u
    parent = [-1] * v
    ap  = [False] *v            # store articulation points
    bridges = []                # store bridges here
    time = [0]                  #array of time so that it is accessible in all recursive calls

    ap_helper(0, graph, visited, enter, low, parent, ap, time, bridges) 

    return ap, bridges


## indexed 1 through 6
edges = [[0,1],[1,2],[2,0],[1,3]]


graph = defaultdict(list)
for u,v in edges: 
    graph[u].append(v)
    graph[v].append(u)

n = 4
print(articulation_point(graph, n))