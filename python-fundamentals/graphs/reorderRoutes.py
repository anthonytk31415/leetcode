from collections import deque, defaultdict

# use hash tables of lists to find the order
# Time: O(n)
# Space: O(n)


def minReorder(n, connections):
    changes = 0
    first = defaultdict(list)
    second = defaultdict(list)
    q = deque()
    pairs = []
    visited = set()

    for u,v in connections: 
        if u == 0 or v == 0: 
            pairs.append([u,v])
        first[u].append(v)
        second[v].append(u)

    for u,v in pairs:
        if (u,v) not in visited:  
            if u == 0: 
                changes +=1; 
                q.append(v)
                visited.add((u,v))
            if v == 0: 
                q.append(u)
                visited.add((u,v))
    while q: 
        cur = q.popleft()

        if first[cur]:
            for v in first[cur]: 
                if (cur, v) not in visited:
                    visited.add((cur, v))
                    changes +=1
                    q.append(v)
        if second[cur]:
            for v in second[cur]:
                if (v, cur) not in visited:
                    visited.add((v, cur))
                    q.append(v)
    return changes 


# roads = [[4,3],[2,3],[1,2],[1,0]]
# print(minReorder(5, roads))  ## 2

roads = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(minReorder(6, roads))  ## 3

# roads = [[1,0],[1,2],[3,2],[3,4]]
# print(minReorder(5, roads))

# roads = [[1,0],[2,0]]
# print(minReorder(3, roads))