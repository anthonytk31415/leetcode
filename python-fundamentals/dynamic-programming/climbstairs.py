# climbing stairs

def climbStairs(n):
    container = {1:1, 2:2}
    for i in range(1,n+1):
        if i not in container:
            container[i] = container[i-1] + container[i-2]
    return container[n]

# def climbStairs(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else: 

#         return climbStairs(n-1) + climbStairs(n-2)


print(climbStairs(3))
print(climbStairs(5))
print(climbStairs(10))
print(climbStairs(38))


#simplier but slower than mine
def climbStairs(self, n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

## the fastest solution
def climbStairs(self, n):
    if n <= 2: 
        return n
    
    a, b, c = 0, 1, 2
    
    while (n > 2):
        a, b = b, c
        c = a + b
        n = n - 1
    
    return c

# def sample(x):
#     y = 1
#     def helper (x,y):
#         y = y + 2
#         return y
#     y = helper(x,y)
#     return y

# print(sample(3))