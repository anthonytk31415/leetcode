class Solution:

    def __init__(self, nums):
        self.nums = nums
        self.shuffled = [x for x in nums]

    def reset(self):
        return self.nums

    def shuffle(self):
        self.shuffled.sort(key = lambda x: random())
        return self.shuffled

from random import random, randint
print(random())
print(randint(3, 9))

# >> 0.8683555860107931
# >> 6


arr = [1,2,3,4,5,6,7,8]

s = Solution(arr)
s.shuffle()
print(s.shuffled)
s.shuffle()
print(s.shuffled)
s.shuffle()
print(s.shuffled)