# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/


# DP problem. 
# O(n) Time for each price
# O(n) Space for each price


# Concept; each day, you can buy, sell, or do nothing. 
# define the buy as max profit you can achieve to have an item you can sell in the next round
# - here, you can either buy now or take buy[i-1] 
# define the sell as the max profit you can achieve so you are ready in next round to buy
# with these definitions you can set up your recursive formulas. 
# buy[i] = max of selling in i-2 (because of delay) and you buy today, or you bought i-1 and did nothing
# sell[i] = max of selling i-1 and did nothing, or you bought i-1 and sold today
# with this setup, you can buy low and hold until you get a great selling price, or if it maximizes profit, you 
# buy, sell, wait for some inopportune period, and then buy again. 
# The key is youre making an inductive step where you assume in the prior step, you have the max profit 

# Oh, and instantiate in the first period buy buying that item; 

# can optmize space and just keep the trailing i - 2 sells and i - 1 buys, but the array just makes interpretation cleaner

def maxProfit(prices):
    prices = [0] + prices
    buy = [0 for _ in range(len(prices))]
    sell = [0 for _ in range(len(prices))]
    
    buy[1] = -prices[1]
    for i in range(2, len(prices)):

        buy[i] = max(sell[i-2] - prices[i], buy[i-1])
        sell[i] = max(sell[i-1], buy[i-1] + prices[i])


    return sell[-1]


prices = [1,2,3,0,2]
# prices = [1,4,2]
print(maxProfit(prices))