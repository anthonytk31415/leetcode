from bisect import bisect_left
from collections import defaultdict

def longestIncreasingSubsequence(arr):
    parent = [None]*len(arr)
    bucket = []
    for i, num in enumerate(arr):

        if not bucket or num > arr[bucket[-1]]:
            if bucket: 
                parent[i] = bucket[-1]
            bucket.append(i)        
        else: 
            idx = bisect_left(bucket, num, key = lambda x: arr[x])
            bucket[idx] = i
            if idx > 0: 
                parent[i] = bucket[idx - 1]

    print("length of LCS: ", len(bucket))
    children = defaultdict(list)
    for i, p in enumerate(parent):
        children[p].append(i)

    res = [0]
    def dfs(i, pathLength):
        if i not in children and pathLength == len(bucket): 
            res[0] += 1
            return 
        for child in children[i]: dfs(child, pathLength + 1)

    dfs(None, 0)

    print(children)
    print("number of LCS: ", res[0])
    # return 


arr = [1,5,2,8,12,4,6]
print(longestIncreasingSubsequence(arr))