from heapq import heappush, heappop

def findScore(nums):
    score = 0

    marker = [0 for x in nums]
    heap = []
    for i, x in enumerate(nums):
        heappush(heap, ((x,i), i))

    print(heap)

    for _ in range(len(nums)):
        cur_val, i = heappop(heap)    
        print(cur_val, i)
        x, idx = cur_val

        if marker[i] == 0:
            score += x
            marker[i] = 1
            if i - 1 >= 0: marker[i-1] = 1
            if i+1 < len(marker): marker[i+1] = 1

    return score

# nums = [2,1,3,4,5,2]
# nums = [2,3,5,1,3,2]
nums = [5,1,1,7,2,4]
print(findScore(nums))