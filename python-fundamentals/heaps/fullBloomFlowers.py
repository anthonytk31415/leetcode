from heapq import heappush, heappop
from collections import deque

# this is an O(nlogn) solution using priority queues. apparently there's a
# binary search one. 


def fullBloomFlowers(flowers, people):
    flowers.sort(key = lambda x: x[0])
    flowers = deque(flowers)

    p_queue = []
    for idx, day in enumerate(people):
        p_queue.append((day, idx))
    p_queue.sort(key=lambda x: x[0])

    numFlowers = [None for _ in range(len(people))]
    queue = []
    p = 0
    while p < len(p_queue):
        pDay, pIdx = p_queue[p]
        # print(pDay, pIdx, queue)

        while flowers:                 # add flowers into the queue until you can't
            # print(flowers, pIdx)
            f_start, f_end = flowers[0] 
            if f_start <= pDay: 
                f_start, f_end = flowers.popleft()
                heappush(queue, [f_end, f_start])
            else: 
                break


        while queue:                # deque flowers if entry_end < current person 
            q_end, q_start = queue[0]
            # print('qend qstart:', queue[0], 'pday: ', pDay)
            if q_end < pDay: 
                heappop(queue)
            else: 
                break
        # print(queue, pIdx)

        # print(queue, pIdx)
        numFlowers[p] = (len(queue), pIdx)
        p += 1
    
    # print(numFlowers)
    res = [None for _ in range(len(people))]
    for i in range(len(people)):
        numFlower, idx = numFlowers[i]
        res[idx] = numFlower

    return res


# flowers = [[1,6],[3,7],[9,12],[4,13]]
# people = [2,3,7,11]


# flowers = [[11,11],[24,46],[3,25],[44,46]]
# people = [1,8,26,7,43,26,1]


flowers = [[1,10],[3,3]]
people = [3,3,2]


# d = deque(people)
# print(d[0])
# print(d)
print(fullBloomFlowers(flowers, people))