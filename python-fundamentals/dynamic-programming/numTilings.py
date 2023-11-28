
# print(7 // 2 )



def numTilings(n):

    if n == 0: 
        return 1

    dp = {0: 1, 1:1, 2:2}
    if n <= 2: 
        return dp[n]

    for i in range(3, n + 1):
        dp[i] = 2*dp[i - 1] + dp[i - 3]

    return dp[n] % (10**9 + 7)

print(numTilings(5))


# this is a math trick ; supress the algebra with n - 1 tricks 

