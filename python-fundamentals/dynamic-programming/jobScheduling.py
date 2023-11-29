# start backwards and do dp. 
# at each ith time, dp[i] = max{job at time i + dp[next time], for all jobs at time i, and also dp[i+1]
# Concept is like knapsack: take either the job max job at time i + max of subsequent jobs after current ith job is done, or the i + 1th 
# one if it's larger. Start from end and iterate to the start.  

# Some tricks: 
# - When you end your job, you'll get an end time and need to do binary search to find the time of the next start times in dp. 

# Time: O(n log n) for sorting and bisecting
# Space: O(n) for storing times and dp


from collections import defaultdict
from bisect import bisect_left


def jobScheduling(startTime, endTime, profit):
    times = sorted(list(set(startTime + endTime)))
    dp = [0] * len(times)

    # create adjacency list of start times to index within startTime
    startTimeToIndex = defaultdict(list)
    for i in range(len(startTime)):
        startTimeToIndex[startTime[i]].append(i)

    #iterate backwards from last time
    for u in range(len(dp) - 1, -1, -1):
        curTime = times[u]
        nextDp = dp[u + 1] if u < len(dp) - 1 else  0
        if curTime not in startTimeToIndex: 
            dp[u] = max(0, nextDp)
        else: 
            paths = []
            for startIdx in startTimeToIndex[curTime]:
                idx = bisect_left(times, endTime[startIdx])
                path = profit[startIdx] + dp[idx]
                paths.append(path)
            dp[u] = max(paths + [0, nextDp])
    return dp[0]


# startTime = [1,2,3,3]
# endTime = [3,4,5,6]
# profit = [50,10,40,70]

startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]

print(jobScheduling(startTime, endTime, profit))