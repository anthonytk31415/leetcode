from heapq import heappush, heappop

def furthestBuilding(heights, bricks, ladders):

    bricksReq = [0]*len(heights)
    for i in range(1, len(heights)):
        bricksReq[i] = max(0, heights[i] - heights[i-1])
    
    maxL= [0] * len(heights)
    heap = []
    heapSum = 0
    for i, num in enumerate(bricksReq): 
        # print(i, heap, heapSum)
        if len(heap) < ladders: 
            heappush(heap, num)
            heapSum += num
        else: 
            if ladders > 0 and num > heap[0]:
                heapSum -= heappop(heap)
                heapSum += num
                heappush(heap, num)
        maxL[i] = heapSum

    curSum = 0
    maxIdx = 0

    for i, heapSumI in enumerate(maxL):
        curSum += bricksReq[i]
        if curSum - heapSumI <= bricks: 
            maxIdx = i
        else: 
            break
    print(bricksReq, maxL)
    return maxIdx




heights = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2

heights = [14,3,19,3]
bricks = 17
ladders = 0

heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1

heights = [7,5,13]
bricks = 0
ladders = 0

print(furthestBuilding(heights, bricks, ladders))