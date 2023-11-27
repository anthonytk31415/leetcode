# a brute force n^3 implementation
def findLength1(nums1, nums2):
    i = 0
    j = 0
    maxCount = 0
    curCount = 0
    for iStart in range(len(nums1)):
        for jStart in range(len(nums2)):
            i = iStart
            j = jStart
            while i < len(nums1) and j < len(nums2):
                if nums1[i] == nums2[j]:
                    i += 1
                    j += 1
                    curCount += 1
                else: 
                    maxCount = max(maxCount, curCount)
                    curCount = 0
                    break
            maxCount = max(maxCount, curCount)
            curCount = 0
    return maxCount

# here's a Time = O(n^2) implementation for DP with Space = O(N^2)
# Classic DP for Longest Common Subsequence problem 
def findLength2(nums1, nums2):
    dp = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
    maxLength = 0
    # i -1 ranges nums1; j - 1 ranges nums2
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if nums1[i-1] == nums2[j-1]: 
                dp[i][j] = 1 + dp[i-1][j-1]
                maxLength = max(maxLength, dp[i][j])

    return maxLength

# note we only need prev and current iteration, so we can use O(N) Space optimized
def findLength(nums1, nums2):
    cur = [0 for _ in range(len(nums2) + 1)]
    prev = [0 for _ in range(len(nums2) + 1)]
    maxLength = 0
    # i -1 ranges nums1; j - 1 ranges nums2
    for i in range(1, len(nums1) + 1):
        for j in range(1, len(cur)):
            if nums1[i-1] == nums2[j-1]: 
                cur[j] = 1 + prev[j-1]
                maxLength = max(maxLength, cur[j])
        prev = [x for x in cur]
        cur = [0 for _ in range(len(nums2) + 1)]
    return maxLength


# nums1 = [1,2,3,2,1]
# nums2 = [3,2,1,4,7]



# nums1 = [0,0,0,0,0,0,1,0,0,0]
# nums2 = [0,0,0,0,0,0,0,1,0,0]


nums1 = [0,1,1,1,1]
nums2 = [1,0,1,0,1]

print(findLength(nums1, nums2))