from math import inf

# DP. at step -1, you "bought a minus inf stock" and you sold 0. Do this so the setup is smooth. 
# You instantiate a dp: Buy and Sell, where buy is max profit after either (buy = you always have a stock that is bought)
# i or you wait after buying at i-1
# And Sell is max profit buy selling stock = buy[i] + price[i], or you sold yesterday and you did nothing. 

# Time: O(n)
# Space: You only are concerned ith i-1 actions, so you can create an O(1) Space

def maxProfit(prices):
    prevBuy, curBuy = -inf, 0
    prevSell, curSell = 0, 0
    for price in prices: 
        curBuy = max(prevBuy, prevSell - price)
        curSell = max(prevSell, curBuy + price)
        
        prevBuy, curBuy = curBuy, 0
        prevSell, curSell = curSell, 0

    return prevSell

prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
print(maxProfit(prices))