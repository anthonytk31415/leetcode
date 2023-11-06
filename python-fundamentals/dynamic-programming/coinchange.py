from functools import lru_cache
from math import inf


# the answer is dependent on answers to smaller problems
# let dp(i) = min coins for amt 
# then dp(i) = dp(i - coin) + 1 for each coin and take the min across each coin
# trick: use @lru_cache to cache the recursive results

# Time: O(amt*nCoins) since we have amounts * n choices at each amount
# Space: O(amt*Coins) since we need the memory for each state

def coinChange(coins, amt):
    @lru_cache(None)
    def dp(i):
        if i == 0: 
            return 0
        if i < 0:
            return inf
        return min((dp(i - coin) + 1) for coin in coins)
    
    return dp(amt) if dp(amt) != inf else -1


coins = [1,2,5]
print(coinChange(coins, 11))