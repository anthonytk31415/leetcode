# take the median: q = median


def singleNonDuplicate(nums):
    def helper(nums, p, r):
        if p >= r: 
            return p
        q = (r + p)//2
        if nums[q-1] == nums[q]:
            if (r - p) == 2: 
                return q+1 
            elif (r - (q+1)) %2 == 1: 
                return helper(nums, p, q-2)
            else: 
                return helper(nums, q+1, r)
        elif nums[q+1] == nums[q]:
            if (r - p) == 2: 
                return q-1 
            if ((q-2) - (p)) %2 == 1: 
                return helper(nums, p, q-1)
            else: 
                return helper(nums, q+2, r)
        else:
            return q
    return nums[helper(nums, 0, len(nums)-1)]

nums = [1,1,2,3,3,4,4,8,8]
# nums = [3,3,7,7,10,11,11]
print(singleNonDuplicate(nums))