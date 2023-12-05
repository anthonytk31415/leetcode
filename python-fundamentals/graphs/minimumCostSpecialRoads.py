from heapq import heappush, heappop
from collections import defaultdict



# A simple BFS with a priority queue but fails due to TLE since we consider each move of one direction in the + grid. 
def minimumCostBFS(start, target, specialRoads):
    dist = {}  ## cells = (i, j, 0); specialRoads = (i, j, 1)
    startX, startY = start
    targetX, targetY = target
    minX, maxX = min(startX, targetX), max(startX, targetX)
    minY, maxY = min(startY, targetY), max(startY, targetY)

    portals = defaultdict(list)
    for stX, stY, endX, endY, cost in specialRoads: 
        portals[(stX, stY)].append([endX, endY, cost])
        minX, maxX = min(minX, stX, endX), max(maxX, stX, endX)
        minY, maxY = min(minY, stY, endY), max(maxY, stY, endY)

    queue = [(0, startX, startY)]

    while queue: 
        curCost, x, y = heappop(queue)

        # if you're at the end, terminate 
        if [x, y] == target: return curCost

        # if x, y is in the starting portal: 
        if (x, y) in portals: 
            for u, v, moveDist in portals[(x, y)]:
                if ((u,v) not in dist) or (curCost + moveDist < dist[(u,v)]):
                    heappush(queue, (curCost + moveDist, u, v))
                    dist[(u, v)] = curCost + moveDist

        for u, v in [(x + 1, y), (x - 1, y), (x ,y - 1), (x , y + 1)]:
            if minX <= u <= maxX and minY <= v <= maxY and (((u,v) not in dist) or (curCost + 1 < dist[(u,v)])): 
                heappush(queue, (curCost + 1, u, v))
                dist[(u, v)] = curCost + 1

    return False


# This is a floyd warshall extension, but still gets TLE. 
# We use the Floyd Warshall extension because if we take a portal, we need to find the shortest path to that portal's starting point
# and the shortest path from ending portal to the target. 
# But it's still a O(N^3) operation for N nodes. 

def minimumCostFW(start, target, specialRoads):
    start, target = tuple(start), tuple(target)
    nodes = set([tuple(x) for x in [start, target] + [[u, v] for u, v, _, _, _ in specialRoads] + [[x, y] for _, _, x, y,  _ in specialRoads]])
    dist = {}    

    # instantiate distance with no portals with the taxicab distance
    for u in nodes: 
        x0, y0 = u
        for v in nodes: 
            x1, y1 = v
            dist[(u, v)] = abs(x0 - x1) + abs(y0 - y1) 

    # introduce a specialRoad and find min distance between u, v
    for x2, y2, x3, y3, cost in specialRoads:                 
        m = (x2, y2)
        n = (x3, y3)
        for u in nodes: 
            x0, y0 = u
            for v in nodes: 
                x1, y1 = v
                if u != v: 
                    dist[(u, v)] = min(dist[(u, v)], dist[(u, m)] + cost + dist[(n, v)])

    # at the end, now find the min path from u to v while introducing a node w  
    for w in nodes: 
        x2, y2 = w
        for u in nodes: 
            x0, y0 = u
            for v in nodes: 
                x1, y1 = v
                if u != v and u != w and v != w: 
                    dist[(u, v)] = min(dist[(u, v)], dist[(u, w)] + dist[(w, v)])
    return dist[(start, target)] 

# Here's the updated priority queue/BFS Implementation . It's similar to Djikstra.
# for each heappop, you perform relaxation on all nodes. 
# To save time, make sure you only enqueue if the point has not been evaluated or if it yields a lower total cost. 
# Time: O(n^2 log n)
# Space: O(n)

def minimumCost(start, target, specialRoads):
    start, target = tuple(start), tuple(target)
    allPoints = set([start, target])
    dist = {}
    portals = defaultdict(list)
    for stX, stY, endX, endY, cost in specialRoads: 
        portals[(stX, stY)].append([endX, endY, cost])
        allPoints.add((stX, stY))
        allPoints.add((endX, endY))

    startX, startY = start
    queue = [(0, startX, startY)]
    dist[start] = 0

    while queue: 
        curCost, x, y = heappop(queue)
        # if you're at the end, terminate 
        if (x, y) == target: return curCost

        # if x, y is in the starting portal: 
        if (x, y) in portals: 
            for u, v, moveDist in portals[(x, y)]:
                if ((u,v) not in dist) or (curCost + moveDist < dist[(u, v)]):
                    heappush(queue, (curCost + moveDist, u, v))
                    dist[(u, v)] = curCost + moveDist

        for u, v in allPoints: 
            curDist = abs(u - x) + abs(v - y)
            if (u, v) not in dist or curCost + curDist < dist[(u, v)]: 
                heappush(queue, (curCost + curDist, u, v))
                dist[(u, v)] = curCost + curDist

    return False


# start = [1,1]
# target = [4,5]
# specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]

start = [3,2]
target = [5,7]
specialRoads = [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]

start = [1,1]
target = [7,9]
specialRoads = [[1,3,1,9,1],[1,9,7,8,5],[1,3,4,2,5],[5,5,7,5,4]]

print(minimumCost(start, target, specialRoads))