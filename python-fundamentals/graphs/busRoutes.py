# min buses

# Time: O(m*n) for building the adjacency list; n length of routes, m length of largest bus route
# Space: O(n) for n routes 

# a = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
b = [[1,2,7],[3,6,7]]
# create an adjacency list 

from collections import defaultdict, deque, Counter
from math import inf

def numBusesToDestination(routes, source, target):
    if source == target: 
        return 0
    graph = defaultdict(list)           # each ith entry in list will be (route, cost)
    
    # each node is the ith entry of routes 
    # each bus stop simply means there's a connection to another node if a stop is shared in the node array 
    # do breadth first search from your starting source

    # i in routes, j in matching route, u is the bus route  

    # in this setup , you have the option of starting wherever "node" you want as long as the bus connects; you'll run bfs on each of those
    # starting points and for each end candidate you'll chose the min



    from collections import Counter
    all_nums = []
    for x in routes: 
        all_nums += x 

    counter_nums = Counter(all_nums)

    updated_routes = []
    for x in routes: 
        insert = []
        for num in x: 
            if counter_nums[num] > 1: 
                insert.append(num)
        updated_routes.append(insert)
    print(updated_routes)


    for i in range(len(updated_routes)):
        for u in updated_routes[i]:
            for j in range(i+1, len(updated_routes)):
                # print(i, j)
                if u in updated_routes[j]:
                    graph[i].append(j)
                    graph[j].append(i)

    print(graph)
    # src and end are arrays of possible starting/ending points
    src, end = [], []
    i = 0
    for i in range(len(routes)): 
        if source in routes[i]: src.append(i)
        if target in routes[i]: end.append(i)

    print(src, end)
    # write bfs with one start and series of ends and return the min path across all ends
    def bfs(graph, start, end):
        dist = [inf]*len(updated_routes)
        visited = [False]*len(updated_routes)
        processed = [False]*len(updated_routes)
        dist[start] = 1
        visited[start] = True
        q = deque()
        q.append(start)
        while q: 
            u = q.popleft()
            for v in graph[u]:
                if not visited[v]: 
                    dist[v] = dist[u] + 1
                    visited[v] = True
                    # print(f'u: {u}, v:{v}, dist: {dist[v]}')
                    q.append(v)
            processed[u] = True 

        min = inf
        for e in end: 
            if dist[e] < min: 
                min = dist[e]
        return min
    
    #### Main program ###
    # iterate across all src points: 
    res_min = inf
    for start in src: 
        start_min = bfs(graph, start, end)
        if start_min < res_min: 
            res_min = start_min

    if res_min == inf: 
        return -1
    else: 
        return res_min

# print(numBusesToDestination(a, 15, 12)) # -1 exppected


c = [[0,1,6,16,22,23],[14,15,24,32],[4,10,12,20,24,28,33],[1,10,11,19,27,33],[11,23,25,28],[15,20,21,23,29],[29]]
# print(numBusesToDestination(b, 1, 6))
print(numBusesToDestination(c, 4, 21))        # 2 expected

# i = 2 (4) to (20) i = 5