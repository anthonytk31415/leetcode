
# here's an n log n way to solve it but maybe we can do linear without the sort
def longestSquareStreak1(nums):
    nums.sort()
    numSet = set(nums)
    visited = set()

    def dfs(num):
        visited.add(num)
        res = 1
        if num**2 in numSet: res += dfs(num**2)
        return res

    res = 0
    for num in nums: 
        if num not in visited: 
            curRes = dfs(num)
            res = max(res, curRes)
    if res > 1: return res
    return -1

# we dont have to sort since you'll have to traverse everything. We do store the path once we visit the node. 
# O(n) time, O(n) space

def longestSquareStreak(nums):
    numDict = {} # gives you the length of its square sequence
    for x in nums: 
        numDict[x] = 1
    visited = set()

    def dfs(num):
        visited.add(num)
        res = 1
        if num**2 in numDict:   
            if num**2 not in visited: dfs(num**2)
            res += numDict[num**2]
        numDict[num] = res
        return res

    res = 0
    for num in nums: 
        if num not in visited: 
            curRes = dfs(num)
            res = max(res, curRes)
    if res > 1: return res
    return -1

# nums = [4,3,6,16,8,2]
nums = [2,3,5,6,7]
print(longestSquareStreak(nums))