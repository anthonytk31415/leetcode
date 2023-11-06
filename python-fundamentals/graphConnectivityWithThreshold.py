### first find if a common divisor z > threshold exists for each vertex 

## conditions: for 2 integers a, b:
## if max(a,b)> threshold --> False
## iterate from i == range(min(a,b, threshold + 1) to max(a,b) + 1)
## if a % i == 0 and b % i == 0: --> Build a connector


#currently, this is too slow; 

from collections import defaultdict

# the trick is to apply union find using the Sieve of Eratosthenes. 
# Iterate over pairs from x = (threshold + 1, n), y = (x+x, n, step = x)
# and apply union if the parents are not the same; this guarantees that y is divisible by x and you dont
# iterate multiple times 


def find(i, parent):
    if parent[i] != i: 
        return find(parent[i], parent)
    else: 
        return i

def union(p_i, p_j, parent, rank):
    if rank[p_i] > rank[p_j]:
        parent[p_j] = p_i
        rank[p_i] += rank[p_i]
    else: 
        parent[p_i] = p_j
        rank[p_j] += rank[p_i]

def areConnected(n, threshold, queries):
    ## first build the edges from your divisors > threshold 
    parent = [i for i in range(n+1)]
    rank = [1 for _ in range(n+1)]

    for x in range(threshold + 1, n+1):
        for y in range(x+x, n+1, x):
            p_x = find(x, parent)
            p_y = find(y, parent)
            if p_x != p_y: 
                union(p_x, p_y, parent, rank)
    
    ## now build the res by confirming whether for each edge[i] = [u,v], if u,v, share the same parent, then True
    res = [False for x in queries]
    for i in range(len(queries)): 
        u,v = queries[i]
        res[i] = (find(u, parent) == find(v, parent))
    
    return res

n = 6
threshold = 2
queries = [[1,4],[2,5],[3,6]]

# n = 6
# threshold = 0
# queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]

# n = 5
# threshold = 1
# queries = [[4,5],[4,5],[3,2],[2,3],[3,4]]

print(areConnected(n, threshold, queries))


## then once you have all of your connectors (edges of the graph), now do union find for each edge 

