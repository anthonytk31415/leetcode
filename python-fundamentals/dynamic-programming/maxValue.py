from math import inf

# 3D DP.
def maxValue1(events, k):
    events.sort(key = lambda x: (x[1], x[0]))
    minTime, maxTime = events[0][0], events[-1][1]

    dp = [[[0 for _ in range(0, maxTime + 1, 1)] for _ in range(len(events) + 1)] for _ in range(k+1)]
    for e in range(1, len(dp)):
        for i in range(1, len(dp[0])):
            start_i, end_i, val_i = events[i-1]
            # print(start_i, end_i, val_i)
            for j in range(1, len(dp[0][0])):
                x = 0
                if j == end_i: 
                    x = val_i + dp[e - 1][i - 1][start_i - 1]
                dp[e][i][j] = max(x, dp[e][i-1][j], dp[e][i][j-1])
    
    # print(dp)
    return dp[-1][-1][-1]

# space optimized with prev and cur
# 
def maxValue(events, k):
    # edge case: k = 1
    if k == 1: 
        return max([x[2] for x in events])

    events.sort(key = lambda x: (x[1], x[0]))
    # print(events)
    isOverlap = False
    for i in range(1, len(events)):
        if events[i][0] <= events[i-1][1]:
            isOverlap = True
            break
    # print(isOverlap)
    if not isOverlap: 
        events.sort(key = lambda x: -x[2])
        return sum([x[2] for x in events[:k]])
    # print('eval')
    # edge case: merge if you have 2 intervals with same start, different end, same val: take smaller end. 
    updatedEvents = [events[0]]
    for event in events[1:]:
        if updatedEvents[-1][0] == event[0] and updatedEvents[-1][2] == event[2]:
            updatedEvents[-1][1] = min(updatedEvents[-1][1], event[1])
        else: 
            updatedEvents.append(event)
    events = updatedEvents

    times = list(set([x[0] for x in events] + [x[1] for x in events])) + [0]
    times.sort()
    timeToIndex = {}
    for i, time in enumerate(times): 
        timeToIndex[time] = i

    prev = [[0 for _ in range(len(times))] for _ in range(len(events) + 1)]
    cur = [[0 for _ in range(len(times))] for _ in range(len(events) + 1)]
    for e in range(k):
        for i in range(1, len(cur)):
            start_i, end_i, val_i = events[i-1]
            for j in range(1, len(cur[0])):
                x = 0
                if times[j] == end_i: 
                    x = val_i + prev[i - 1][timeToIndex[start_i] - 1]
                cur[i][j] = max(x, cur[i-1][j], cur[i][j-1])
        # print(prev, cur)
        prev, cur = cur, [[0 for _ in range(len(times))] for _ in range(len(events) + 1)]
    
    return prev[-1][-1]

import bisect 

# and then, here comes the king of elegence: Lee

# you really should look at the structure of some of Lee's Knapsack. So smooth

# So the concept is: dp represents the prior k's (i.e. k-1) iteration of max value at end time. 
# We sort events by end time and iterate through the events: s, e, v
# For each event, we find the max prior value at end time by bisect - 1 
# (the -1 because when a meeting ends, we cant immediately start another one).
# We only append a new end time to our current dp = dp2 if the value increases. That way, 
# the end of the dp array always contains the max value at end time. 

def maxValue(A, K):
    A.sort(key=lambda sev: sev[1])
    dp, dp2 = [[0, 0]], [[0, 0]]
    for k in range(K):
        for s, e, v in A:
            i = bisect.bisect(dp, [s]) - 1
            if dp[i][1] + v > dp2[-1][1]:
                dp2.append([e, dp[i][1] + v])
        dp, dp2 = dp2, [[0, 0]]
    return dp[-1][-1]


events = [[1,3,4],[2,4,1],[1,1,4],[3,5,1],[2,5,5]]
k = 3
# events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
# k = 3

# events = [[1,2,4],[3,4,3],[2,3,1], [1,4,6]]
# events = [[1,2,4],[3,4,3],[2,3,10]]
# k = 2
print(maxValue(events, k))