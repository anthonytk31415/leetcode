from collections import deque, Counter

def validateBinaryTreeNodes(n, leftChild, rightChild):

    parent = [None for _ in range(n)]

    def dfs(u):
        if u in visited: 
            x[0] = False
            return 
        visited.add(u)
        for v in [leftChild[u], rightChild[u]]:
            # print(v, parent, "p_v", parent[v], "u: ", u)
            if v != -1: 
                if parent[v] == None: 
                    parent[v] = u
                    dfs(v)
                elif parent[v] != u: 
                    x[0] = False 
                    return

    for i in range(n):
        if parent[i] == None: 
            x = [True]
            visited = set()
            dfs(i)
            if x[0] == False: 
                return False

    count = Counter(parent)
    if count[None] != 1: return False
    return True



# n = 4
# leftChild = [1,-1,3,-1]
# rightChild = [2,3,-1,-1]



# n = 4
# leftChild = [1,-1,3,-1]
# rightChild = [2,-1,-1,-1]

# n = 6
# leftChild = [1,-1,-1,4,-1,-1]
# rightChild = [2,-1,-1,5,-1,-1]

# n = 4
# leftChild = [3,-1,1,-1]
# rightChild = [-1,-1,0,-1]


# n =4
# leftChild =[1,0,3,-1]
# rightChild = [-1,-1,-1,-1]

# n = 2
# leftChild =[1,0]
# rightChild =[-1,-1]

print(validateBinaryTreeNodes(n, leftChild, rightChild))