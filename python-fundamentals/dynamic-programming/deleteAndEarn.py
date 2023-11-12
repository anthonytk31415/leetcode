from collections import Counter
#Time: O(nlogn) for the sort
#Space: O(n) to store the profits

# We first do Counter to find occurrances of each number and then find the profit of taking the number 
# by doing occurrences * number.
# Then we build a distinctNums list by sorting the distinct keys of Counter
# Build the DP table "maxProfits" by cycling through the first one on in list to the end. 
# the max profit is built by first calculating total profit if you had taken the ith element. 
# It's equal to taking that ith element's profit plus the max profit of i's predecessor if that predecessor 
# num is not equal to i - 1. If it is, you take the most prior one (i-2)
# Then max profit is max of the last max profit and the current one you just calculated.

def deleteAndEarn(nums):
    profits = Counter(nums)
    distinctNums = list(profits.keys())
    # calculate possible profit by obtaining num
    for num in distinctNums: 
        profits[num] = num * profits[num]

    distinctNums.sort()

    # build the DP maxProfits = maxProfit possible by obtaining the ith distinct num
    maxProfits = [0 for _ in range(len(distinctNums))]
    for i, curNum in enumerate(distinctNums):
        maxProfits[i] = profits[num]
        if i != 0: 
            prevNum = distinctNums[i-1]
            if prevNum != curNum - 1: 
                maxProfits[i] += maxProfits[i-1]
            elif 0 <= i - 2:
                maxProfits[i] += maxProfits[i-2]
            # take the max of what you just calculated or the prior one
            maxProfits[i] = max(maxProfits[i-1], maxProfits[i])

    return maxProfits[-1]


nums = [2,2,3,3,3,4]
# nums = [2,2,3,3,3,4]
print(deleteAndEarn(nums))