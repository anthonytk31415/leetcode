def change(amount, coins):
    coins = [0] + coins
    dp = [[0]*(amount + 1) for coin in range(len(coins))]
    print(dp)
    for c in range(1, len(coins)):
        for amt in range(len(dp[0])):
            if amt == 0 and c == 1:
                dp[c][amt] = 1
            elif 0 <= amt - coins[c] < len(dp[0]):
                dp[c][amt] = dp[c][amt - coins[c]] + dp[c-1][amt]
            else: 
                dp[c][amt] = dp[c-1][amt]
        
    return dp[-1][-1]
    
amount = 5
coins = [1,2,5]
print(change(amount, coins))