
# https://leetcode.com/problems/number-of-longest-increasing-subsequence
# This is a variant of the classic Patience Game induced Longest Increasing Subsequence. 

# To find the number of paths, we iterate through our nums and play the "Patience Game": 
# Keep track of an array res = [[indexes], ...]. Instantiate with [[0]] representing the 0th index going into the 0th idx of the array.
# Now iterate through nums:   
# When we find a largest number in the sequence of nums (i.e. nums > res[-1][-1]), we append an array with the index of the number: res = [[idx_i, idx_k, ... ], ..., [new idx]] 
#   The most recent number is at the end of the subarray. 
# When we find a smaller number, we binary search the number (key = lambda x: nums[x[-1]]) and append it to that list in that index. 
# Once we find our Patience Sorted Array (res), we start from the front and iterate through the res to build a parent arary. The Parent array represents 
# when you get the index i, you'll have Parent[i] paths to take. Take note of valid parents: for an index j in the ith index of the res, its parent will be in the i-1th position
# and for that parent to be a valid one, that parent's num < child num. We'll build this recursively. 
# Return the sum of all parent[i]'s in res[-1]. 

# Time: O(nlogn)
# Space: O(n)

from bisect import bisect_left, bisect
def findNumberOfLIS(nums):
    res = [[0]]
    for i in range(1, len(nums)): 
        num = nums[i]
        if num > nums[res[-1][-1]]:
            res.append([i])
            numLIS = 1
        else: 
            idx = bisect_left(res, num, key = lambda x: nums[x[-1]])
            res[idx].append(i)

    parent = [1 for _ in range(len(nums))]
    for i in range(len(res)):
        for j in range(len(res[i])):
            if i == 0: 
                parent[res[i][j]] = 1
            else: 
                idx = bisect(res[i-1], -nums[res[i][j]], key = lambda x: -nums[x])
                parent[res[i][j]] = sum([parent[x] for x in res[i-1][idx:] if x < res[i][j]])

    return sum([parent[x] for x in res[-1]])


## you can modify this so when you build the parent, you can take the length of of the res[i-1] from the binary searched element onward. 


# nums = [1,2,7,3,6,5]
# nums = [1,0,2,6,3,5,4]
nums = [1,2,4,3,5,4,7,2]
# nums.sort()
# print(nums)
# idx = bisect_left(nums, 2)
# print(idx)
# idx = bisect_left(nums, 6)
# print(idx)

print(findNumberOfLIS(nums))


# follow-up: No.549. Binary Tree Longest Consecutive Sequence II