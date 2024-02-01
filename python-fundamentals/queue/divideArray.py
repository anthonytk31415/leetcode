from collections import deque

def divideArray(nums, k):
    nums.sort()
    nums = deque(nums)
    
    res = []
    while len(nums) > 0: 
        curRes=  []
        minNum = nums.popleft()
        curRes.append(minNum)
        for _ in range(2):
            if nums[0] - minNum <= k: curRes.append(nums.popleft()) 
            else: return []
        res.append(curRes)
    return res


nums = [1,3,4,8,7,9,3,5,1]
k = 2

nums = [1,3,3,2,7,3]
k = 3

print(divideArray(nums, k))