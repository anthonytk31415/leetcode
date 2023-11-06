def nextGreaterElements(nums):
    lookup = set(nums)
    res = []
    for x in nums:
        if x+1 in lookup: 
            res.append(x+1)
        else: 
            res.append(-1)

    return res



# nums = [1,2,1]
nums = [1,2,3,4,3]
print(nextGreaterElements(nums))



'''
The idea here is to store the indexes of the elements that we 
haven't seen a greater than value for them yet
we do this because if you stored the values you wouldn't be 
able to easily know where a value is at so you
can set it accordingly. This comes in handy in the second loop.

The values in the stack when we enter the second loop will always 
be decending, this is an important part of knowing that 
we are setting the indexes to their correct value. Since we always 
will set the index's left in the stack to the smallest
number when reiterating over the stack, ensuring a correct answer. 
'''




class Solution(object):
    def nextGreaterElements(self, nums):
        stack = []
        result = [-1] * len(nums)
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                result[stack.pop()] = nums[i]
            stack.append(i)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                result[stack.pop()] = nums[i]
                
        return result