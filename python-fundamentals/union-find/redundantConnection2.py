
# Time: O(n)
# Space: O(n) for parents

## union 


## redundant connection
def find(parent, i):
    if parent[i] != i: 
        return find(parent, parent[i])
    else: 
        return i

def union(parent, p_i, p_j):
    parent[p_j] = p_i


# first detect if there are any edges that point to the same vertex; 
# if that happens, then one of those edges needs to be removed, but which one? 
# do union find with one edge. if no cycles, that youre OK
# if not, it's the other edge

# if dual-parents are found, then there's just one problematic cycle edge so remove it. 

# (1) node with no parents, but there's a cycle: so take the latest edge 
# (2) node with two parents - test for cycle  
#   (2a) if cycle, then take the other one
#   (2b) if no cycles with both, take the later one

# there will be a node that will have two edges. So a child will have two parents.
# Always take the second (later) edge. But test first if there's still a cycle. 



from collections import defaultdict

# if cycle detected, return the edge that caused it. 
# if not, return False. 
def union_find(parent, edges):
    cand = None
    for w in edges: 
        u,v = w
        p_u = find(parent, u)
        p_v = find(parent, v)
        if p_u == p_v: 
            cand = w
        elif p_u != p_v: 
            union(parent, p_u, p_v)
    if cand != None: 
        return cand
    else: 
        return False

def buildParent(n):
    parent = []
    for i in range(n):
        parent.append(i)
    return parent



def findRedundantDirectedConnection(edges):
    parent_c = defaultdict(list)
    index_1_c , index_2_c = None, None

    # test for finding a vertex with two parents
    for i in range(len(edges)): 
        u,v = edges[i]
        # print(u,v)
        if v not in parent_c: 
            parent_c[v].append(i)
        elif v in parent_c: 
            parent_c[v].append(i)
            index_1_c = parent_c[v][0]
            index_2_c = parent_c[v][1]
            break
    
    # (1) test cycle for node with two parents; check 2nd one first; if 
    # not a cycle, then return it; else return the earlier edge 
    if index_1_c!= None and index_2_c != None: 
        edge_c = edges[:index_2_c] + edges[index_2_c+1:]
        parent = buildParent(len(edges) +1)         ## indexed at 1, so keep 0 as just there
        if not union_find(parent, edge_c): 
            return edges[index_2_c]
        else: 
            return edges[index_1_c]

    # test for node with cycles: 
    # (3) cycle, 
    parent = buildParent(len(edges) +1) 
    return union_find(parent, edges)

    


# edges = [[1,2],[1,3],[2,3]]
edges =  [[1,2],[2,3],[3,4],[4,1],[1,5]] # 4,1
# edges = [[2,1],[3,1],[4,2],[1,4]]
print(findRedundantDirectedConnection(edges))