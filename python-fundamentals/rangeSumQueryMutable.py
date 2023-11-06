## this is too slow, need to do a special 

class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.runningSum = [i for i in self.nums]
        self.updated = False
        self.buildRunningSum()

    def buildRunningSum(self, index):
        for i in range(1, len(self.nums)): 
            self.runningSum[i] = self.runningSum[i-1] + self.runningSum[i]
        self.updated = True

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        self.updated = False

    def sumRange(self, left: int, right: int) -> int:
        if self.updated == False: 
            self.buildRunningSum()
        if left - 1 == -1: 
            x1 = 0
        else: 
            x1 = self.runningSum[left-1]
        x2 = self.runningSum[right]
        return x2 - x1

z = NumArray([1,3,5])
print(z.sumRange(0,2))
z.update(1,2)
print(z.nums)