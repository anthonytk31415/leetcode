from collections import deque
def minReorder(n, connections):
    
    visited = [False] * n
    changes = 0

    zeroes = set() # include all vertices that appropriately lead to 0
    zeroes.add(0)

    # iterate across connections 
    for _ in range(len(connections)):
        for i in range(len(connections)):
            if visited[i]: 
                continue
            u,v = connections[i] 
            # reverse and change 
            if u in zeroes:
                zeroes.add(v)
                connections[i] = [v, u]                
                visited[i] = True
                changes +=1
                break
            # continue
            elif v in zeroes:  
                zeroes.add(u)
                visited[i] = True
                break
    return changes 


roads = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(minReorder(6, roads))  ## 3

# roads = [[1,0],[1,2],[3,2],[3,4]]
# print(minReorder(5, roads))

# roads = [[1,0],[2,0]]
# print(minReorder(3, roads))