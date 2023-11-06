# https://leetcode.com/problems/minimum-cost-to-make-array-equal/?envType=daily-question&envId=2023-10-27

# Time: O(nlogn)
# Space: O(n)

# kind of solved this as a sliding window. 
# you need to compare your 
# If you initially sort your nums (and keep track your cost), 
# every time yo

def minCost(nums, cost):
    data = list(zip(nums, cost))
    data.sort(key= lambda x: x[0])
    
    nums = [x[0] for x in data]
    cost = [x[1] for x in data]

    delta = [None for _ in range(len(data))]
    for i in range(1, len(data)):
        delta[i] = nums[i] - nums[i-1]

    # calculate cost for reducing all nums to nums[0]
    curCost = 0
    for i in range(1, len(data)):
        curCost += (nums[i] - nums[0]) * cost[i]

    ## 
    minCost = curCost

    adds = 0
    subs = sum(cost)
    for i in range(1, len(data)):
        adds += cost[i-1]
        subs -= cost[i-1]
        curCost = curCost + delta[i]*adds - delta[i]*subs
        minCost = min(minCost, curCost)

    return minCost

# nums = [1,3,5,2]
# cost = [2,3,1,14]

nums = [2,2,2,2,2]
cost = [4,2,8,1,3]


print(minCost(nums, cost))