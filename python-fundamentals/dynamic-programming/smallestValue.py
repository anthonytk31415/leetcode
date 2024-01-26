
from collections import Counter



# memory limit 

def smallestValue2(n):

    def sieve_of_eratosthenes(limit):
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if primes[i]:
                for j in range(i*i, limit + 1, i):
                    primes[j] = False

        return [num for num, is_prime in enumerate(primes) if is_prime]


    primes = sieve_of_eratosthenes(n+1)
    memo = {x:x for x in primes}
    primeSum = {x:x for x in primes}
    def dfs(k): 
        
        if k in memo: return memo[k]
            # else: return dfs(memo[k])
            # if memo[k] == k: return k

        decomp = k
        kPrimeFactors = 0
        res = 0

        # we know k is not prime; find smallest prime that divides k evenly
        for prime in primes: 
            if decomp % prime == 0: 
                kPrimeFactors += prime
                decomp = decomp // prime
                break 
        kPrimeFactors += primeSum[decomp]
        primeSum[k] = kPrimeFactors

        if kPrimeFactors != k: res = dfs(kPrimeFactors)
        else: res = k
            
        memo[k] = res
        return res

    for i in range(3, n+1):
        dfs(i)
    
    # print(memo)
    return memo[n]



# arr = [1,2,3]
# myDict = {x:x for x in arr}
# print(myDict)


# 2 -> 2 (prime -> no divisors)
# 3 -> 3 (prime -> no divisors)
# 4 -> 2 + dfs(2) = 2 -> 4
# 5 -> 5
# 6 -> 2 + dfs(3) = 3 -> 5
# 7 -> 7
# 8 -> 2 + dfs(4) -> 6 -> 5
# 9 -> 3 + dfs(3) -> 6 -> 5
# 10 -> 2 + dfs(5) -> 7
# 11 -> 11
# 12 -> 2 + dfs(6) -> 7
# 13 -> 13
# 14 -> 2 + dfs(7) -> 9
# 15 -> 3 + dfs(5) -> 8
# 16 -> 2 + dfs(8) = 2 + 5 = 7

# 18 -> 2 + dfs(9) 2 + 5 



# below is too slow

def smallestValue1(n):
    primes = [2]
    primeFactors = {2: 2} # [prime factors, sum]
    memo = {2:2}
    def dfs(k): 
        if k in memo: return memo[k]

        kPrimeFactors = 0
        decomp = k
        for prime in primes: 
            if decomp % prime == 0: 
                kPrimeFactors += prime
                decomp = decomp // prime
                break 
        res = 0
        if kPrimeFactors > 0: 
            kPrimeFactors += primeFactors[decomp]
            if kPrimeFactors != k: res = dfs(kPrimeFactors)
            else: res = k
            
        else: 
            res = k
            primes.append(k)
            kPrimeFactors += k

        primeFactors[k] = kPrimeFactors
        memo[k] = res
        return res


    for i in range(3, n+1):
        dfs(i)
    
    print(memo)
    return memo[n]




def smallestValue(n):

    def sieve_of_eratosthenes(limit):
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if primes[i]:
                for j in range(i*i, limit + 1, i):
                    primes[j] = False

        return [num for num, is_prime in enumerate(primes) if is_prime]


    primes = sieve_of_eratosthenes(n)
    primeSet = set(primes)    
    val = n
    while val not in primeSet:
        reduced = val
        primeSum = 0
        for prime in primes: 
            if prime > reduced: break 
            while reduced % prime == 0: 
                primeSum += prime
                reduced = reduced//prime
        if val == primeSum: break 
        val = primeSum
        

    return val



print(smallestValue(16)) # 5
# print(smallestValue(16)) # 5

print(smallestValue(99957))
print(smallestValue(99958))
