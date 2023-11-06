def permute(nums):
    res = []
    
    nums = set(nums)

    def helper(nums, cur_path, res):
        if not nums: 
            res+= cur_path
            return
         
        for x in nums: 
            new_cur_path = [c + [x] for c in cur_path]
            new_nums = set(x for x in nums)
            new_nums.remove(x)
            helper(new_nums, new_cur_path, res)    

    helper(nums, [[]], res)
    return res

nums = [1,2,3]

print(permute(nums))