
# Its like longest increasing subsequence in the O(n^2) form 
# but here since given a number k, there's only one number that will increase 
# the arithmetic sequence (num - difference), we can use a hash map to 
# look it up. So this is O(n) Time, O(n) Space for the hash map. 

import collections

def longestSubsequence1(arr, difference):
    maxLength, diffs = 0, {}
    for num in arr: 
        if num - difference in diffs: 
            diffs[num] = 1 + diffs[num - difference]
        else: 
            diffs[num] = diffs.get(num, 1)
        maxLength = max(maxLength, diffs[num])
    return maxLength

def longestSubsequence(arr, d):
    dp = collections.Counter()
    for a in arr:
        print(dp, a, dp[a - d])
        dp[a] = max(dp[a], dp[a - d] + 1)
    return max(dp.values())


arr = [1,3,5,7]
difference = 1

dp = collections.Counter()

print(dp["yo"])

# arr = [1,5,7,8,5,3,4,2,1]
# difference = -2

# print(longestSubsequence(arr, difference))