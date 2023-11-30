from math import ceil
# https://leetcode.com/problems/guess-number-higher-or-lower-ii/submissions/

# The concept is not terrible with Memoization DP but its quite tricky with how to handle the starting and ending points
# of the intervals as well as the trick that (1) each (start, end) pair will have potentially a different result and (2) 
# picking up and finding the recursive formula. 


# TBD: somewhere in here there's the ability to use a monotonic stack. 

# Time: O(n^3) since you need to potentially go through N^2 options N times 
# Space: O(n^2)


from functools import lru_cache

def getMoneyAmount(n):

    @lru_cache(None)
    def helper(start, end):
        res = 0
        if end - start == 0: 
            res = 0
        elif end - start == 1: 
            res = start   
        else: 
            choices = []
            for leftEnd in range(start, end - 1):
                head = leftEnd + 1
                rightStart = head + 1
                curChoice = head + max(helper(start, leftEnd), helper(rightStart, end)) 
                choices.append(curChoice)
            res = min(choices)
        return res
    return helper(1, n)


# n = 10
# n = 5
n = 10


# print(5//2)
print(getMoneyAmount(n))
