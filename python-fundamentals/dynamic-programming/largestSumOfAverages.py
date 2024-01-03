# DP solution. You'll need to calculate for each k, and for each j the 
# maximum sum of averages at that k at that j'th index. 

# Use the prefixSum to easily sum of first j integers and then 
# when we calculate for the jth index, we find the max of dpPrev (i.e. k -1) at partitions of w 
# and thus use prefix to calculate the remainder. Think: we find at each j the max of 
# w from 1, to j the prefix and the dp Prev. 

# Time: O(k*n^2)
# Space: O(n)

def largestSumOfAverages(nums, k):
    prefix = [x for x in nums]
    for i in range(1, len(prefix)):
        prefix[i] = prefix[i] + prefix[i-1]

    dpPrev, dpCur = [0]*len(nums), [0]*len(nums)
    for i in range(1, k+1):
        for j in range(len(dpCur)):
            if i == 1: dpCur[j] = prefix[j]/(j+1)
            elif j == 0: dpCur[j] = dpPrev[j]
            else:
                candidates = []
                for w in range(1, j+1):
                    curCandidate = dpPrev[w-1] + (prefix[j] - prefix[w-1])/(j-(w)+1)
                    candidates.append(curCandidate)
                if candidates: dpCur[j] = max(candidates)
                dpCur[j] = max(dpCur[j], dpPrev[j])
        dpPrev, dpCur = dpCur, [0]*len(nums)
    return dpPrev[-1]




nums = [9,1,2,3,9] 
k = 3

nums = [1,2,3,4,5,6,7]
k = 4
print(largestSumOfAverages(nums, k))