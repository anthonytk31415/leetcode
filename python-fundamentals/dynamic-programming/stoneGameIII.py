import numpy as np
from math import inf 

def stoneGameIII(stoneValue):
    stoneValue = stoneValue[::-1]
    memo = [None]*len(stoneValue)

    # i represents current index and returns an np.array[scoreA, scoreB]  
    def f(i): 
        if i == 0:
            maxPoints = np.array([stoneValue[0],0])
        else: 
            maxPoints = np.array([-inf,-inf])
            for j in range(1, 4):
                print(i, j)
                if i - j + 1< 0: break  
                x = memo[i-j][::-1] if i - j >= 0 else 0
                ySum = sum(stoneValue[i-j+1:i+1])
                y = np.array([ySum, 0])

                print("x: ", x, "y:", y, "ySum", ySum)
                curRes = x + y
                if curRes[0] > maxPoints[0]:
                    maxPoints = curRes 
        
        memo[i] = maxPoints
        return memo[i]

    for i in range(len(stoneValue)):
        f(i)

    print(memo)
    print(memo[-1])
    if memo[-1][0] > memo[-1][1]: return "Alice"
    if memo[-1][0] == memo[-1][1]: return "Tie"
    else: return "Bob"

# a = (1,2)
# print(a[::-1])
# stoneValue = [3,-9]
# stoneValue = [1,2,3,-9]
stoneValue = [1,2,3,7]
# stoneValue = [1,2,3,6]
print(stoneGameIII(stoneValue))






# a = np.array([1,2])
# b = np.array([3,2])
# c = a + b 
# print(c)
# print(a[0])
# print(a[::-1])