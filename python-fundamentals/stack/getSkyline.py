from collections import deque
from math import inf 

# def getSkyline(buildings):

    # res = []                # insert left most corner [x, height]
    # stack = []              # top contains the tallest element; [right, height]; the stack needs sto be in a descending staircase 
    # stack.append([0, inf])  
    # curHeight = 0

    # for i, b in enumerate(buildings): 
    #     left, right, height = b

    #     # handle insertion: 
    #     if height > curHeight: 
    #         res.append([left, height ])
    #         curHeight = height
    #     # pop elements from the stack with smaller height and index, since largest one last dominates; smaller and longer are OK
    #     while stack: 
    #         topRight, topHeight = stack[-1] 
    #         if topHeight <= height and topRight <= right: stack.pop()
    #         else: break 

    #     # if this is the larest element 


    #     # pop and put in res the elements that are less than the next i
    #     if i < len(buildings) - 1: 
    #         while stack and stack[-1][0] < buildings[i+1][0]:
    #             topRight, topHeight = stack.pop() 
    #             res.append([topRight, stack[-1][1]])

    #     # for the last entry
    #     if i == len(buildings) - 1: 
    #         while len(stack) > 1:
    #             topRight, topHeight = stack.pop() 
    #             res.append([topRight, stack[-1][1]])

    # return res



from heapq import heappush, heappop 

def mergeInterval(u, v):
    a, b, c = u
    x, y, z = v
    if x <= a and b <= y and z >= c: 
        return [x, y, z]


def getSkyline(buildings):
    buildings.sort(key = lambda x: (x[0], x[2]))
    # print(buildings)

    newBuildings = []
    newBuildings.append(buildings[0])
    for i in range(1, len(buildings)):
        a, b, c = newBuildings[-1]
        x, y, z = buildings[i]
        if x <= a and b <= y and z >= c: 
            newBuildings.pop()
            newBuildings.append([x,y,z])
        else: 
            newBuildings.append([x,y,z])



    buildings = newBuildings
    res = []                # insert left most corner [x, height]
    queue = []              # top contains the tallest element; [right, height]; the stack needs sto be in a descending staircase 

    for i, b in enumerate(buildings):
        # print("queue: {}, res: {}, i: {}, b: {}".format(queue, res, i, b))
        left, right, height = b
        if not res or res[-1][1] < height: res.append([left, height])
        heappush(queue, [-height, right])

        while queue and ((i == len(buildings)- 1) or (queue[0][1] < buildings[i+1][0])):
            curHeight, curRight = heappop(queue)
            curHeight = -curHeight
            if curRight <= res[-1][0]: continue
            if queue: 
                while queue and queue[0][1] <= curRight:  
                    heappop(queue)
            if queue and -queue[0][0] < res[-1][1]: res.append([curRight, -queue[0][0]])
            elif not queue: res.append([curRight, 0])
        
    return res 

# buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# buildings = [[0,2,3],[2,5,3]]
buildings = [[1,2,1],[1,2,2],[1,2,3]]
buildings = [[1,20,1],[1,21,2],[1,22,3]]


buildings = [[3,7,8],[3,8,7],[3,9,6],[3,10,5],[3,11,4],[3,12,3],[3,13,2],[3,14,1]]
print(getSkyline(buildings))