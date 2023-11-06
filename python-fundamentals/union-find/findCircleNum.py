# findCircleNum
# union find question

# Number of Provinces

#union find - return the total number of unique sets

# define your graph
# then instantiate: 
# n cities for ith city 
# create: 
# --> parent = array from 0 to i -1
# --> 
# for each i,j in isConnected = 1 --> do parent_i = find(i), parent_j = find(j)
# then union the two if the parents are not equal
# then count the number of unique i's in the parent array

#1245; 1:16am
# struggled with a bit of syntax and also, at the end you could have parents that don't 
# point to the "prime parent"; so write that in your logic

## below is a union find method

def find(parent, i):
    if parent[i] != i:
        return find(parent, parent[i])
    else: 
        return parent[i] 

def union(parent, i, j):
    parent[j] = i

def findCircleNum(isConnected): 
    parent = []
    for i in range(len(isConnected)):
        parent.append(i)
    
    for i in range(len(isConnected)):
        for j in range(i+1, len(isConnected)):
            if isConnected[i][j] == 1:
                p_i = find(parent, i)
                p_j = find(parent, j)
                if p_i != p_j:
                    union(parent, p_i, p_j)
    ans = set()
    for i in range(len(parent)):
        ans.add(find(parent, i))
    return len(ans)

# print(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
# print(findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))
# x 0,0
# 0,3
# x 1,1
# 1,2
# - 2,1
# x 2,2
# 2,3
# - 3,0
# - 3,2
# x 3,3



### can also answer this with num of connected components
## number of connected components/DFS below

# isconnected is n x n matrix
def findCircleNum2(isConnected):
    visited = set()
    processed = set()
    res = 0

    def dfs_helper(isConnected, visited, processed, u):
        visited.add(u)
        for j in range(len(isConnected)):
            v = isConnected[u][j]
            if j not in visited and v == 1:
                dfs_helper(isConnected, visited, processed, j) 
        processed.add(u)

    for u in range(len(isConnected)):
        if u not in processed: 
            res +=1
            dfs_helper(isConnected, visited, processed, u)

    return res

print(findCircleNum2([[1,1,0],[1,1,0],[0,0,1]]))
print(findCircleNum2([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))


print(findCircleNum2([[1,0,0],[0,1,0],[0,0,1]]))