

## do dfs on helper function; when there's nowhere to go, go to the next one
## if the color fails, stop and do another color
## this is a backtracking problem on all the colors


# return true all paths are traversed and have a color assigned to them

# 11:00

#Time: O(V+E)
# Space: O(V+E)

from collections import defaultdict

def gardenNoAdj(n, paths):
    # do 0-indexed
    graph = defaultdict(list)
    for (u,v) in paths:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)


    ## pass on flower and visited in each new dfs iteration

    def dfs(u, flower, visited):
        visited[u] = True
        possible_flowers = set([1,2,3,4])                                   # check for adjacent flowers to find the right flower for u
        for v in graph[u]:          
            if visited[v] == True and flower[v] in possible_flowers:         
                possible_flowers.remove(flower[v])                          # remove all flowers adjacent to u
        # take out a remaining flower (it doesnt matter)
        flower[u] = possible_flowers.pop()
        for v in graph[u]:                                                  # now traverse to the next v that is not visited            
            if visited[v] == False: 
                dfs(v, flower, visited)

    visited = [False]*n
    flower = [None]*n

    # iterate across all n vertices manually, to ensure you get all of the disconnected components
    for i in range(n):
        if visited[i] == False: 
            dfs(i, flower, visited)

    return flower

# n = 3
# paths = [[1,2],[2,3],[3,1]]

n = 4
paths = [[1,2],[3,4]]

print(gardenNoAdj(n, paths))