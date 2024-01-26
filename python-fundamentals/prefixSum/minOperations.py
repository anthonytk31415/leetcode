# https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/


from bisect import bisect_left

# Keep a prefix sum so you can calculate the sum of integers up to an index in constant time.
# Say q = query[i]. We want to match all elements to q at that ith iteration. 
# We keep an index marker where we have elements < q to the left of idx and elements >= q to the right 
# inclusive of idx. So on the left, we take abs(width * q - sum of integers) to find operations. 
# Similarly, on the right we take abs(width * q - sum of integers). 
# We must separate them so the arithmetic works.

# Time: O(nlogn) for the sort, Space = O(n) for the prefix sum

def minOperations(nums, queries):
    nums.sort()
    n = len(nums)
    res = [0] * len(queries)
    prefix = [x for x in nums]
    for i in range(1, len(prefix)):
        prefix[i] = prefix[i] + prefix[i-1]

    for i, q in enumerate(queries): 
        idx = bisect_left(nums, q)
        if idx == 0:         
            alpha = abs((prefix[n-1]) - (n-1-idx+1)*q)
            beta = 0
        if idx > 0: 
            alpha = abs((prefix[n-1] - prefix[idx - 1]) - (n-1-idx+1)*q)
            beta = abs(prefix[idx-1] - idx * q)
        res[i] = alpha + beta

    return res

nums = [3,1,6,8]
queries = [1,5]

nums = [2,9,6,3]
queries = [10]

print(minOperations(nums, queries))