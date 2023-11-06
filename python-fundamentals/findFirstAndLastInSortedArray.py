def searchRange(nums, target):
    if not nums: 
        return [-1, -1]
    # this will return 
    def helper(nums, target, p, r):
        if p == r: 
            return p
        
        else: 
            q = (p + r) // 2
            if target > nums[q]:
                return helper(nums, target, q+1, r)
            else: 
                return helper(nums, target, p, q)
                
    start = helper(nums, target, 0, len(nums)-1)

    if nums[start] != target: 
        return [-1, -1]
    else: 
        end = start
        while True:
            if end + 1 >= len(nums) or nums[end+1] != target: 
                break 
            else: 
                end +=1
        while True: 
            if start - 1 <0 or nums[start-1] != target: 
                break
            else: 
                start -=1
        return [start, end]
            





        # if 0 <= res0 - 1 and nums[res0-1] == target:
        #     return [res0-1, res0]
        # elif res0+1 <= len(nums) - 1 and nums[res0+1] == target:
        #     return [res0, res0 + 1]
        # else: 
        #     return [res0, res0]

nums = [5,7,7,8,8,10]
target = 8

# nums = []
# target = 0
print(searchRange(nums, target))