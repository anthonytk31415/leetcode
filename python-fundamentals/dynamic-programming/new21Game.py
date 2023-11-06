# so this works, but it is too slow. 
# how can I improve? 

def new21Game(n, k, maxPts):
    memo = {}
    prob_i = 1/maxPts

    def helper(curPts):
        if curPts in memo: return memo[curPts]
        res = 0
        # terminal condition: curPts over threshold
        if curPts >= k:
            if curPts <= n: 
                res = 1
            else: 
                res = 0
        # keep drawing            
        else: 
            # print(range(1, maxPts + 1))
            for i in range(1, maxPts + 1):
                res += helper(curPts + i) * prob_i
        memo[curPts] = res
        return res
    
    helper(0)
    return memo[0]



# the game: 
# - Start at pts = 0. Keep drawing until you have pts >= k.
# - Each draw is an integer uniformly from [1, w], where w = max points.

# - Possible values are from 0 to (k-1) + w. 

# goal: prob(pts <= n) = ?

# Some key note: 
# - prob(pts) = [prob(pts - w + 0) + prob(pts - w + 1) + ... + prob(pts -w + (w-1))] * 1/w (*)
# -- interpretation: to get to current points, you have to draw from (pts - x + x) 
#    for each x from 1 to w as long as 1 <= x <= maxPts
# -- we divide by 1/2 because each 'draw' has 1/w chance
#    (for ex. if we are at pts=3, to get to pts = 3+1 = 4, that's a 1/w draw)
# -- note the terms in in the brackets "[]" make a sliding window of length w at most. 

# Approach: 
# - Let's create a DP array from 0 to n inclusive where dp[0] = 1 and we'll instantiate the
#   rest of dp[i] = 0. 
#   *** this is the key insight *** 
#   dp[i] will represent the prob(pts = i). So dp[0] = prob[0] = 1. And we'll build 
#   dp[i] from its predecessors of length w away from i: 
#   dp[i] = 1/w(dp[i - w] + ... + dp[i - 1]) = 1/w(sum of dp[i - w + j]) for 
#   j = 0 , 1, ... w -1

# - in the approach below, Wsum will be the running prob: sum of dp[i]

def new21Game(N, K, W):
    if K == 0 or N >= K + W: return 1
    dp = [1.0] + [0.0] * N

    Wsum = 1.0
    for i in range(1, N + 1):
        dp[i] = Wsum / W
        # add in the new term if i is within the sliding window
        if i < K: Wsum += dp[i]         

        # take away the "oldest" term if i is outside the sliding window
        if i - W >= 0: Wsum -= dp[i - W]

    return sum(dp[K:])


# n =
# 9811
# k =
# 8776
# maxPts =
# 1096

print(new21Game2(3,3,2))


# print(new21Game(9811, 8776, 1096))
# print(new21Game(3,3,2))
# print(new21Game(10,1,10))
# print(new21Game(6,1,10))

# print(new21Game(21,17,10))
# print([x for x in range(1,3)])
# myDict = {}
# print(0 in myDict)