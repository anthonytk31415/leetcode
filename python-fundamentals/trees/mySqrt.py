# mySqrt

# x non-negative int
def mySqrt(x):
    # newtons method
    n = 3
    x0 = x/2
    x1 = x0 - (x0**2 - x) / (2*x0)
    n -=1
    while n > 0:
        x0 = x1
        x1 = x0 - (x0**2 - x) / (2*x0)
        n -=1
    return x1//1


# solution to x_0 **(1/2) = y is y such that y^2 = x_0 --> f(x) = x^2 - x_0
# e.g. x_0 = 9, y = 3, so 3 ^2 = 
# --> f'(x) = 2x


# guess = 

# x_0 = 4
# x_1 = 4 - (4**2 - 8)/(2*4)



print(mySqrt(4,3))
