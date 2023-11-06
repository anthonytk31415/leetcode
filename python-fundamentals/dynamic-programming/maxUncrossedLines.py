from collections import defaultdict
from functools import lru_cache
def maxUncrossedLines(nums1, nums2):
    i = 0
    j = 0

    @lru_cache(None)
    def helper(i, j): 
        print('i:', i, 'j:', j)
        if i >= len(nums1) or j >= len(nums2):
            return 0
        res = []
        for idx_i in range(i, len(nums1)):
            for idx_j in range(j, len(nums2)):
                cur_res = 0
                if nums1[idx_i] == nums2[idx_j]:
                    cur_res = 1 + helper(idx_i+1, idx_j + 1)
                    res.append(cur_res)

        if not res: 
            return 0
        return max(res) 

    return helper(i, j)

# nums1 = [1,3,7,1,7,5]
# nums2 = [1,9,2,5,1]

# nums1 = [2,5,1,2,5]
# nums2 = [10,5,2,1,5,2]

nums1 = [1,4,2]
nums2 = [1,2,4]

print(maxUncrossedLines(nums1, nums2))