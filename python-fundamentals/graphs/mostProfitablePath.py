from collections import defaultdict, deque
from math import inf 

# We do BFS Twice. 

# We also so a trick where we write BFS once and implement logic to capture the appropriate gate amount. 
# We run BFS first with Bob, and we write a synthetic "time" array representing time that the other person got to that node. 
# We put all entries at inf so when Bob runs, he gets all of the values. (we really dont care what values bob gets)
# To ensure we only have real times for Bob's path to 0, we write a Parent array and at the end of building the tree, 
# if i is not in the bob->0 path, we mark that i's Time as Inf to guarantee that Alice takes all of the value. 

# When we run BFS on Alice, we feed into the function Bob's time (called timeBob). When we visit a node, 
# if Alice's visit time < Bob's, then we take the the value, and same logic for == time, etc.

# we basically traverse all nodes and edges twice. Once for Alice. Once for Bob. 
# Time = O(V+E); Space = O(V + E) for adjacency list

def mostProfitablePath1(edges, bob, amount):

    graph = defaultdict(list)
    for u, v in edges: 
        graph[u].append(v)
        graph[v].append(u)
    print(graph)

    aliceTimeDummy = [inf] * len(graph)

    def bfs(start, otherTime):
        parent = [None]*len(graph)
        time = [inf]*len(graph)
        visited = set()

        visited.add(start)
        parent[start] = -1          # -1 for parent = start; None = never visited
        time[start] = 0

        queue = deque([[start, amount[start], time[start]]])
        maxValue = -inf
        while queue: 
            u, curVal, curTime = queue.popleft()
            candidates = [x for x in graph[u] if x not in visited] 
            if candidates: 
                for v in candidates:
                    visited.add(v)
                    parent[v] = u
                    time[v] = curTime + 1

                    newVal = curVal
                    if time[v] < otherTime[v]:
                        newVal += amount[v]
                    elif time[v] == otherTime[v]:
                        newVal += amount[v]/2

                    queue.append([v, newVal, curTime + 1])
            else: 
                # this is a terminal value, i.e. empty candidates
                maxValue = max(maxValue, curVal)

        return [parent, time, maxValue]

    parentBob, timeBob, maxValueBob = bfs(bob, aliceTimeDummy)
    bobPath = set([bob])
    cur = 0

    # clean up Bob's path not leading to 0
    while parentBob[cur] != -1: 
        bobPath.add(cur)
        cur = parentBob[cur]
    for i in range(len(timeBob)):
        if i not in bobPath: 
            timeBob[i] = inf

    parentAlice, timeAlice, maxValueAlice = bfs(0, timeBob)

    return int(maxValueAlice)



# Here's the Lee implementation. Really short but also, a bit of a recursive mindfuck. 
# It's a complex implementation, but a really good test of understanding how DFS works. 

# The intuition is as you traverse DFS, when you call DFS for the first time, you get results from the "future" calls and work backwards. 
# In this case, we rely on DFS to find where bob is, and then percolate bob's distance to the ith place where we currently are. 
# We know our (Alice's) distance: it's just 1 + our previous distance, which we'll provide in our function call. 
# In our DFS calls, to pick up our maximum route, when we DFS our candidates, we'll take the max of those routes. 
# To find the distance to Bob, we'll take the min of our DFS candidates. One path will have Bob. The others will be inf. 
# 

# Important definitions. 
# d0 is the dist from 0 to i
# dBob is dist from i to bob
# iterate over the candidates for traversal
# when you dfs, you'll eventually hit bob, or you dont 
# Think as you start from 0: there's one path that hits where bob starts. The rest of the paths don't hit it. 
# so those paths that don't hit Bob will have infinite distance due to DFS and how we dont hit nodes that have been 
# visited. 

# instantiate res = -inf and take the smallest of the res when we dfs i's candidates. We use -inf because we want to hit 
# the largest res that might be negative. 
def mostProfitablePath(edges, bob, amount):

    graph = defaultdict(list)
    for u, v in edges: 
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(i, d0):
        res = -inf
        dBob = 0 if i == bob else inf
        for j in graph[i]:
            if j not in visited: 
                visited.add(j)
                curRes, curDBob = dfs(j, d0 + 1)
                res = max(curRes, res)
                dBob = min(dBob, curDBob)
        if res == -inf: res = 0
        if d0 < dBob: res += amount[i]
        if d0 == dBob: res +=  amount[i] // 2
        return res, dBob + 1

    visited.add(0)
    return dfs(0, 0)[0]
    

edges = [[0,1],[1,2],[1,3],[3,4]]
bob = 3
amount = [-2,4,2,-4,6]


print(mostProfitablePath1(edges, bob, amount))