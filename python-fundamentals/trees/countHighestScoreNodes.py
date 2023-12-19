# create numNodes[i] for each node i

# Now go through each node i. 
# You need to now get the partitions after removing i. 

# Look at p_i = parent of i. that partition's length = numNodes[p_i] - numNodes[i]
# The other two: Leftchild[i], RightChild[i]

from collections import defaultdict

def countHighestScoreNodes(parents):

    children = defaultdict(list)
    for i in range(len(parents)):
        children[parents[i]].append(i)

    numNodes = [0]*len(parents)

    def dfs(node):
        res = 1
        if children[node]: 
            for child in children[node]:
                res += dfs(child)
        numNodes[node] = res
        return res

    dfs(0)
    countMax = 0
    maxScore = -1
    for i in range(len(numNodes)):
        curScore = 1
        if numNodes[0] - numNodes[i] > 0: 
            curScore *= numNodes[0] - numNodes[i]
        for child in children[i]:
            curScore *= numNodes[child]
        if curScore > maxScore: 
            countMax = 1
            maxScore = curScore 
        elif curScore == maxScore: 
            countMax += 1
    return countMax

# parents = [-1,2,0,2,0]
parents = [-1,2,0]
print(countHighestScoreNodes(parents))