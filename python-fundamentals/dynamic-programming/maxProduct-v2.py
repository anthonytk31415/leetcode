#Trick: you want to keep a running tracker of your "chains" and a the max at each step
# because each new num n the nums array can "flip" the chain of max/min, your answer could 
# be a subarray prior to getting to the end
#
# at each step, a change in signs can "break the chain" depending on the sign of x itself
  
# at each step, your  min/max could be the previous chain * x or x itself; 
# and at each step you evaluate the max
# signs can change max to min so you want to keep track of the highest progressing chain


def maxProduct(nums):
    if len(nums) == 1:
        return nums[0]
    minC = maxC = curMax = nums[0] 
    for x in nums[1:]:
        minC, maxC = min(x, minC*x, maxC*x), max(x, minC*x, maxC*x)
        curMax = max(curMax, minC, maxC)
    return curMax

# print(maxProduct([1,2,-4,3]))
print(maxProduct([2,3,-2,4]))


from math import inf
def maxProduct2(nums):
    mini, maxi, res = 1, 1, -inf
    for n in nums:
        a = mini * n
        b = maxi * n
        mini = min(a, b, n)
        maxi = max(a, b, n)
        res = max(res, maxi)
    return res