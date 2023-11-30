
from math import ceil
def getMoneyAmount(n):
    memo = {} ## key = (n, start); value = cost

    def helper(n, start):
        if (n, start) in memo: 
            return memo[(n, start)]
        res = 0
        if n == 1: 
            res = 0
        elif n == 2: 
            res = start   
        else: 
            choices = []
            for left in range(1, n - 1):
                head = left + 1
                right = n - 1 - left
                curChoice = head + helper(left, 1) + helper(right, head + 1) 
                print("n {}, start {}, left {}, right {}, head {}, curchoice {}".format(n, start, left, right, head, curChoice))
                choices.append(curChoice)
            res = min(choices)
        memo[(n, start)] = res
        return res

    ans = helper(n, 1)
    print(memo)
    return ans


# n = 10
# n = 5
n = 6


# print(5//2)
print(getMoneyAmount(n))
