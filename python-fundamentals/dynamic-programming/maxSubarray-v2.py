# max subarray

## chain breaks when your step hits zero
## broken will always keeep the largest chain or broken as time goes on

# x =      [1, -5,  2,  7, -3,  -7, 10]
# chain =  [1, -4,  2,  9,  6,  -1, 10]
# broken = [1,  1,  2,  9,  9,   9, 10]

# chains = max(prev_chain, 0) + current 
# broken = max(prev_broken, chains)

from math import inf

def maxSub(arr):

    chain = broken = -inf

    for x in arr:
        chain = max(chain, 0) + x
        broken = max(broken, chain)
    return broken


x = [1, -5,  2,  7, -3,  2, 5, -12]

print(maxSub(x))