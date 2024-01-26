from functools import reduce
from math import gcd 

# nums = [12, 18, 24, 30]
# res = reduce(lambda x, y: x + y, nums)
# print(res)

nums = [1,4,3,1]
nums = [5,5,5,5,10]
res = reduce(lambda x, y: gcd(x, y), nums)
print(res)