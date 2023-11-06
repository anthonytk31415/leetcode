
from collections import deque
from heapq import heappush, heappop

# Trick: 
# - use sort your "info" based in capital (keep corresponding profit)

# - do this k times: 
#     - at each step, add all of the projects where capital <= w. add this in a max heap 
#     - then grab the one with the highest profit (heappop from max heap)

# space: O(n) for keeping track of n = length of profits in a queue
# time: O(nlogn) for sorting and manipulating the priority queue

# my first attemp below at a dynamic programming solution; it did not work, nor was it fast - it was n^2 in the attempt and failed. 

# def findMaximizedCapital(k, w, profits, capital): 
#     if k > len(profits): k = len(profits)

#     info = list(zip(profits, capital))
#     info.sort(key = lambda x: x[1])
#     info = [(0,0)x for x in info]

    # dp = [w] + [w for _ in range(k)]
    # availCapital = [w] + [w for _ in range(k)]

    # for i in range(1, len(profits)):
    #     for j in range(1, k + 1):
    #         if j > i: 
    #             dp[j] = dp[j-1]
    #             availCapital[j] = availCapital[j-1]
    #         elif availCapital[j-1] >= capital[i]:
    #             dp[j] = max(dp[j], dp[j-1] + profits[i])
    #             availCapital[j] = availCapital[j-1] + profits[i]
    # return dp[-1]

def findMaximizedCapital(k, w, profits, capital): 
    queue = []
    info = list(zip(profits, capital))
    info.sort(key = lambda x: x[1])
    info = deque(info)

    # if k > len(profits): k = len(profits)

    for _ in range(k):
        while info: 
            if info[0][1] <= w: 
                x = info.popleft()
                heappush(queue, (-x[0], x[1]))
            else: 
                break
        if queue: 
            curProfit, curCapital = heappop(queue)
            curProfit = -curProfit
            w += curProfit

    return w



# k = 2
# w = 0
# profits = [1,2,3]
# capital = [0,1,1]

# k = 3
# w = 0
# profits = [1,2,3]
# capital = [0,1,2]

k = 10
w = 0
profits = [1,2,3]
capital = [0,1,2]

# k = 1
# w = 2
# profits = [1,2,3]
# capital = [1,1,2]


# k = 2
# w = 0
# profits = [1,2,3]
# capital = [0,9,10]
# 6
print(findMaximizedCapital(k, w, profits, capital))