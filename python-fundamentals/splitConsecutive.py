# [1,2,3,4,4,5]

# # iterate across the i's in nums
# # if you encounter a[i] = a[i+1]:
# abcd --> len = 4 i = 0; 4 - 0 - 1
# len=4, i = 2; 4-2 = 2 


1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 7, 
      x  x           x     x 

1, 2, 2, 3, 3, 4 
      x  x     

1 2 2 3 
    x


1 2 2 2 2 2 2 2 2 2 2 2 3 4 

- if you had a bunch

def isPossible(nums):

    def helper(nums, i, cur_consec, leftover):
        # cur_consec 
        if len(nums) - i + cur_consec < 3:                  # current chain doesn't have enough nums and current consecutive
            
            for x in nums: 
                leftover.append(x)
            return helper(leftover, 0, 0, leftover) 
        elif not nums and cur_consec >= 3:                  # no more nums, consecutives >= 3: success
            return helper()        
        elif len(nums) - i > 1 and nums[i] == nums[i+1]:    # you have room to add chains
            if cur_consec >= 3:                             # need to break the chain
                return helper(nums, i + 1, 1)
            if cur_consec < 3: 
                return False
        elif len(nums) - i > 1 and nums[i+1] > nums[i]:                           # add to the chain
            return helper(nums, i + 1, cur_consec + 1)

        
    return helper(nums, 0, 1, [])

# nums = [1,2,3,4,4,5] # false
nums = [1,2,3,3,4,4,5,5]
print(isPossible(nums))