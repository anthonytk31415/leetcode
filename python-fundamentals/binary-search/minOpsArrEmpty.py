from collections import Counter; 

# find the largest integer n such that (x - 3*n) is even
# if x is even, then n is even
# if x odd, then n odd

def minOperations(nums):

    def findLargestThree(x):
        if x == 1: return -1
        if x % 3 == 0: return x//3
        left = 1 if (x % 2 == 1) else 0
        right = x if (x %2 == 1) else x - 1
        while left <= right: 
            mid = (left + right)//2
            check = x - 3*mid
            if check == 0: return mid
            elif check > 0: left = mid + 2
            else: right = mid - 2
        return right

    counter = Counter(nums)
    res = 0
    for num in counter.keys(): 
        val = counter[num]
        multThree = findLargestThree(val)
        if multThree == -1: return -1
        res += multThree
        res += (val - 3*multThree) // 2
    return res


# nums = [19,19,19,19,19,19,19,19,19,19,19,19,19]
nums = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]
print(minOperations(nums))