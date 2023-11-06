def kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k):
    curSum = 0
    if k >= numOnes: 
        k = k - numOnes
        curSum += numOnes
    else: 
        return k
    if k >= numZeros:
        k = k - numZeros
    else: 
        return curSum
    if k <= numNegOnes: 
        return curSum -k
    
# numOnes = 3 
# numZeros = 2
# numNegOnes = 0
# k = 2


# numOnes = 3 
# numZeros = 2
# numNegOnes = 3
# k = 7
# print(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))





def primeSubOperation(nums):
    memo = {}
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
                307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
                401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
                503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
                601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
                809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
                907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

# for the number, take num - p
# 


    def largestAdjNumLessThan(num, cap):
        if (num, cap) in memo: 
            return memo[(num, cap)]
        if num < cap: 
            memo[(num, cap)] = num
            return num
        else:
            res = num
            for p in primes: 
                if p > num or (num - p) < 1: 
                    break
                if num - p < cap: 
                    res = (num-p)
                    break

            memo[(num, cap)] = res
            return res

    for i in range(len(nums)-2, -1, -1):
        if nums[i] < nums[i+1]:
            continue
        else: 
            nums[i] = largestAdjNumLessThan(nums[i], nums[i+1])
            if nums[i] >= nums[i+1]:
                return False
    # print(nums)
    return True
            

nums = [6,8,11,12]
# nums = [5,8,3] 
## False
# nums = [998,2]
print(primeSubOperation(nums))


    # for i in range(len(primes)):
    #     if i == 0 or i == 1: 
    #         primes[i] == False
    #     elif primes[i] == None: 
    #         primes[i] == True
    #         cur = 2
    #         while i*cur < 1000:
    #             if primes[i*cur] == None: 
    #                 primes[i*cur] = False
    #             cur +=1
    #     elif primes[i] == False: 
    #         continue