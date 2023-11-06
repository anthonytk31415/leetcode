# searchInsert

# if nums length == 0: return 0
# if nums length == 1: return p-1 or p + 1
# find the median; 



# log n time for n length of nums

def searchInsert(nums, target):
    def helper(nums, target, p, r):
        if p > r: 
            return p
        elif p == r:
            if target > nums[p]: 
                return p + 1
            else: 
                return p
        else: 
            q = (p + r) // 2
            if target <= nums[q]: 
                # print(p,q)
                return helper(nums, target, p, q)
            else:
                # print(q+1,r)
                return helper(nums, target, q+1, r)
    return helper(nums, target, 0, len(nums) - 1)

print(searchInsert([1,3,5,6], 2))