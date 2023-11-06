from heapq import heappop, heappush 

# put each point in a heap
# pop them out k times 

# Time: O(n log n) for n points
# Space: O(n) 

def kClosest(points, k):
    def dist(x, y):
       return ((x)**2 + (y)**2)**(1/2)

    queue = []
    for point in points:
        x,y = point
        heappush(queue, (dist(x,y), (x,y)))

    res = []
    for _ in range(k):
        dist, point = heappop(queue)
        res.append(list(point))
    return res

points = [[3,3],[5,-1],[-2,4]]
k = 2

print( kClosest(points, k))