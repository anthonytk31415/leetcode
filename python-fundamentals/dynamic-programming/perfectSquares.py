# Perfect Squares
# https://leetcode.com/problems/perfect-squares/

## TLE???

from collections import deque
from math import inf, sqrt
def numSquares(n):
    squares = [i**2 for i in range(int(sqrt(n))+1) if i**2 <= n]
    dp = [[inf]*(n+1) for _ in range(len(squares))]
    print(squares)
    for row in range(1, len(dp)):
        for col in range(len(dp[0])):
            if row == 1 and col == 0: 
                dp[row][col] = 0
            elif 0 <= col-squares[row] < (n+1): 
                dp[row][col] = min(dp[row-1][col], 1+ dp[row][col-squares[row]])
            else: 
                dp[row][col] = dp[row-1][col]
    return dp[-1][-1]

print(numSquares(13))

## a bfs version

def numSquares2(n):
    squares = [i**2 for i in range(int(sqrt(n)), 0, -1) if i**2 <= n]
    q = deque()
    q.append((n, 0, inf))
    while q: 
        cur_n, cur_nums, last_prime = q.popleft() 
        if cur_n == 0: return cur_nums
        for sq in squares: 
            if sq <= last_prime and cur_n - sq >= 0: 
                q.append((cur_n - sq, cur_nums + 1, sq))

print(numSquares2(13))