# O(n^2) time :(
def maxProfit(prices):
    curMax = 0
    for i in range(len(prices)):
        z = max(prices[i:]) - prices[i]
        curMax = max(curMax, z)
    return curMax

#O(n) time

def maxProfit(prices):
    curMax = 0
    smallest = prices[0]
    for n in prices:
        if n < smallest: 
            smallest = n
        else:
            curMax = max(curMax, n - smallest)
    return curMax




z = [100, 50, 200, 10, 301, 302, 150]
print(maxProfit(z))