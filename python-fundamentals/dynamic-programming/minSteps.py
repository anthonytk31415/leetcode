# https://leetcode.com/problems/2-keys-keyboard/

def minSteps(n): 
    memo = {1: 0, 2: 2}

    def helper(k):
        if k in memo: 
            return memo[k]
        
        res = k # max capped at k for copying 1 time and then pasting (k-1) times

        for i in range(3, int(k // 2 + 1)):
            if k % i == 0: 
                cur = int((k / i) + helper(i))
                res = min(res, cur)

            print(i, res)
        memo[k] = res
        return res
    
    return helper(n)



print(minSteps(24))