
# Union find approach: 

# take the edgeList and sort them by distance 
# then for each query in queries: 
# union find all edges that are less than the query distance 
# when you cannot do so any more, see if u, v of the query has the same parent. if so mark res[i] is true, else false 
# then move to the next query 

# from collections import defaultdict

# Space: O(n) for n 

def find(i, parent):
    if i != parent[i]:
        parent[i] = find(parent[i], parent)
    return parent[i]

def union(pi, pj, parent, rank):
    if rank[pi] < rank[pj]:
        parent[pi] = pj
        rank[pj] += rank[pi]
    else: 
        parent[pj] = pi
        rank[pi] += rank[pj] 

def distanceLimitedPathsExist(n, edgeList, queries):
    parent = [i for i in range(n)]
    rank = [1 for _ in range(n)]

    edgeList.sort(key = lambda x: x[2])
    query_q = []
    for i, x in enumerate(queries):
        u, v, w = x
        query_q.append((w, u, v, i))
    query_q.sort(key = lambda x: x[0])

    res = [False]*len(queries)
    e = 0       # e will keep track of which edge you are at

    for q in query_q: 
        q_wt, u, v, idx = q 
        while e < len(edgeList):
            cur_edge = edgeList[e]
            i, j, w = cur_edge
            if w < q_wt: 
                pi, pj = find(i, parent), find(j, parent)
                if pi != pj: 
                    union(pi, pj, parent, rank)
                e +=1
            else: 
                break  
        
        # see if u, v have the same parent
        pu, pv = find(u, parent), find(v, parent)
        if pu == pv: 
            res[idx] = True

    return res


# n = 3
# edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]]
# queries = [[0,1,2],[0,2,5]]

n = 5
edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]]
queries = [[0,4,14],[1,4,13]]

print(distanceLimitedPathsExist(n, edgeList, queries))