# findMinArrowShots

# trick: 
# - sort by ending point 
# - keep track of a cur pointer; and instantiate it with the first part of the 
#   array; 
# - this is because that is the latest point that can break that balloon and the next
#   one; if they ovelap, then that arrow can break both
# - if that arrow "doesn't" break the next balloon, you need a new arrow


# Time: O(nlogn) for sorting the points array
# Space: O(1)

def findMinArrowShots(points):
    points.sort(key=lambda x: x[1])
    cur = points[0][1]
    arrows = 1
    print(points)
    for i in range(1, len(points)):
        s, e = points[i]
        print(f'{s}, {e}, {cur}')
        if not (s <= cur <= e): 
            arrows +=1
            cur = e
    return arrows

# points = [[1,2],[2,3],[3,4],[4,5]]

points = [[10,16],[2,8],[1,6],[7,12]]
print(findMinArrowShots(points))