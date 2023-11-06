from collections import defaultdict
from random import randint 

class Solution:

    def __init__(self, nums):
        self.num_dict = defaultdict(list)
        for i in range(len(nums)):
            self.num_dict[nums[i]].append(i)
            
        print(self.num_dict)


    def pick(self, target):
        return self.num_dict[target][randint(0, len(self.num_dict[target])-1)]

nums = [1, 2, 3, 3, 3]

sol = Solution(nums)
print(sol.pick(3)
, sol.pick(3)
, sol.pick(3))