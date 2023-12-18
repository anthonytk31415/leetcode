
from bisect import bisect

# Sort with two pointers
# One solution: sort items and initiate a query to then sort the queries essentially in a queue. 
# go through the sorted queries (queue). For each idx in queue, take the prior's largest beauty. 
# Keep a pointer on your items: if your price of item j <= queue price: consider max beauty on that jth item. 

# Complexities for all solutions here: 
# Time: O(n log n) for either sorts or binary searches. 
# Space: O(n) for storage

def maximumBeauty1(items, queries):
    items.sort(key = lambda x: x[0])
    queue = [(queries[i], i) for i in range(len(queries))]
    queue.sort(key = lambda x: x[0])
    maxBeauty = [0]*len(queries)            # for the ith query, we maintain the maxBeauty[i] and return this later

    j = 0       # j over items
    for queueIdx, queueItem in enumerate(queue): 
        curQueueMaxPrice, curQueryIdx = queueItem

        if queueIdx > 0: 
            _, prevQueryIdx = queue[queueIdx - 1]
            maxBeauty[curQueryIdx] = max(maxBeauty[curQueryIdx], maxBeauty[prevQueryIdx])

        while j < len(items) and items[j][0] <= curQueueMaxPrice: 
            beauty_j = items[j][1]
            maxBeauty[curQueryIdx] = max(maxBeauty[curQueryIdx], beauty_j) 
            j += 1

    return maxBeauty

# here's a bisect version: 
# Sort the items. Then for each item, keep track of prior's max beauty. 
# then for each query, binary search the query to find the max beauty from the items. 

def maximumBeauty(items, queries):
    items.sort(key = lambda x: x[0])
    for i in range(1, len(items)):
        items[i][1] = max(items[i][1], items[i-1][1])

    maxBeauty = []
    for query in queries: 
        idx = bisect(items, query, key = lambda x: x[0])
        if idx - 1 < 0: 
            curRes = 0
        else: curRes = items[idx - 1][1]
        maxBeauty.append(curRes)
    
    return maxBeauty


# print(maxBeauty(items, quer))

# items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
# # print(sorted(items, key = lambda x: x[0]))
# # sorted = [[1, 2], [2, 4], [3, 2], [3, 5], [5, 6]]
# queries = [1,2,3,4,5,6]
                

# items = [[1,2],[1,2],[1,3],[1,4]]
# queries = [1]

items = [[10,1000]]
queries = [5]

# items = [[193,732],[781,962],[864,954],[749,627],[136,746],[478,548],
#          [640,908],[210,799],[567,715],[914,388],[487,853],[533,554],
#          [247,919],[958,150],[193,523],[176,656],[395,469],[763,821],
#          [542,946],[701,676]]


# queries = [885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584]

print(maximumBeauty(items, queries))